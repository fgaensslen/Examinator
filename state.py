"""Session state management for Examinator."""

import streamlit as st


def initialize_session_state():
    """Initialize all session state variables."""
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
