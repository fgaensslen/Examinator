import html
import math
import os
from pathlib import Path
import random
import re
import urllib.parse
import frontmatter
import streamlit as st
import yaml

# Import custom modules
from config import (
    BASE_DIR, QUESTIONS_DIR, PAGE_TITLE, PAGE_ICON,
    ITEMS_PER_PAGE, DEFAULT_QUESTIONS, HR_DIVIDER
)
from styles import apply_styles
from utils import load_last_updates, get_available_exams, load_questions
from parsers import parse_case_study
from state import initialize_session_state, toggle_favorite
from helpers import check_answer_status, render_divider, render_selectbox


def colorize_sql_fragment(text: str) -> str:
    """Colorize SQL keywords/operators in an already display-formatted text fragment."""
    if not text:
        return text

    # Protect quoted literals so later keyword/type passes do not recolor inside quotes.
    string_tokens = []
    token_prefix = "%%SQLSTRTOKEN"
    token_suffix = "%%"

    def _stash_string(m):
        string_tokens.append(m.group(0))
        return f"{token_prefix}{len(string_tokens) - 1}{token_suffix}"

    text = re.sub(r"'[^']*'|\"[^\"]*\"", _stash_string, text)

    # Variables (e.g. @KnownIssueDescription)
    text = re.sub(
        r"(@[A-Za-z_][A-Za-z0-9_]*)",
        r"<span style='color:#111827;'>\1</span>",
        text,
    )

    # Core SQL keywords + control-flow / DDL / transaction tokens.
    blue_keywords = (
        "SELECT", "FROM", "WHERE", "JOIN", "AS", "ORDER", "BY", "GROUP", "HAVING",
        "DESC", "ASC", "TOP", "DISTINCT", "MATCH", "INSERT", "INTO", "VALUES",
        "UPDATE", "SET", "DELETE", "CREATE", "ALTER", "DROP", "OR", "PROCEDURE",
        "BEGIN", "END", "TRY", "CATCH", "THROW", "TRANSACTION", "COMMIT", "ROLLBACK",
        "DECLARE", "IF", "ELSE", "RETURN", "OUTPUT", "EXEC", "EXECUTE", "USE",
        "TABLE", "VIEW", "FUNCTION", "WITH", "OVER", "PARTITION", "UNION", "ALL",
        "CASE", "WHEN", "THEN", "IS", "NOT", "NULL", "EXISTS", "IN", "BETWEEN"
    )
    text = re.sub(
        r"\b(" + "|".join(blue_keywords) + r")\b",
        lambda m: f"<span style='color:#2b7de9;'>{m.group(0)}</span>",
        text,
        flags=re.IGNORECASE,
    )

    # SQL data types (blue in SSMS-like style).
    type_keywords = (
        "INT", "BIGINT", "SMALLINT", "TINYINT", "BIT", "DECIMAL", "NUMERIC", "FLOAT",
        "REAL", "MONEY", "SMALLMONEY", "CHAR", "NCHAR", "VARCHAR", "NVARCHAR", "TEXT",
        "NTEXT", "DATE", "DATETIME", "DATETIME2", "SMALLDATETIME", "TIME", "UNIQUEIDENTIFIER"
    )
    text = re.sub(
        r"\b(" + "|".join(type_keywords) + r")\b",
        lambda m: f"<span style='color:#2b7de9;'>{m.group(0)}</span>",
        text,
        flags=re.IGNORECASE,
    )

    # Built-in function names (magenta-ish in SSMS-like appearance).
    function_keywords = (
        "SYSUTCDATETIME", "GETDATE", "CURRENT_TIMESTAMP", "DATEDIFF", "DATEADD", "DATEPART",
        "JSON_VALUE", "JSON_QUERY", "ISNULL", "COALESCE", "COUNT", "SUM", "AVG", "MIN", "MAX",
        "EDIT_DISTANCE", "EDIT_DISTANCE_SIMILARITY"
    )
    text = re.sub(
        r"\b(" + "|".join(function_keywords) + r")\s*(?=\()",
        lambda m: f"<span style='color:#ff00ff;'>{m.group(0)}</span>",
        text,
        flags=re.IGNORECASE,
    )

    # Keep logical connectors visually distinct, but keep ON blue.
    text = re.sub(
        r"\b(AND)\b",
        lambda m: f"<span style='color:#f08a24;'>{m.group(0)}</span>",
        text,
        flags=re.IGNORECASE,
    )

    # Restore quoted literals in red.
    for idx, token in enumerate(string_tokens):
        text = text.replace(f"{token_prefix}{idx}{token_suffix}", f"<span style='color:#ef4444;'>{token}</span>")

    return text


