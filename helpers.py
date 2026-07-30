"""Helper functions for UI rendering and answer processing."""

import streamlit as st
from config import HR_DIVIDER


def render_selectbox(key: str, options: list, selected_val: str, current_idx: int, b_key: str) -> str:
    """
    Renders a selectbox and updates session state.
    
    Args:
        key: Unique key for the selectbox widget
        options: List of dropdown options
        selected_val: Currently selected value
        current_idx: Current question index
        b_key: Blank key identifier
        
    Returns:
        Selected choice value
    """
    choice = st.selectbox(
        f"Select for {b_key}",
        options,
        index=options.index(selected_val) if selected_val in options else 0,
        key=key,
        label_visibility="collapsed"
    )
    st.session_state.selected_answers[current_idx][b_key] = choice
    return choice


def check_answer_status(item_idx: int, q_item: dict) -> tuple[bool, bool, bool]:
    """
    Check if an answer is answered, wrong, or correct.
    
    Args:
        item_idx: Question index
        q_item: Question dictionary
        
    Returns:
        Tuple of (is_answered, is_wrong, is_correct)
    """
    is_drag_drop = q_item.get("is_drag_drop", False)
    
    if is_drag_drop:
        ans_val = st.session_state.selected_answers.get(item_idx, {})
        is_answered = len(ans_val) > 0 and all(v != "" for v in ans_val.values())
        is_wrong = item_idx in st.session_state.checked_questions and ans_val != q_item["correct"]
        is_correct = item_idx in st.session_state.checked_questions and ans_val == q_item["correct"]
    else:
        ans_val = st.session_state.selected_answers.get(item_idx, [])
        is_answered = len(ans_val) > 0
        ans_sorted = sorted(ans_val)
        correct_sorted = sorted(q_item["correct"])
        is_wrong = item_idx in st.session_state.checked_questions and ans_sorted != correct_sorted
        is_correct = item_idx in st.session_state.checked_questions and ans_sorted == correct_sorted
    
    return is_answered, is_wrong, is_correct


def render_divider():
    """Render a horizontal divider."""
    st.markdown(HR_DIVIDER, unsafe_allow_html=True)
