"""Utility functions for loading and managing question data."""

import os
import re
import random
from pathlib import Path
import frontmatter
import streamlit as st
from config import QUESTIONS_DIR, LAST_UPDATES_FILE
from parsers import detect_code_language


@st.cache_data
def load_last_updates(filepath: str = None) -> dict[str, str]:
    """Reads last_update.md and returns a dict: {'DP-800': '18.07.2026', ...}"""
    if filepath is None:
        filepath = str(LAST_UPDATES_FILE)
    
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


@st.cache_data
def get_available_exams() -> list[tuple[str, int]]:
    """Returns list of (exam_name, question_count) tuples."""
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


def load_questions(exam_folder: str) -> list[dict]:
    """Loads all questions from an exam folder."""
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
            
            correct_mapping = post.get("correct_mapping", {})
            raw_template = post.content.strip()
            
            # 1. Read explicit language setting from frontmatter
            explicit_lang = str(post.get("code_lang", post.get("language", ""))).strip().upper()
            
            # 2. Check for fence blocks
            fence_match = re.match(r'^```([a-zA-Z0-9_+-]*)\s*\n(.*?)\n```$', raw_template, re.DOTALL)
            
            # Handle explicit frontmatter setting
            if explicit_lang:
                if explicit_lang in ["TEXT"]:
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
            correct_mapping = [i for i, item in enumerate(raw_choices) if item["is_correct"]]
            
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
            "correct": correct_mapping,
            "code_template": code_template,
            "is_code": is_code,
            "code_lang": code_lang,
            "ans_image": ans_img
        })
        
    return questions