@st.cache_data
def load_svg_data_uri(file_name: str) -> str:
    """Return a data URI for an SVG file in static/, or empty string if missing."""
    logo_path = BASE_DIR / "static" / file_name
    if not logo_path.exists():
        return ""

    svg_raw = logo_path.read_text(encoding="utf-8")
    return f"data:image/svg+xml;utf8,{urllib.parse.quote(svg_raw)}"

# Page config
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

# Apply custom CSS
apply_styles()

# Initialize session state
initialize_session_state()

# -------------------------------------------------------------
# View 1: Main Dashboard
# -------------------------------------------------------------
if st.session_state.current_view == "dashboard":
    st.markdown("""
        <div style="text-align: center;">
            <h1 style="margin: 0; padding: 0; line-height: 1.5;">Examinator</h1>
        </div>
    """, unsafe_allow_html=True)

    exams = get_available_exams()
    if not exams:
        st.warning("No question folders found.")

    last_updates = load_last_updates()
    ms_logo_uri = load_svg_data_uri("MS_logo.svg")
    github_logo_uri = load_svg_data_uri("GitHub_logo.svg")

    def _exam_category(exam_code: str) -> str:
        prefix = exam_code.split("-")[0].upper()
        if prefix == "GH":
            return "GitHub"
        if prefix in {"SC", "MS", "MD"}:
            return "Security"
        if prefix in {"MB", "PL", "AB"}:
            return "AI Business Solutions"
        return "Cloud & AI Platforms"

    section_order = [
        "Cloud & AI Platforms",
        "AI Business Solutions",
        "Security",
        "GitHub",
    ]
    categorized_exams = {section: [] for section in section_order}

    for exam_name, q_count in exams:
        section = _exam_category(exam_name)
        categorized_exams[section].append((exam_name, q_count))

    visible_sections = [s for s in section_order if categorized_exams.get(s)]

    if not visible_sections:
        st.info("No exam categories available.")

    st.markdown('<div class="exam-board">', unsafe_allow_html=True)
    board_cols = st.columns(len(visible_sections), gap="medium") if visible_sections else []

    for col_idx, section_name in enumerate(visible_sections):
        section_class = re.sub(r"[^a-z0-9]+", "-", section_name.lower()).strip("-")
        with board_cols[col_idx]:
            title_size = "20px"
            title_weight = "900"
            st.markdown(
                f"""
                <div class="exam-column-title-wrap {section_class}">
                    <div class="exam-column-title" style="font-size:{title_size}; font-weight:{title_weight}; text-transform:none; color:#0f172a; text-align:center;">
                        {section_name}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            section_exams = sorted(
                categorized_exams.get(section_name, []),
                key=lambda exam: exam[0] not in st.session_state.favorite_exams,
            )

            for exam_name, q_count in section_exams:
                date_str = last_updates.get(exam_name)
                update_line = f"Updated {date_str}" if date_str else "Update date unavailable"
                logo_uri = github_logo_uri if exam_name.upper().startswith("GH-") else ms_logo_uri
                logo_html = (
                    f'<img src="{logo_uri}" alt="logo" style="height:16px; width:16px; object-fit:contain; display:inline-block;" />'
                    if logo_uri
                    else ""
                )

                with st.container(border=True):
                    with st.container(key=f"exam-header-{exam_name}"):
                        code_col, count_col = st.columns(
                            [4, 3], gap="small", vertical_alignment="center"
                        )
                        with code_col:
                            st.markdown(
                                f"""
                                <div class="exam-tile-code-chip" style="color:#ffffff;">
                                    <span class="exam-tile-code" style="font-size:15px; font-weight:900; color:#ffffff; line-height:1.1; display:flex; align-items:center; gap:7px;">{logo_html}<span>{exam_name}</span></span>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )
                        with count_col:
                            st.markdown(
                                f'<div class="exam-tile-count" style="font-size:15px;color:#ffffff; white-space:nowrap; text-align:right;">{q_count} Questions</div>',
                                unsafe_allow_html=True,
                            )
                        update_col, favorite_col = st.columns([6, 1], gap="small", vertical_alignment="bottom")
                        with update_col:
                            st.markdown(
                                f'<div class="exam-tile-meta" style="margin-top:6px; font-size:13px; color:#dbeafe;">{update_line}</div>',
                                unsafe_allow_html=True,
                            )
                        with favorite_col:
                            is_favorite = exam_name in st.session_state.favorite_exams
                            if st.button(
                                "★" if is_favorite else "☆",
                                key=f"favorite_{exam_name}",
                            ):
                                toggle_favorite(exam_name)
                                st.rerun()

                    st.markdown(
                        '<div style="font-size:15px; font-weight:600; margin: 0 0 2px 0;">Number of questions</div>',
                        unsafe_allow_html=True,
                    )
                    default_value = min(DEFAULT_QUESTIONS, q_count)
                    num_qs = st.slider(
                        "Number of questions",
                        min_value=1,
                        max_value=q_count,
                        value=default_value,
                        label_visibility="collapsed",
                        key=f"slider_{exam_name}",
                    )

                    if st.button(
                        "Start Practice Exam",
                        key=f"start_{exam_name}",
                        type="secondary",
                        use_container_width=True,
                    ):
                        st.session_state.selected_exam = exam_name
                        st.session_state.quiz_data = load_questions(exam_name)

                        random.shuffle(st.session_state.quiz_data)
                        st.session_state.quiz_data = st.session_state.quiz_data[:num_qs]

                        st.session_state.mode = "exam"
                        st.session_state.current_q_idx = 0
                        st.session_state.panel_page = 1
                        st.session_state.selected_answers = {}
                        st.session_state.checked_questions = set()
                        st.session_state.current_view = "quiz"
                        st.rerun()

                    if st.button(
                        "Browse all questions",
                        key=f"browse_{exam_name}",
                        use_container_width=True,
                    ):
                        st.session_state.selected_exam = exam_name
                        st.session_state.quiz_data = load_questions(exam_name)
                        st.session_state.mode = "browse"
                        st.session_state.current_q_idx = 0
                        st.session_state.selected_answers = {}
                        st.session_state.checked_questions = set()
                        st.session_state.current_view = "quiz"
                        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# View 2: Quiz Presentation with Sidebar Navigation
