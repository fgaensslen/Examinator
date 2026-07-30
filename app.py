import html
import math
import os
from pathlib import Path
import random
import re
import frontmatter
import streamlit as st
import yaml

# Path Configuration
BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_DIR = BASE_DIR / "static" / "questions"

# Page config
st.set_page_config(page_title="Examinator", page_icon="🎓", layout="centered")

# Custom CSS layout corrections
st.markdown("""
    <style>
    /* FORCE COMPLETE DISAPPEARANCE OF ALL SCROLLBARS EVERYWHERE */
    * {
        scrollbar-width: none !important; /* Firefox */
    }
    *::-webkit-scrollbar {
        display: none !important; /* Chrome, Safari, Opera, Edge */
    }
    html, body, [data-testid="stAppViewContainer"], .stApp {
        overflow: hidden !important;
        height: 100vh !important;
    }
    
    /* Shift sidebar contents down from top edge naturally */
    [data-testid="stSidebarUserContent"] {
        padding-top: 3rem !important;
    }

    /* MOVE THE MIDDLE MAIN CONTAINER BLOCKS SLIGHTLY HIGHER */
    [data-testid="stMainBlockContainer"] {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }

    /* DASHBOARD MODE SELECTION BUTTONS */
    .dashboard-btn-container button {
        width: 320px !important;      
        min-width: 320px !important;
        max-width: 320px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        display: block !important;
        padding: 18px 24px !important;
        font-size: 22px !important;    
        font-weight: bold !important;
        margin-bottom: 12px !important;
        border-radius: 8px !important;
    }
    .dashboard-btn-container button p {
        font-size: 22px !important;
        line-height: 1.3 !important;
    }
    
    /* CLEAN ACTION BUTTONS BELOW QUESTIONS (NO OVERLAPPING) */
    .quiz-action-container button {
        padding: 8px 16px !important;
        font-size: 15px !important;
        border-radius: 6px !important;
        width: auto !important;
    }
    
    /* MAKES ALL BUTTONS IN THE SIDEBAR SMALLER & CONSISTENT */
    div[data-testid="stSidebar"] button p {
        font-size: 12px !important;
    }
    div[data-testid="stSidebar"] button {
        padding: 2px 4px !important;
        min-height: 28px !important;
        height: 28px !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
    }
    
    /* Target the bottom pagination container specifically to maintain rigid layout geometry */
    .custom-pagination-row [data-testid="stHorizontalBlock"] {
        gap: 4px !important;
        justify-content: flex-start !important;
    }
    .custom-pagination-row button {
        width: 32px !important;
        height: 32px !important;
        min-width: 32px !important;
        max-width: 32px !important;
        padding: 0px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border-radius: 6px !important;
    }

    /* REDUCE DROPDOWN MARGINS ONLY */
    [data-testid="stSelectbox"] {
        margin-top: -10px !important;
        margin-bottom: 0px !important;
    }

    /* Reduce the gap in vertical containers with selectboxes */
    div:has([data-testid="stSelectbox"]) {
        row-gap: 0.8rem !important;
    }
    
    .app-header {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }

    /* Update the main button styling for centralized text */
    [data-testid="stMainBlockContainer"] div[data-testid="stButton"] button {
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important; 
        text-align: left !important;
        width: 100% !important;
        padding: 10px 16px !important;
        border-radius: 8px !important;
        min-height: 45px !important;
        height: auto !important;
        margin-bottom: 8px !important;
    }

    /* Ensure the inner text container also centers */
    [data-testid="stMainBlockContainer"] div[data-testid="stButton"] button > div {
        display: flex !important;
        justify-content: flex-start !important;
        text-align: left !important;
        width: 100% !important;
    }

    /* Ensure the paragraph text is centered */
    [data-testid="stMainBlockContainer"] div[data-testid="stButton"] button p {
        text-align: left !important;   
        width: 100% !important;
        margin: 0 !important;
        font-size: 15px !important;
    }

    /* FEEDBACK CARD CONTAINERS - NO BUBBLES, TEXT LEFT ALIGNED */
    [data-testid="stMainBlockContainer"] div[data-testid="stButton"] button,
    .feedback-card {
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important; 
        text-align: left !important;
        width: 100% !important;
        padding: 10px 16px !important;
        border-radius: 8px !important;
        min-height: 48px !important;
        height: auto !important;
        margin-bottom: 8px !important;
        box-sizing: border-box !important;
    }

    .feedback-card {
        font-size: 15px !important;
        font-weight: 400 !important;
        justify-content: space-between !important;
    }
    .card-correct {
        border: 3px solid #10b981 !important;
        background-color: #86efac !important;
        color: #065f46 !important;
    }
    .card-wrong {
        border: 3px solid #ef4444 !important;
        background-color: #f87171 !important;
        color: #991b1b !important;
    }
    .card-neutral {
        border: 1px solid rgba(128, 128, 128, 0.5) !important;
        background-color: rgba(128, 128, 128, 0.25) !important;
        color: inherit !important;
    }
    
    .feedback-card span.choice-text {
        flex-grow: 1 !important;
        margin: 0 !important;
        line-height: 1.4 !important;
    }
    
    /* BADGES FOR SELECTED REVIEW STATE */
    .badge-wrong {
        background-color: #fecaca;
        color: #991b1b;
        border: 2px solid #ef4444;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        white-space: nowrap;
        margin-left: 15px;
    }
    .badge-correct {
        background-color: #bbf7d0;
        color: #065f46;
        border: 2px solid #10b981;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        white-space: nowrap;
        margin-left: 15px;
    }

    /* IN-CODE BLANK FEEDBOX FEEDBACK STYLING */
    .code-blank-correct {
        border: 2px solid #10b981 !important;
        background-color: #ecfdf5 !important;
        color: #065f46 !important;
        padding: 4px 10px !important;
        border-radius: 6px !important;
        font-family: 'Consolas', monospace !important;
        font-weight: bold !important;
        display: inline-block !important;
        margin: 2px 0 !important;
    }
    .code-blank-wrong {
        border: 2px solid #ef4444 !important;
        background-color: #fef2f2 !important;
        color: #991b1b !important;
        padding: 4px 10px !important;
        border-radius: 6px !important;
        font-family: 'Consolas', monospace !important;
        font-weight: bold !important;
        display: inline-block !important;
        margin: 2px 0 !important;
    }

    /* ELIMINATE JUMPING AND OFFSET EFFECTS ON STATE CHANGE */
    [data-testid="stMarkdownContainer"] .feedback-card {
        box-sizing: border-box !important;
        max-width: 100% !important;
    }
    [data-testid="stMarkdownContainer"] {
        margin: 0 !important;
        padding: 0 !important;
    }
    /* Restore list indentation */
    [data-testid="stMarkdownContainer"] ul,
    [data-testid="stMarkdownContainer"] ol {
        padding-left: 1.5rem !important;
        margin-left: 0 !important;
    }
            
    /* Sidebar Map Styles */
    .map-btn-answered {
        border: 2px solid #3b82f6 !important;
        background-color: #dbeafe !important;
    }
    .map-btn-unanswered {
        border: 1px solid #e2e8f0 !important;
        background-color: #ffffff !important;
    }
    .map-btn {
        display: block;
        padding: 10px;
        text-align: center;
        text-decoration: none !important;
        border-radius: 5px;
        border: 1px solid #ccc;
        color: inherit;
        font-weight: normal;
    }
    .map-btn:hover {
        text-decoration: none !important;
    }
    .map-unanswered { background-color: #ffffff; color: #333; }
    .map-answered { background-color: #dbeafe; color: #1e40af; border-color: #3b82f6; }
    .map-correct { background-color: #d1fae5; color: #065f46; border-color: #10b981; }
    .map-wrong { background-color: #fee2e2; color: #991b1b; border-color: #ef4444; }
    .map-current { outline: 3px solid #6366f1; }     

    /* CODE BLOCK & CONTAINER STYLING */
    .code-box-header {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        padding-bottom: 4px;
        margin-bottom: 6px;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 12px;
        font-weight: bold;
        color: #64748b;
        letter-spacing: 1px;
    }

    .code-line, 
    .code-line p {
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace !important;
        font-size: 13.5px !important;
        line-height: 1.25 !important;
        margin: 0 !important;
        padding: 0 !important;
        white-space: pre !important;
    }

    /* PREVENT CONTAINER OVERFLOW */
    div[data-testid="stContainer"] {
        overflow-x: auto !important;
    }

    /* INLINE FLEX ROW FOR DRAG-AND-DROP CODE LINES */
    .code-line-row {
        display: block !important;
        margin: 2px 0 !important;
    }

    .code-line-row [data-testid="stHorizontalBlock"] {
        display: inline-flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: flex-start !important;
        gap: 6px !important;
        width: auto !important;
        margin: 0 !important;
    }

    .code-line-row [data-testid="column"] {
        width: auto !important;
        flex: 0 0 auto !important;
        min-width: unset !important;
        padding: 0 !important;
    }

    /* CONTROL DROPDOWN WIDTH */
    .code-line-row [data-testid="stSelectbox"] {
        width: 320px !important;
        min-width: 220px !important;
        margin: 0 !important;
    }

    .code-line-row [data-testid="stSelectbox"] > div {
        min-height: 30px !important;
        max-height: 30px !important;
        font-size: 13px !important;
    }

    /* ------------------------------------------------------------- */
    /* RIGHT-ALIGN EXPANDER HEADER META TEXT                         */
    /* ------------------------------------------------------------- */

    /* 1. Force the markdown wrapper inside the header to grow to 100% width */
    [data-testid="stExpanderSummary"] div[data-testid="stMarkdownContainer"],
    details summary div[data-testid="stMarkdownContainer"] {
        flex-grow: 1 !important;
        width: 100% !important;
    }

    /* 2. Turn the paragraph into a full-width flex container */
    [data-testid="stExpanderSummary"] div[data-testid="stMarkdownContainer"] > p,
    details summary div[data-testid="stMarkdownContainer"] > p {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        width: 100% !important;
        margin: 0 !important;
    }

    /* 3. Push the colored/gray text span directly to the far right edge */
    [data-testid="stExpanderSummary"] div[data-testid="stMarkdownContainer"] p span,
    details summary div[data-testid="stMarkdownContainer"] p span {
        margin-left: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Helper Functions
# -------------------------------------------------------------
def load_last_updates(
    filepath: str = "static/last_update.md",
) -> dict[str, str]:
    """Reads static/last_update.md and returns a dict: {'DP-800': '18.07.2026', ...}"""
    updates = {}
    if not os.path.exists(filepath):
        return updates

    with open(filepath, "r", encoding="utf-8") as f:
        current_exam = None
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                current_exam = line.lstrip("#").strip()
            elif line and current_exam:
                updates[current_exam] = line
                current_exam = None

    return updates

def detect_code_language(template_text):
    text = template_text.strip()
    
    if (text.startswith("{") or text.startswith("[")) and ":" in text:
        return "JSON"
        
    # Removed |dbo\. so plain text descriptions don't trigger SQL formatting
    sql_pattern = r'\b(SELECT|FROM|WHERE|INSERT|UPDATE|DELETE|JOIN|ALTER|CREATE|ORDER\s+BY|GROUP\s+BY)\b'
    if re.search(sql_pattern, text, re.IGNORECASE):
        return "SQL"
        
    return "TEXT"

def parse_case_study(file_path):
    """Parses a case study markdown file containing YAML frontmatter and section headings."""
    if not os.path.exists(file_path):
        return None, {}
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    content = content.replace("\xa0", " ")
        
    metadata = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                metadata = yaml.safe_load(parts[1])
            except Exception as e:
                st.error(f"YAML Error in {file_path}: {e}")
            content = parts[2]
            
    pattern = r"^#\s+(.+?)\n(.*?)(?=\n^#\s+|\Z)"
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
    
    sections = {heading.strip(): body.strip() for heading, body in matches}
    return sections, metadata

def get_available_exams():
    if not os.path.exists(QUESTIONS_DIR):
        return []
    exams = []
    for item in os.listdir(QUESTIONS_DIR):
        item_path = os.path.join(QUESTIONS_DIR, item)
        if os.path.isdir(item_path) and not item.startswith(".") and not item.startswith("__"):
            md_files = [f for f in os.listdir(item_path) if f.endswith(".md")]
            if md_files:
                exams.append((item, len(md_files)))
    return sorted(exams)

def load_questions(exam_folder):
    questions = []
    folder_path = QUESTIONS_DIR / exam_folder
    
    if not folder_path.exists():
        return questions

    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
    web_image_prefix = f"app/static/questions/{exam_folder}/"
    
    for file in files:
        filepath = folder_path / file
        base_filename = filepath.stem
        
        with open(filepath, 'r', encoding='utf-8') as f:
            file_raw = f.read()
            
        post = frontmatter.loads(file_raw)
        question_frontmatter = post.get("question", "")
        
        ans_img_path = folder_path / f"{base_filename}_answer.png"
        ans_img = f"{web_image_prefix}{base_filename}_answer.png" if ans_img_path.exists() else None
        
        is_drag_drop = post.get("question_type") == "drag_drop"
        
        if is_drag_drop:
            choices = list(post.get("values_pool", []))
            random.shuffle(choices)
            
            correct_indices = post.get("correct_mapping", {})
            raw_template = post.content.strip()
            
            # 1. Read explicit language setting from frontmatter
            explicit_lang = str(post.get("code_lang", post.get("language", ""))).strip().upper()
            
            # 2. Check for fence blocks
            fence_match = re.match(r'^```([a-zA-Z0-9_+-]*)\s*\n(.*?)\n```$', raw_template, re.DOTALL)
            
            # Handle explicit frontmatter setting
            if explicit_lang:
                if explicit_lang in ["TEXT", "NONE", "PLAIN"]:
                    is_code = False
                    code_lang = ""
                    code_template = raw_template
                else:
                    is_code = True
                    code_lang = explicit_lang
                    code_template = raw_template
            elif fence_match:
                is_code = True
                code_lang = fence_match.group(1).upper() or "CODE"
                code_template = fence_match.group(2).strip()
            else:
                detected_lang = detect_code_language(raw_template)
                is_code = detected_lang != "TEXT"
                code_lang = detected_lang if is_code else ""
                code_template = raw_template

            question_text = question_frontmatter.strip()          
        else:
            raw_choices = []
            content_lines = post.content.strip().split("\n")
            question_lines = []
            
            for line in content_lines:
                match = re.match(r'^\s*-\s*\[([ xX])\]\s*(.*)$', line)
                if match:
                    is_correct = match.group(1).lower() == 'x'
                    raw_choices.append({"text": match.group(2).strip(), "is_correct": is_correct})
                else:
                    question_lines.append(line)
                    
            random.shuffle(raw_choices)
            choices = [item["text"] for item in raw_choices]
            correct_indices = [i for i, item in enumerate(raw_choices) if item["is_correct"]]
            
            code_template = ""
            is_code = False
            code_lang = ""
            
            question_text = "\n".join(question_lines).strip()
            if not question_text:
                question_text = question_frontmatter.strip()

        question_text = re.sub(
            r'!\[(.*?)\]\((?!https?://|app/static/|\./app/static/)(.*?)\)', 
            rf'![\1]({web_image_prefix}\2)', 
            question_text
        )
                
        questions.append({
            "filename": file,
            "question": question_text,
            "is_drag_drop": is_drag_drop,
            "choices": choices,
            "correct": correct_indices,
            "code_template": code_template,
            "is_code": is_code,
            "code_lang": code_lang,
            "ans_image": ans_img
        })
        
    return questions

# -------------------------------------------------------------
# State Management
# -------------------------------------------------------------
if "current_view" not in st.session_state:
    st.session_state.current_view = "dashboard"
if "selected_exam" not in st.session_state:
    st.session_state.selected_exam = None
if "mode" not in st.session_state:
    st.session_state.mode = None
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = []
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0
if "panel_page" not in st.session_state:
    st.session_state.panel_page = 1
if "selected_answers" not in st.session_state:
    st.session_state.selected_answers = {}  
if "checked_questions" not in st.session_state:
    st.session_state.checked_questions = set()
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# -------------------------------------------------------------
# View 1: Main Dashboard
# -------------------------------------------------------------
if st.session_state.current_view == "dashboard":    
    st.markdown("""
        <div style="text-align: center;">
            <h1 style="margin: 0; padding: 0; line-height: 1.5;">🎓 Examinator</h1>
        </div>
    """, unsafe_allow_html=True)

    exams = get_available_exams()
    
    if not exams:
        st.warning("No question folders found.")

    # Load the update dates
    last_updates = load_last_updates()
    
    for exam_name, q_count in exams:        
        date_str = last_updates.get(exam_name)

        # Format the title with the date if available
        if date_str:
                label = f"📄 {exam_name} ({q_count} Questions) :gray[(Last Update: {date_str})]"
        else:
            label = f"📄 {exam_name} ({q_count} Questions)"

        with st.expander(label, expanded=False):
            default_value = min(10, q_count)

            num_qs = st.slider("Number of questions", 
                               min_value=1, 
                               max_value=q_count, 
                               value=default_value, 
                               key=f"slider_{exam_name}")
            
            if st.button("Start Practice Test", key=f"start_{exam_name}", type="primary", use_container_width=True):
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
            
            if st.button("Browse questions individually", key=f"browse_{exam_name}", use_container_width=True):
                st.session_state.selected_exam = exam_name
                st.session_state.quiz_data = load_questions(exam_name)
                st.session_state.mode = "browse"
                st.session_state.current_q_idx = 0
                st.session_state.selected_answers = {}
                st.session_state.checked_questions = set()
                st.session_state.current_view = "quiz"
                st.rerun()

# -------------------------------------------------------------
# View 2: Quiz Presentation with Sidebar Navigation
# -------------------------------------------------------------
elif st.session_state.current_view == "quiz":
    questions = st.session_state.quiz_data
    total_qs = len(questions)

    if st.session_state.current_q_idx >= total_qs:
        st.session_state.current_q_idx = 0

    current_idx = st.session_state.current_q_idx
    
    items_per_page = 20
    total_pages = math.ceil(total_qs / items_per_page)
    curr_page = st.session_state.panel_page
    
    start_item_idx = (curr_page - 1) * items_per_page
    end_item_idx = min(start_item_idx + items_per_page, total_qs)
    
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
                        if q_item["is_drag_drop"]:
                            ans_val = st.session_state.selected_answers.get(item_idx, {})
                            is_answered = len(ans_val) > 0 and all(v != "" for v in ans_val.values())
                            is_wrong = item_idx in st.session_state.checked_questions and ans_val != q_item["correct"]
                            is_correct = item_idx in st.session_state.checked_questions and ans_val == q_item["correct"]
                        else:
                            is_answered = len(st.session_state.selected_answers.get(item_idx, [])) > 0
                            is_wrong = item_idx in st.session_state.checked_questions and \
                                    sorted(st.session_state.selected_answers.get(item_idx, [])) != sorted(q_item["correct"])
                            is_correct = item_idx in st.session_state.checked_questions and \
                                        sorted(st.session_state.selected_answers.get(item_idx, [])) == sorted(q_item["correct"])

                        btn_type = "primary" if item_idx == current_idx else "secondary"
                        
                        label = f"{item_idx + 1}"
                        if is_wrong: label = f"✕ {item_idx + 1}"
                        elif is_correct: label = f"✓ {item_idx + 1}"
                        elif is_answered: label = f"● {item_idx + 1}"

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
                            st.image(img_path, caption=alt_text, width=300)
                        else:
                            st.warning(f"Image not found: {img_file}")
                    else:
                        st.markdown(token, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: center;">
            <h1 style="margin: 0; padding: 0; line-height: 1.5;">🎓 Examinator</h1>
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
                                    badge_html = f'<span class="code-blank-wrong">[{safe_val}]</span> <span style="color: green; font-weight: bold;">[{safe_correct}]</span>'
                                
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
    
    # --- Bottom Layout Action Buttons Row ---
    st.markdown('<div class="quiz-action-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if current_idx > 0:
            if st.button("⬅️ Previous Question", key=f"prev_{current_idx}", disabled=(current_idx == 0), use_container_width=True):
                st.session_state.current_q_idx -= 1
                if st.session_state.current_q_idx < (st.session_state.panel_page - 1) * items_per_page:
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
            
            if st.button("Check Answer", 
                         key=f"chk_btn_{current_idx}", 
                         disabled=is_checked or not can_check, 
                         use_container_width=True):
                st.session_state.checked_questions.add(current_idx)
                st.rerun()
        else:
            st.empty()

    with col3:
        if current_idx + 1 < total_qs:
            if st.button("Next Question ➡️", key=f"next_{current_idx}", use_container_width=True):
                st.session_state.current_q_idx += 1
                if st.session_state.current_q_idx >= (st.session_state.panel_page * items_per_page):
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