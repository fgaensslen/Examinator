"""CSS styles for Examinator."""

CUSTOM_CSS = """
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
"""

def apply_styles():
    """Apply custom CSS styles to the Streamlit app."""
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