# -------------------------------------------------------------
elif st.session_state.current_view == "quiz":
    questions = st.session_state.quiz_data
    total_qs = len(questions)

    if st.session_state.current_q_idx >= total_qs:
        st.session_state.current_q_idx = 0

    current_idx = st.session_state.current_q_idx
    
    total_pages = math.ceil(total_qs / ITEMS_PER_PAGE)
    curr_page = st.session_state.panel_page
    
    start_item_idx = (curr_page - 1) * ITEMS_PER_PAGE
    end_item_idx = min(start_item_idx + ITEMS_PER_PAGE, total_qs)
    
    if current_idx not in st.session_state.selected_answers:
        st.session_state.selected_answers[current_idx] = {} if questions[current_idx]["is_drag_drop"] else []
        
    # --- SIDEBAR NAV PANEL ---
    with st.sidebar:
        side_head_col1, side_head_col2 = st.columns([2, 1])
        with side_head_col1:
            st.write(f"### {total_qs} questions")
        with side_head_col2:
            if st.button("🏠 Start", key="side_exit_btn", type="secondary"):
                st.session_state.current_view = "dashboard"
                st.rerun()

        st.markdown(
            f'<div style="font-weight: bold; margin-bottom: 8px;">'
            f'{start_item_idx + 1}–{end_item_idx} <span style="font-size: 12px; font-weight: normal; color: #666; text-transform: lowercase;">of</span> {total_qs}'
            f'</div>', 
            unsafe_allow_html=True
        )
        
        for row_start in range(start_item_idx, end_item_idx, 4):
            cols = st.columns(4)
            for c_offset in range(4):
                item_idx = row_start + c_offset
                if item_idx < end_item_idx:
                    with cols[c_offset]:
                        q_item = questions[item_idx]
                        is_answered, is_wrong, is_correct = check_answer_status(item_idx, q_item)

                        btn_type = "primary" if item_idx == current_idx else "secondary"
                        
                        label = f"{item_idx + 1}"
                        if is_wrong: label = f"{item_idx + 1} ✗"
                        elif is_correct: label = f"{item_idx + 1} ✓"
                        elif is_answered: label = f"{item_idx + 1} ●"

                        if st.button(label, key=f"nav_grid_{item_idx}", type=btn_type, use_container_width=True):
                            st.session_state.current_q_idx = item_idx
                            st.rerun()
        
        st.write("---")
        
        display_pages = {1, curr_page, min(curr_page + 1, total_pages), total_pages}
        sorted_pages = sorted(list(display_pages))
        
        st.markdown('<div class="custom-pagination-row">', unsafe_allow_html=True)
        nav_columns = st.columns(6) 
        
        with nav_columns[0]:
            if st.button("«", disabled=(curr_page == 1), key="nav_prev_page"):
                st.session_state.panel_page -= 1
                st.rerun()
        
        for idx in range(4):
            with nav_columns[idx + 1]:
                if idx < len(sorted_pages):
                    p_num = sorted_pages[idx]
                    p_btn_type = "primary" if p_num == curr_page else "secondary"
                    if st.button(f"{p_num}", key=f"nav_page_{p_num}", type=p_btn_type):
                        st.session_state.panel_page = p_num
                        st.rerun()
                else:
                    st.write("")
                    
        with nav_columns[5]:
            if st.button("»", disabled=(curr_page == total_pages or total_pages <= 1), key="nav_next_page"):
                st.session_state.panel_page += 1
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)
    
    # --- MAIN BODY PRESENTATION ---
    @st.dialog("Case Study Details", width="large")
    def show_case_study_dialog(case_study_filename):
        current_exam = st.session_state.get("selected_exam", "")
        case_study_dir = os.path.join(QUESTIONS_DIR, current_exam, "case_studies")
        file_path = os.path.join(case_study_dir, case_study_filename)
        
        sections, metadata = parse_case_study(file_path)
        
        if not sections:
            st.error(f"Could not load case study file from path: {file_path}")
            return
            
        tab_titles = list(sections.keys())
        tabs = st.tabs(tab_titles)
        
        for tab, (heading, body) in zip(tabs, sections.items()):
            with tab:
                st.markdown(f"### {heading}")
                tokens = re.split(r"(!\[.*?\]\(.*?\))", body)
                for token in tokens:
                    token = token.strip()
                    if not token:
                        continue
                    img_match = re.match(r"!\[(.*?)\]\((.*?)\)", token)
                    if img_match:
                        alt_text, img_file = img_match.groups()
                        img_path = os.path.join(case_study_dir, img_file)
                        if os.path.exists(img_path):
                            st.image(img_path, caption=alt_text, width="content")
                        else:
                            st.warning(f"Image not found: {img_file}")
                    else:
                        st.markdown(token, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: center;">
            <h1 style="margin: 0; padding: 0; line-height: 1.5;">Examinator</h1>
            <h4 style="margin: 4px 0 10px 0; padding: 0; color: gray; font-weight: normal;">
                <b>{st.session_state.selected_exam}</b> - {'Study Mode' if st.session_state.mode == 'browse' else 'Practice Exam'}
            </h4>
            <hr style="margin: 10px 0 15px 0; border: none; border-top: 1px solid #e0e0e0;">
        </div>
    """, unsafe_allow_html=True)
    
    q = questions[current_idx]
    current_q_filename = q.get("filename", f"question_{current_idx:03d}.md")
    current_exam = st.session_state.get("selected_exam", "")

    # Determine if a case study exists
    matched_case_study = None
    case_study_dir = os.path.join(QUESTIONS_DIR, current_exam, "case_studies")

    if os.path.exists(case_study_dir):
        for cs_file in os.listdir(case_study_dir):
            if cs_file.endswith(".md"):
                sections, metadata = parse_case_study(os.path.join(case_study_dir, cs_file))
                linked_qs = metadata.get("linked_questions", [])
                if current_q_filename in linked_qs:
                    matched_case_study = cs_file
                    break

    col_header, col_btn = st.columns([3, 1], vertical_alignment="center")

    with col_header:
        st.markdown(
            f'<h3 style="margin: 0; padding: 0; line-height: 1.2;">Question {current_idx + 1} of {total_qs}</h3>', 
            unsafe_allow_html=True
        )

    if matched_case_study:
        with col_btn:
            if st.button("📖 Case Study", use_container_width=True, type="secondary"):
                show_case_study_dialog(matched_case_study)

    st.markdown(
        '<hr style="margin: 10px 0 15px 0; border: none; border-top: 1px solid #e0e0e0;">', 
        unsafe_allow_html=True
    )

    st.markdown(q["question"], unsafe_allow_html=True)   

    st.markdown(
        '<hr style="margin: 10px 0 15px 0; border: none; border-top: 1px solid #e0e0e0;">', 
        unsafe_allow_html=True
    )
    
    is_checked = current_idx in st.session_state.checked_questions
    current_selections = st.session_state.selected_answers[current_idx]

    # Render Interactive Drag-and-Drop or Standard Multiple Choice
    if q["is_drag_drop"]:
        values_pool = q["choices"]
        correct_map = q["correct"]
        code_template = q["code_template"]
        is_code = q.get("is_code", False)
        code_lang = q.get("code_lang", "")
        
        dropdown_options = [""] + values_pool
        template_lines = code_template.split("\n")
        
        container_ctx = st.container(border=True) if is_code else st.container()
        
        with container_ctx:
            if is_code and code_lang:
                st.markdown(f'<div class="code-box-header"><span>{code_lang}</span></div>', unsafe_allow_html=True)
            
            for line in template_lines:
                has_placeholder = any(f"{{{b_key}}}" in line for b_key in correct_map.keys())
                
                if not has_placeholder:
                    if not line.strip():
                        st.write("")
                        continue
                    if is_code:
                        leading_spaces = len(line) - len(line.lstrip(' '))
                        indent_str = "&nbsp;" * leading_spaces
                        safe_line = line.strip().replace(" ", "&nbsp;")
                        if code_lang.upper() == "SQL":
                            safe_line = colorize_sql_fragment(safe_line)
                        st.markdown(f'<div class="code-line">{indent_str}{safe_line}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(line)
                else:
                    for b_key in sorted(correct_map.keys(), key=lambda x: int(x.split('_')[1]) if '_' in x else 0):
                        placeholder = f"{{{b_key}}}"
                        if placeholder in line:
                            parts = line.split(placeholder)
                            raw_prefix = parts[0]
                            raw_suffix = parts[1] if len(parts) > 1 else ""
                            
                            leading_spaces = len(raw_prefix) - len(raw_prefix.lstrip(' '))
                            col_prefix = raw_prefix.strip().replace(" ", "&nbsp;")
                            col_suffix = raw_suffix.strip().replace(" ", "&nbsp;")
                            if is_code and code_lang.upper() == "SQL":
                                col_prefix = colorize_sql_fragment(col_prefix)
                                col_suffix = colorize_sql_fragment(col_suffix)
                            
                            b_val = current_selections.get(b_key, "")
                            
                            if not is_checked:
                                if is_code:
                                    st.markdown(f'<div class="code-line-row" style="margin-left: {leading_spaces}ch;">', unsafe_allow_html=True)
                                    
                                    cols_list = []
                                    if col_prefix:
                                        cols_list.append("prefix")
                                    cols_list.append("selectbox")
                                    if col_suffix:
                                        cols_list.append("suffix")
                                    
                                    cols = st.columns(len(cols_list), vertical_alignment="center")
                                    c_idx = 0
                                    
                                    if "prefix" in cols_list:
                                        with cols[c_idx]:
                                            st.markdown(f'<div class="code-line">{col_prefix}</div>', unsafe_allow_html=True)
                                        c_idx += 1
                                        
                                    with cols[c_idx]:
                                        b_choice = st.selectbox(
                                            f"Select for {b_key}", 
                                            dropdown_options, 
                                            index=dropdown_options.index(b_val) if b_val in dropdown_options else 0, 
                                            key=f"dd_{current_idx}_{b_key}", 
                                            label_visibility="collapsed"
                                        )
                                        st.session_state.selected_answers[current_idx][b_key] = b_choice
                                    c_idx += 1
                                    
                                    if "suffix" in cols_list:
                                        with cols[c_idx]:
                                            st.markdown(f'<div class="code-line">{col_suffix}</div>', unsafe_allow_html=True)
                                            
                                    st.markdown('</div>', unsafe_allow_html=True)
                                else:
                                    if col_prefix and not col_suffix:
                                        c_label, c_input = st.columns([3, 7], vertical_alignment="center")
                                        with c_label:
                                            st.markdown(f"**{col_prefix}**")
                                        with c_input:
                                            b_choice = st.selectbox(
                                                f"Select for {b_key}", 
                                                dropdown_options, 
                                                index=dropdown_options.index(b_val) if b_val in dropdown_options else 0, 
                                                key=f"dd_{current_idx}_{b_key}", 
                                                label_visibility="collapsed"
                                            )
                                            st.session_state.selected_answers[current_idx][b_key] = b_choice
                                    else:
                                        if col_prefix:
                                            st.markdown(f"**{col_prefix}**")
                                        b_choice = st.selectbox(
                                            f"Select for {b_key}", 
                                            dropdown_options, 
                                            index=dropdown_options.index(b_val) if b_val in dropdown_options else 0, 
                                            key=f"dd_{current_idx}_{b_key}", 
                                            label_visibility="collapsed"
                                        )
                                        st.session_state.selected_answers[current_idx][b_key] = b_choice
                                        if col_suffix:
                                            st.markdown(col_suffix)
                            else:
                                b_correct = correct_map.get(b_key, "")
                                safe_val = html.escape(b_val if b_val else "[No answer]")
                                safe_correct = html.escape(b_correct)
                                
                                if b_val == b_correct:
                                    badge_html = f'<span class="code-blank-correct">[{safe_val}]</span>'
                                else:
                                    badge_html = (
                                        f'<span style="display:inline-block; vertical-align:top;">'
                                        f'<span class="code-blank-wrong">[{safe_val}]</span>'
                                        f'<br><span style="color: green; font-weight: bold;">[{safe_correct}]</span>'
                                        f'</span>'
                                    )
                                
                                if is_code:
                                    indent_str = "&nbsp;" * leading_spaces
                                    prefix_str = f"{col_prefix} " if col_prefix else ""
                                    suffix_str = f" {col_suffix}" if col_suffix else ""
                                    combined_html = f'<div class="code-line">{indent_str}{prefix_str}{badge_html}{suffix_str}</div>'
                                    st.markdown(combined_html, unsafe_allow_html=True)
                                else:
                                    prefix_str = f"**{col_prefix}** " if col_prefix else ""
                                    suffix_str = f" {col_suffix}" if col_suffix else ""
                                    st.markdown(f"{prefix_str}{badge_html}{suffix_str}", unsafe_allow_html=True)
    else:
        for c_idx, choice in enumerate(q["choices"]):
            is_selected = c_idx in current_selections
            is_correct_choice = c_idx in q["correct"]
            
            if not is_checked:
                btn_type = "primary" if is_selected else "secondary"
                button_label = choice.replace("\\", "\\\\").replace("$", "\\$")
                
                if st.button(button_label, key=f"btn_choice_{current_idx}_{c_idx}", use_container_width=True, type=btn_type):
                    max_allowed = len(q["correct"])
                    
                    if max_allowed == 1:
                        st.session_state.selected_answers[current_idx] = [c_idx]
                    else:
                        if c_idx in current_selections:
                            st.session_state.selected_answers[current_idx].remove(c_idx)
                        else:
                            if len(current_selections) < max_allowed:
                                st.session_state.selected_answers[current_idx].append(c_idx)
                            else:
                                st.toast(f"You can only select {max_allowed} answers.")
                    st.rerun()
            else:
                safe_choice = html.escape(choice)

                if is_correct_choice:
                    badge_html = '<span class="badge-correct">Your Answer</span>' if is_selected else ''
                    st.markdown(
                        f'<div class="feedback-card card-correct">'
                        f'<span class="choice-text">{safe_choice}</span>'
                        f'{badge_html}'
                        f'</div>',
                        unsafe_allow_html=True
                    )
                elif is_selected and not is_correct_choice:
                    st.markdown(
                        f'<div class="feedback-card card-wrong">'
                        f'<span class="choice-text">{safe_choice}</span>'
                        f'<span class="badge-wrong">Your Answer</span>'
                        f'</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f'<div class="feedback-card card-neutral">'
                        f'<span class="choice-text">{safe_choice}</span>'
                        f'</div>',
                        unsafe_allow_html=True
                    )

    if is_checked and q["ans_image"]:
        st.write("---")
        st.image(q["ans_image"], use_container_width=True)

    st.write("")

    @st.dialog("Selection Hint")
    def show_selection_hint(required_count: int, selected_count: int):
        remaining = required_count - selected_count
        st.info(
            f"This question requires **{required_count}** answers. "
            f"You have selected **{selected_count}** so far. "
            f"\n\nPlease select **{remaining}** more to continue."
        )
        if st.button("OK", use_container_width=True):
            st.rerun()
    
    # --- Bottom Layout Action Buttons Row ---
    st.markdown('<div class="quiz-action-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if current_idx > 0:
            if st.button("⬅️ Previous Question", key=f"prev_{current_idx}", disabled=(current_idx == 0), use_container_width=True):
                st.session_state.current_q_idx -= 1
                if st.session_state.current_q_idx < (st.session_state.panel_page - 1) * ITEMS_PER_PAGE:
                    st.session_state.panel_page -= 1
                st.rerun()
        else:
            st.empty()
            
    with col2:
        if st.session_state.mode == "browse":
            if q["is_drag_drop"]:
                can_check = all(v != "" for v in current_selections.values())
            else:
                can_check = (len(current_selections) == len(q["correct"]))
            required_answers = len(q["correct"]) if not q["is_drag_drop"] else 0

            single_answer_disabled = (not q["is_drag_drop"]) and required_answers == 1 and len(current_selections) == 0
            
            if st.button("Check Answer", 
                         key=f"chk_btn_{current_idx}", 
                         disabled=is_checked or (q["is_drag_drop"] and not can_check) or single_answer_disabled,
                         use_container_width=True):
                if (not q["is_drag_drop"]) and required_answers >= 2 and len(current_selections) < required_answers:
                    show_selection_hint(required_answers, len(current_selections))
                    st.stop()
                st.session_state.checked_questions.add(current_idx)
                st.rerun()
        else:
            st.empty()

    with col3:
        if current_idx + 1 < total_qs:
            if st.button("Next Question ➡️", key=f"next_{current_idx}", use_container_width=True):
                if st.session_state.mode == "exam" and (not q["is_drag_drop"]):
                    required_answers = len(q["correct"])
                    selected_count = len(current_selections)
                    if required_answers >= 2 and selected_count < required_answers:
                        show_selection_hint(required_answers, selected_count)
                        st.stop()
                st.session_state.current_q_idx += 1
                if st.session_state.current_q_idx >= (st.session_state.panel_page * ITEMS_PER_PAGE):
                    st.session_state.panel_page += 1
                st.rerun()
        else:
            if st.session_state.mode == "exam":
                if st.button("🚀 Submit Exam", key="submit_exam", use_container_width=True):
                    answered_count = len([i for i in range(total_qs) if st.session_state.selected_answers.get(i)])
                    st.session_state.summary_data = (answered_count, total_qs - answered_count)
                    st.session_state.show_summary = True
                    st.rerun()
            else:
                st.empty()

    @st.dialog("Exam Results")
    def show_summary(answered, unanswered):
        correct_count = 0
        total_qs = len(questions)
        
        for idx, q_item in enumerate(questions):
            user_ans = st.session_state.selected_answers.get(idx, [])
            if q_item["is_drag_drop"]:
                if user_ans == q_item["correct"]:
                    correct_count += 1
            else:
                if sorted(user_ans) == sorted(q_item["correct"]):
                    correct_count += 1
                    
        score_pct = (correct_count / total_qs) * 100 if total_qs > 0 else 0        
        
        st.write(f"You answered **{correct_count} out of {total_qs}** questions correctly.")
        st.markdown(f"<h2>Total Score: {score_pct:.1f}%</h2>", unsafe_allow_html=True)
        st.write("")
        
        if st.button("Close & Review", type="primary", use_container_width=True):
            st.session_state.submitted = True
            st.session_state.checked_questions = set(range(total_qs))
            del st.session_state.show_summary
            st.rerun()

    if st.session_state.get("show_summary"):
        show_summary(*st.session_state.summary_data)

    st.markdown('</div>', unsafe_allow_html=True)