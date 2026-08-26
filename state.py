"""Session state management for Examinator."""

import json

import streamlit as st
from streamlit_js_eval import streamlit_js_eval


def initialize_session_state():
    """Initialize all session state variables."""
    if "favorite_storage_version" not in st.session_state:
        st.session_state.favorite_storage_version = 0

    stored_value = streamlit_js_eval(
        js_expressions="localStorage.getItem('examinator_favorites') || '[]'",
        key=f"favorite_storage_load_{st.session_state.favorite_storage_version}",
        default=None,
    )
    if stored_value is None:
        st.stop()

    try:
        stored_favorites = json.loads(stored_value)
    except (TypeError, json.JSONDecodeError):
        stored_favorites = []
    st.session_state.favorite_exams = set(stored_favorites)

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


def toggle_favorite(exam_name: str):
    """Toggle an exam favorite and persist it in a browser cookie."""
    favorites = st.session_state.favorite_exams
    if exam_name in favorites:
        favorites.remove(exam_name)
    else:
        favorites.add(exam_name)

    stored_value = json.dumps(sorted(favorites))
    st.session_state.favorite_storage_version += 1
    streamlit_js_eval(
        js_expressions=f"(localStorage.setItem('examinator_favorites', {json.dumps(stored_value)}), 'saved')",
        key=f"favorite_storage_save_{st.session_state.favorite_storage_version}",
        default=None,
    )
