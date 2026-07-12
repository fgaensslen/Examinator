import os
import random
import re
import streamlit as st
import frontmatter

QUESTIONS_DIR = "./questions"

# Page config - Changes the browser tab title and icon
st.set_page_config(page_title="Certificator", page_icon="🎓", layout="centered")

# Custom CSS targeting button selectors directly to enforce a strict fixed layout width and larger font
st.markdown("""
    <style>
    /* Force absolute uniform static width on ALL button tags across the app */
    button[data-testid="stBaseButton-element"],
    .stButton > button {
        width: 320px !important;      /* Explicit fixed width */
        min-width: 320px !important;  /* Prevents columns from shrinking it */
        max-width: 320px !important;  /* Prevents rows from stretching it */
        margin-left: auto !important;
        margin-right: auto !important; /* Centers the buttons on the screen */
        display: block !important;
        
        /* INCREASED FONT SIZE & COMFORTABLE PADDING */
        padding: 18px 24px !important;
        font-size: 22px !important;    
        font-weight: bold !important;
        
        margin-bottom: 12px !important;
        border-radius: 8px !important;
    }
    
    /* Ensures multi-line text blocks (like the practice modes) render cleanly at the new font size */
    button[data-testid="stBaseButton-element"] p,
    .stButton > button p {
        font-size: 22px !important;
        line-height: 1.3 !important;
    }
    
    .app-header {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Helper Functions
# -------------------------------------------------------------
def get_available_exams():
    """Scans ./questions folder for exam subfolders."""
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
    """Loads and parses all markdown quiz questions in a folder."""
    questions = []
    folder_path = os.path.join(QUESTIONS_DIR, exam_folder)
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
    
    for file in files:
        filepath = os.path.join(folder_path, file)
        post = frontmatter.load(filepath)
        
        choices = []
        correct_indices = []
        
        lines = post.content.strip().split("\n")
        idx = 0
        for line in lines:
            match = re.match(r'^\s*-\s*\[([ xX])\]\s*(.*)$', line)
            if match:
                is_correct = match.group(1).lower() == 'x'
                choice_text = match.group(2).strip()
                choices.append(choice_text)
                if is_correct:
                    correct_indices.append(idx)
                idx += 1
                
        questions.append({
            "filename": file,
            "question": post.get("question", "Missing Question Text"),
            "documentation": post.get("documentation", ""),
            "choices": choices,
            "correct": correct_indices
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

# -------------------------------------------------------------
# View 1: Main Dashboard (Examinator Hub)
# -------------------------------------------------------------
if st.session_state.current_view == "dashboard":
    st.markdown('<div class="app-header"><h1>🎓 Examinator</h1></div>', unsafe_allow_html=True)
    
    exams = get_available_exams()
    if not exams:
        st.warning("No question folders found. Please place your exam markdown folders in this directory.")
    
    for exam_name, q_count in exams:
        button_label = f"📄 {exam_name} ({q_count} Questions)"
        
        if st.button(button_label):
            st.session_state.selected_exam = exam_name
            st.session_state.quiz_data = load_questions(exam_name)
            st.session_state.current_view = "exam_menu"
            st.rerun()

# -------------------------------------------------------------
# View 2: Mode Selector Page (With Range Slicer)
# -------------------------------------------------------------
elif st.session_state.current_view == "exam_menu":
    st.markdown(f'<div class="app-header"><h1>🎓 Examinator</h1></div>', unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'><b>{st.session_state.selected_exam}</b></h3>", unsafe_allow_html=True)
    
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.current_view = "dashboard"
        st.rerun()
        
    max_questions = len(st.session_state.quiz_data)
    
    st.subheader("🎯 Filter Practice Material")
    selected_range = st.slider(
        "Select the range of questions you want to practice:",
        min_value=1,
        max_value=max_questions,
        value=(1, max_questions),
        step=1
    )
    
    start_idx, end_idx = selected_range
    total_selected = end_idx - start_idx + 1
    st.info(f"Selected range includes **{total_selected}** questions (From Question {start_idx} to {end_idx}).")
    
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📚 Browse In Order"):
            st.session_state.mode = "browse"
            st.session_state.quiz_data = st.session_state.quiz_data[start_idx - 1 : end_idx]
            st.session_state.current_view = "quiz"
            st.rerun()
            
    with col2:
        if st.button("⏱️ Random Practice"):
            st.session_state.mode = "exam"
            sliced_subset = st.session_state.quiz_data[start_idx - 1 : end_idx]
            random.shuffle(sliced_subset)
            st.session_state.quiz_data = sliced_subset
            st.session_state.current_view = "quiz"
            st.rerun()

# -------------------------------------------------------------
# View 3: Quiz Presentation
# -------------------------------------------------------------
elif st.session_state.current_view == "quiz":
    st.markdown(f'<div class="app-header"><h1>🎓 Examinator</h1></div>', unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'><b>{st.session_state.selected_exam}</b> - {'Study Mode' if st.session_state.mode == 'browse' else 'Practice Exam'}</h3>", unsafe_allow_html=True)
    
    if st.button("🚪 Exit Quiz Mode"):
        st.session_state.current_view = "dashboard"
        st.rerun()
        
    st.write("---")
    
    questions = st.session_state.quiz_data
    
    for i, q in enumerate(questions, 1):
        st.markdown(f"### Question {i}")
        st.info(q["question"])
        
        user_selection = []
        # FIX: Loop with enumerate index (c_idx) to guarantee absolute key uniqueness
        for c_idx, choice in enumerate(q["choices"]):
            unique_key = f"q_{i}_c_{c_idx}"
            user_selection.append(st.checkbox(choice, key=unique_key))
            
        if st.button("Check Answer", key=f"btn_{i}"):
            selected_indices = [idx for idx, checked in enumerate(user_selection) if checked]
            
            if selected_indices == q["correct"]:
                st.success("🎉 Correct!")
            else:
                correct_answers_text = ", ".join([q["choices"][c_idx] for c_idx in q["correct"]])
                st.error(f"❌ Incorrect. Correct answer(s): {correct_answers_text}")
                
            if q["documentation"]:
                st.markdown(f"[Read Microsoft Documentation Blueprint]({q['documentation']})")
                
        st.write("---")