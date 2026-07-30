"""Parsing functions for questions and case studies."""

import os
import re
import yaml


def detect_code_language(template_text: str) -> str:
    """Detect code language from template text."""
    text = template_text.strip()
    
    if (text.startswith("{") or text.startswith("[")) and ":" in text:
        return "JSON"
        
    sql_pattern = r'\b(SELECT|FROM|WHERE|INSERT|UPDATE|DELETE|JOIN|ALTER|CREATE|ORDER\s+BY|GROUP\s+BY)\b'
    if re.search(sql_pattern, text, re.IGNORECASE):
        return "SQL"
        
    return "TEXT"


def parse_case_study(file_path: str) -> tuple[dict | None, dict]:
    """
    Parses a case study markdown file containing YAML frontmatter and section headings.
    
    Returns:
        Tuple of (sections_dict, metadata_dict)
    """
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
                print(f"YAML Error in {file_path}: {e}")
            content = parts[2]
            
    pattern = r"^#\s+(.+?)\n(.*?)(?=\n^#\s+|\Z)"
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
    
    sections = {heading.strip(): body.strip() for heading, body in matches}
    return sections, metadata
