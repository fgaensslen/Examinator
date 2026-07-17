import os
import random
import re
import math
import streamlit as st
import frontmatter

QUESTIONS_DIR = "./questions"

# Page config
st.set_page_config(page_title="Certificator", page_icon="🎓", layout="centered")

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
    
    [data-testid="stSidebar"] {
        background-color: #f7f7f7 !important;
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
    
    /* MAKES ALL BUTTONS IN THE SIDEBAR SMALLER */
    div[data-testid="stSidebar"] button p {
        font-size: 12px !important;
    }
    div[data-testid="stSidebar"] button {
        padding: 2px 4px !important;
        min-height: 28px !important;
        height: 28px !important;
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
    
    .app-header {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }

    /* TARGET EVERY SINGLE ELEMENT RENDERED INSIDE MAIN BUTTONS */
    [data-testid="stMainBlockContainer"] div[data-testid="stButton"] button {
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important; 
        text-align: left !important;
        width: 100% !important;
        padding: 16px 20px !important;
        border-radius: 16px !important;
        min-height: 60px !important;
        height: auto !important;
        margin-bottom: 10px !important;
    }

    /* FIXES THE HIDDEN INNER LAYOUT WRAPPER */
    [data-testid="stMainBlockContainer"] div[data-testid="stButton"] button > div {
        display: flex !important;
        justify-content: flex-start !important;
        text-align: left !important;
        width: 100% !important;
    }

    [data-testid="stMainBlockContainer"] div[data-testid="stButton"] button p {
        text-align: left !important;  
        width: 100% !important;
        margin: 0 !important;
        font-size: 16px !important;
    }

    /* FEEDBACK CARD CONTAINERS MATCHING THE SCREENSHOT - NO BUBBLES, TEXT LEFT ALIGNED */
    .feedback-card {
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important; 
        text-align: left !important;
        width: 100% !important;
        padding: 16px 20px !important;
        border-radius: 16px !important;
        min-height: 60px !important;
        height: auto !important;
        margin-bottom: 10px !important;
    }
    .card-correct {
        border: 3px solid #10b981 !important;
        background-color: #ecfdf5 !important;
    }
    .card-wrong {
        border: 3px solid #ef4444 !important;
        background-color: #fef2f2 !important;
    }
    .card-neutral {
        border: 1px solid #e2e8f0 !important;
        background-color: #ffffff !important;
        color: #64748b;
    }
    
    /* BADGES FOR SELECTED REVIEW STATE */
    .badge-wrong {
        background-color: #fee2e2;
        color: #ef4444;
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
        background-color: #d1fae5;
        color: #10b981;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        white-space: nowrap;
        margin-left: 15px;
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
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Helper Functions
# -------------------------------------------------------------
def get_available_exams():
    if not os.path.exists(QUESTIONS_DIR):
        return []
    exams = []
    for item in os.listdir(QUESTIONS_DIR):
        if os.path.isdir(os.path.join(QUESTIONS_DIR, item)) and not item.startswith(".") and not item.startswith("__"):
            md_files = [f for f in os.listdir(os.path.join(QUESTIONS_DIR, item)) if f.endswith(".md")]
            if md_files:
                exams.append((item, len(md_files)))
    return sorted(exams)

def load_questions(exam_folder):
    questions = []
    folder_path = os.path.join(QUESTIONS_DIR, exam_folder)
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
    
    for file in files:
        filepath = os.path.join(folder_path, file)
        post = frontmatter.load(filepath)
        
        # Extract image from Markdown text (e.g., ![text](image.png))
        md_image_match = re.search(r'!\[.*?\]\((.*?)\)', post.content)
        inline_img = None
        if md_image_match:
            # Join the folder path with the filename found in the markdown
            inline_img = os.path.join(folder_path, md_image_match.group(1))
        
        # Determine optional image paths
        base_name = os.path.splitext(file)[0]
        q_img = os.path.join(folder_path, f"{base_name}.png")
        ans_img = os.path.join(folder_path, f"{base_name}_answer.png")
        
        # ... inside the loop where you process choices ...
        raw_choices = [] # Store pairs of (choice_text, is_correct)
        lines = post.content.strip().split("\n")
        
        for line in lines:
            match = re.match(r'^\s*-\s*\[([ xX])\]\s*(.*)$', line)
            if match:
                is_correct = match.group(1).lower() == 'x'
                raw_choices.append({"text": match.group(2).strip(), "is_correct": is_correct})
        
        # Shuffle the choices
        random.shuffle(raw_choices)
        
        # Extract the shuffled text and the new correct indices
        choices = [item["text"] for item in raw_choices]
        correct_indices = [i for i, item in enumerate(raw_choices) if item["is_correct"]]
                
        questions.append({
            "filename": file,
            "question": post.get("question", "Missing Question Text"),
            "documentation": post.get("documentation", ""),
            "choices": choices,
            "correct": correct_indices,
            "q_image": q_img if os.path.exists(q_img) else None,
            "ans_image": ans_img if os.path.exists(ans_img) else None
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

# -------------------------------------------------------------
# View 1: Main Dashboard
# -------------------------------------------------------------
if st.session_state.current_view == "dashboard":
    st.markdown('<div class="app-header"><h1>🎓 Examinator</h1></div>', unsafe_allow_html=True)
    exams = get_available_exams()
    if not exams:
        st.warning("No question folders found.")
    
    st.markdown('<div class="dashboard-btn-container">', unsafe_allow_html=True)
    for exam_name, q_count in exams:
        if st.button(f"📄 {exam_name} ({q_count} Questions)"):
            st.session_state.selected_exam = exam_name
            st.session_state.quiz_data = load_questions(exam_name)
            st.session_state.selected_answers = {}
            st.session_state.checked_questions = set()
            st.session_state.current_view = "exam_menu"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# View 2: Mode Selector Page
# -------------------------------------------------------------
elif st.session_state.current_view == "exam_menu":
    st.markdown(f'<div class="app-header"><h1>🎓 Examinator</h1></div>', unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'><b>{st.session_state.selected_exam}</b></h3>", unsafe_allow_html=True)
    
    st.markdown('<div class="dashboard-btn-container">', unsafe_allow_html=True)
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.current_view = "dashboard"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
        
    max_questions = len(st.session_state.quiz_data)
    selected_range = st.slider("Select range of questions:", min_value=1, max_value=max_questions, value=(1, max_questions))
    
    start_idx, end_idx = selected_range
    st.write("---")
    
    st.markdown('<div class="dashboard-btn-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📚 Browse In Order"):
            st.session_state.mode = "browse"
            st.session_state.quiz_data = st.session_state.quiz_data[start_idx - 1 : end_idx]
            st.session_state.current_q_idx = 0
            st.session_state.panel_page = 1
            st.session_state.selected_answers = {}
            st.session_state.checked_questions = set()
            st.session_state.current_view = "quiz"
            st.rerun()
    with col2:
        if st.button("⏱️ Random Practice"):
            st.session_state.mode = "exam"
            sliced_subset = st.session_state.quiz_data[start_idx - 1 : end_idx]
            random.shuffle(sliced_subset)
            st.session_state.quiz_data = sliced_subset
            st.session_state.current_q_idx = 0
            st.session_state.panel_page = 1
            st.session_state.selected_answers = {}
            st.session_state.checked_questions = set()
            st.session_state.current_view = "quiz"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# View 3: Quiz Presentation with Sidebar Navigation
# -------------------------------------------------------------
elif st.session_state.current_view == "quiz":
    questions = st.session_state.quiz_data
    total_qs = len(questions)
    current_idx = st.session_state.current_q_idx
    
    items_per_page = 20
    total_pages = math.ceil(total_qs / items_per_page)
    curr_page = st.session_state.panel_page
    
    start_item_idx = (curr_page - 1) * items_per_page
    end_item_idx = min(start_item_idx + items_per_page, total_qs)
    
    if current_idx not in st.session_state.selected_answers:
        st.session_state.selected_answers[current_idx] = []
        
    # --- SIDEBAR NAV PANEL ---
    with st.sidebar:
        side_head_col1, side_head_col2 = st.columns([2, 1])
        with side_head_col1:
            st.write(f"### {total_qs} questions")
        with side_head_col2:
            if st.button("🚪 Exit", key="side_exit_btn", type="secondary"):
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
                        btn_type = "primary" if item_idx == current_idx else "secondary"
                        if st.button(f"{item_idx + 1}", key=f"nav_grid_{item_idx}", type=btn_type, use_container_width=True):
                            st.session_state.current_q_idx = item_idx
                            st.rerun()
        
        st.write("---")
        
        # --- SMART GHCERTIFIED PAGINATION ROW STYLE ---
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
    st.markdown(f'<div class="app-header"><h1>🎓 Examinator</h1></div>', unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center; color: gray;'><b>{st.session_state.selected_exam}</b> - {'Study Mode' if st.session_state.mode == 'browse' else 'Practice Exam'}</h4>", unsafe_allow_html=True)
    st.write("---")
    
    q = questions[current_idx]
    st.markdown(f"### Question {current_idx + 1} of {total_qs}")
    # Using st.markdown allows for <br> tags or double-space line breaks
    # Wrap the markdown rendering in a div that uses your custom CSS
    st.markdown(q["question"].replace('\n', '<br>'), unsafe_allow_html=True)    
    
    # Render Question Image ONLY if it exists in directory
    if q["q_image"]:
        st.image(q["q_image"], use_container_width=True)
        st.write("")  # Little space buffer
    
    is_checked = current_idx in st.session_state.checked_questions
    current_selections = st.session_state.selected_answers[current_idx]
    
    # Render Answers List
    for c_idx, choice in enumerate(q["choices"]):
        is_selected = c_idx in current_selections
        is_correct_choice = c_idx in q["correct"]
        
        if not is_checked:
            # Native Streamlit button types: 'primary' applies a filled highlight color
            btn_type = "primary" if is_selected else "secondary"
            
            if st.button(choice, key=f"btn_choice_{current_idx}_{c_idx}", use_container_width=True, type=btn_type):
                if c_idx in current_selections:
                    st.session_state.selected_answers[current_idx].remove(c_idx)
                else:
                    if len(q["correct"]) == 1:
                        st.session_state.selected_answers[current_idx] = [c_idx]
                    else:
                        st.session_state.selected_answers[current_idx].append(c_idx)
                st.rerun()
        else:
            # Locked Review mode with clear indication of what you selected
            if is_correct_choice:
                badge_html = '<span class="badge-correct">Your Answer</span>' if is_selected else ''
                st.markdown(
                    f'<div class="feedback-card card-correct">'
                    f'<span>{choice}</span>'
                    f'{badge_html}'
                    f'</div>',
                    unsafe_allow_html=True
                )
            elif is_selected and not is_correct_choice:
                st.markdown(
                    f'<div class="feedback-card card-wrong">'
                    f'<span>{choice}</span>'
                    f'<span class="badge-wrong">Your Answer</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="feedback-card card-neutral">'
                    f'<span>{choice}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )

    # Render Answer/Explanation Image ONLY if checked and exists in directory
    if is_checked and q["ans_image"]:
        st.write("---")
        st.image(q["ans_image"], use_container_width=True)

    if is_checked:
        is_perfect = sorted(current_selections) == sorted(q["correct"])

    st.write("")
    
    # Bottom Layout Action Buttons Row
    st.markdown('<div class="quiz-action-container">', unsafe_allow_html=True)
    c_btn1, c_btn2, c_btn3 = st.columns([1.2, 1, 1.2])
    
    with c_btn1:
        if st.button("⬅️ Previous Question", key=f"prev_{current_idx}", disabled=(current_idx == 0)):
            st.session_state.current_q_idx -= 1
            if st.session_state.current_q_idx < (st.session_state.panel_page - 1) * items_per_page:
                st.session_state.panel_page -= 1
            st.rerun()
            
    with c_btn2:
        # The button is now ONLY disabled if the question is already checked
        if st.button("Check Answer", key=f"chk_{current_idx}", disabled=is_checked):
            st.session_state.checked_questions.add(current_idx)
            st.rerun()
                
    with c_btn3:
        if st.button("Next Question ➡️", key=f"next_{current_idx}", disabled=(current_idx + 1 >= total_qs)):
            st.session_state.current_q_idx += 1
            if st.session_state.current_q_idx >= (st.session_state.panel_page * items_per_page):
                st.session_state.panel_page += 1
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)