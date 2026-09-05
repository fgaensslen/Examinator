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

/* Keep pagination controls independent of Streamlit's Markdown wrapper DOM. */
html body div[class*="st-key-nav_prev_page"] button,
html body div[class*="st-key-nav_next_page"] button,
html body div[class*="st-key-nav_page_"] button {
    width: 32px !important;
    height: 32px !important;
    min-width: 32px !important;
    max-width: 32px !important;
    min-height: 32px !important;
    max-height: 32px !important;
    padding: 0px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border-radius: 6px !important;
}
html body div[class*="st-key-nav_prev_page"] button > div,
html body div[class*="st-key-nav_next_page"] button > div,
html body div[class*="st-key-nav_page_"] button > div,
html body div[class*="st-key-nav_prev_page"] button p,
html body div[class*="st-key-nav_next_page"] button p,
html body div[class*="st-key-nav_page_"] button p {
    justify-content: center !important;
    text-align: center !important;
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

/* Keep drag-and-drop blank rows at a consistent gap whether the row shows a
   selectbox (unanswered) or a result badge (answered/checked), so spacing
   doesn't shift once a question is checked. */
[class*="st-key-drag_drop_block_"],
[class*="st-key-text_drag_drop_block_"] {
    row-gap: 0.8rem !important;
}
[class*="st-key-drag_drop_block_"] [data-testid="stMarkdownContainer"] p,
[class*="st-key-text_drag_drop_block_"] [data-testid="stMarkdownContainer"] p {
    margin-bottom: 0 !important;
}
/* Pull the result-badge row up the same amount the selectbox is pulled up,
   so the gap under a question line stays identical before/after checking. */
[class*="st-key-drag_drop_block_"] [data-testid="stElementContainer"]:has(.code-blank-correct),
[class*="st-key-drag_drop_block_"] [data-testid="stElementContainer"]:has(.code-blank-wrong),
[class*="st-key-drag_drop_block_"] [data-testid="stElementContainer"]:has(.text-blank-correct),
[class*="st-key-drag_drop_block_"] [data-testid="stElementContainer"]:has(.text-blank-wrong),
[class*="st-key-text_drag_drop_block_"] [data-testid="stElementContainer"]:has(.text-blank-correct),
[class*="st-key-text_drag_drop_block_"] [data-testid="stElementContainer"]:has(.text-blank-wrong) {
    margin-top: -10px !important;
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
.code-blank-correct,
.text-blank-correct {
    border: 2px solid #10b981 !important;
    background-color: #ecfdf5 !important;
    color: #065f46 !important;
    padding: 4px 10px !important;
    border-radius: 6px !important;
    font-weight: 400 !important;
    display: inline-block !important;
    margin: 2px 0 !important;
}
.code-blank-wrong,
.text-blank-wrong {
    border: 2px solid #ef4444 !important;
    background-color: #fef2f2 !important;
    color: #991b1b !important;
    padding: 4px 10px !important;
    border-radius: 6px !important;
    font-weight: 400 !important;
    display: inline-block !important;
    margin: 2px 0 !important;
}

.code-blank-wrong {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace !important;
    transform: translateY(-6px) !important;
}
.code-answer-correct {
    display: inline-block !important;
    transform: translateY(-5px) !important;
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
    white-space: pre-wrap !important;
    overflow-wrap: break-word !important;
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

.code-line-row [data-testid="stHorizontalBlock"],
[class*="st-key-drag_drop_block_"] [data-testid="stHorizontalBlock"] {
    display: inline-flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 6px !important;
    width: auto !important;
    margin: 0 !important;
}

.code-line-row [data-testid="column"],
.code-line-row [data-testid="stColumn"],
[class*="st-key-drag_drop_block_"] [data-testid="column"],
[class*="st-key-drag_drop_block_"] [data-testid="stColumn"] {
    width: auto !important;
    flex: 0 0 auto !important;
    min-width: unset !important;
    padding: 0 !important;
}

/* CONTROL DROPDOWN WIDTH */
.code-line-row [data-testid="stSelectbox"],
[class*="st-key-drag_drop_block_"] [data-testid="stSelectbox"] {
    width: 300px !important;
    min-width: 220px !important;
    margin: 0 !important;
    transform: translateY(-5px) !important;
}

.code-line-row [data-testid="stSelectbox"] > div,
[class*="st-key-drag_drop_block_"] [data-testid="stSelectbox"] > div {
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

/* ------------------------------------------------------------- */
/* DASHBOARD POSTER-STYLE LAYOUT                                */
/* ------------------------------------------------------------- */

.poster-hero {
    border: 1px solid #d7d1c6;
    background: linear-gradient(125deg, #f7f3ea 0%, #f2ece1 45%, #efe7d9 100%);
    border-radius: 14px;
    padding: 16px 18px;
    margin-bottom: 14px;
}

/* Keep the favorite control visually inside the exam header. */
div[class*="st-key-favorite-storage"] {
    display: none !important;
}
div[class*="st-key-exam-header-"] {
    background: linear-gradient(90deg, #1e40af 0%, #2563eb 60%, #3b82f6 100%);
    border: 1px solid #1d4ed8;
    border-radius: 8px;
    padding: 9px 11px 3px !important;
    margin-bottom: 4px;
    overflow: visible !important;
}
div[class*="st-key-exam-header-"] [data-testid="stHorizontalBlock"] {
    width: 100% !important;
    align-items: center !important;
    gap: 8px !important;
}
div[class*="st-key-exam-header-"] [data-testid="column"]:first-child {
    flex: 1 1 auto !important;
    min-width: 0 !important;
}
div[class*="st-key-exam-header-"] [data-testid="column"]:nth-child(2) {
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: max-content !important;
}
div[class*="st-key-exam-header-"] [data-testid="column"]:last-child {
    flex: 0 0 180px !important;
    width: 180px !important;
    min-width: 180px !important;
}
div[class*="st-key-exam-header-"] [data-testid="column"] > div {
    width: 100% !important;
}
div[class*="st-key-exam-header-"] .exam-tile-code-chip {
    background: transparent !important;
    border: 0 !important;
    border-radius: 0 !important;
    padding: 0 !important;
}
div[class*="st-key-exam-header-"] .exam-tile-count {
    display: block !important;
    padding: 0 !important;
    background: transparent !important;
    border-radius: 0 !important;
    text-align: right !important;
}
div[class*="st-key-exam-header-"] [data-testid="stButton"] button {
    background: transparent !important;
    border: 0 !important;
    color: #ffffff !important;
    font-size: 24px !important;
    width: 100% !important;
    min-width: 0 !important;
    min-height: 32px !important;
    height: 32px !important;
    padding: 0 !important;
    margin: 0 !important;
    justify-content: flex-end !important;
    transform: translateY(8px);
}
div[class*="st-key-exam-header-"] [data-testid="stButton"] button > div,
div[class*="st-key-exam-header-"] [data-testid="stButton"] button p {
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
    text-align: right !important;
    white-space: nowrap !important;
}
body [data-testid="stMainBlockContainer"] div[class*="st-key-exam-header-"] [data-testid="stButton"] button {
    width: 100% !important;
    min-width: 0 !important;
    min-height: 32px !important;
    height: 32px !important;
    padding: 0 !important;
    margin: 0 !important;
    justify-content: flex-end !important;
    transform: translateY(8px) !important;
    position: relative !important;
    left: 20px !important;
}
body [data-testid="stMainBlockContainer"] div[class*="st-key-exam-header-"] [data-testid="stButton"] button > div,
body [data-testid="stMainBlockContainer"] div[class*="st-key-exam-header-"] [data-testid="stButton"] button p {
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
    text-align: right !important;
    white-space: nowrap !important;
}
body [data-testid="stMainBlockContainer"] div[class*="st-key-exam-header-"] [data-testid="stButton"] button:hover p {
    font-size: 0 !important;
}
body [data-testid="stMainBlockContainer"] div[class*="st-key-exam-header-"] [data-testid="stButton"] button:hover p::after {
    content: "★";
    color: #ffffff !important;
    font-size: 15px !important;
}
/* Keep the exam header rows side-by-side on narrow/mobile viewports. */
div[class*="st-key-exam-header-"] [data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
    flex-direction: row !important;
}
div[class*="st-key-exam-header-"] [data-testid="column"],
div[class*="st-key-exam-header-"] [data-testid="stColumn"] {
    min-width: 0 !important;
    flex-basis: auto !important;
}
div[class*="st-key-exam-header-"] [data-testid="stHorizontalBlock"] > [data-testid="column"]:first-child,
div[class*="st-key-exam-header-"] [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child {
    flex: 1 1 auto !important;
    width: auto !important;
    min-width: 0 !important;
}
div[class*="st-key-exam-header-"] [data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child,
div[class*="st-key-exam-header-"] [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:last-child {
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: max-content !important;
}
html body [data-testid="stMainBlockContainer"] div[class*="st-key-exam-header-"] [data-testid="stButton"] button {
    left: 0 !important;
    width: auto !important;
}
.poster-hero .poster-brand {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #7a7468;
    margin-bottom: 4px;
    font-weight: 700;
}

.poster-hero h1 {
    margin: 0;
    color: #dd4b25;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: 0.2px;
    line-height: 1;
}

.poster-hero p {
    margin: 8px 0 0 0;
    color: #333;
    font-size: 14px;
    line-height: 1.35;
}

.poster-board {
    border: 1px solid #ddd6c8;
    border-radius: 16px;
    padding: 12px;
    background: #f6f3ee;
    max-height: 73vh;
    overflow-y: auto;
}

.poster-column-title-wrap {
    background: #e2ded5;
    border: 1px solid #d0c9bb;
    border-radius: 8px;
    margin-bottom: 10px;
    padding: 7px 9px;
}

.poster-column-title {
    margin: 0;
    font-size: 13px;
    font-weight: 800;
    color: #2f2f2f;
    text-transform: uppercase;
    letter-spacing: 0.55px;
    line-height: 1.2;
}

.poster-tile {
    border: 1px solid #cfcdc6;
    border-left: 5px solid #111;
    border-radius: 8px;
    padding: 9px 10px;
    background: #fff;
    margin-bottom: 6px;
}

.poster-tile-code {
    margin: 0;
    color: #111;
    font-size: 17px;
    font-weight: 800;
    line-height: 1.1;
}

.poster-tile-sub {
    margin-top: 3px;
    color: #373737;
    font-size: 12px;
    font-weight: 600;
    line-height: 1.2;
}

.poster-tile-meta {
    margin-top: 6px;
    color: #6b6b6b;
    font-size: 11px;
    line-height: 1.25;
}

.poster-tile.track-fundamentals {
    border-left-color: #111;
}

.poster-tile.track-role {
    border-left-color: #2f80ed;
}

.poster-tile.track-specialty {
    border-left-color: #7f56d9;
}

@media (max-width: 1024px) {
    .poster-board {
        max-height: none;
        overflow: visible;
    }

    .poster-hero h1 {
        font-size: 30px;
    }
}

/* ------------------------------------------------------------- */
/* EXAM TILE DASHBOARD                                           */
/* ------------------------------------------------------------- */

.exam-board {
    margin-top: 8px;
}

.exam-column-title-wrap {
    background: transparent;
    border: 0;
    border-radius: 0;
    padding: 8px 10px;
    margin-bottom: 10px;
}

.exam-column-title {
    font-size: 13px;
    color: inherit;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.exam-column-title-wrap.cloud-ai-platforms .exam-column-title,
.exam-column-title-wrap.github .exam-column-title {
    font-size: 18px;
    font-weight: 900;
}

.exam-tile {
    border-left: 5px solid #6b7280;
    padding-left: 0;
    margin-bottom: 4px;
}

.exam-tile-code-chip {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%);
    border-radius: 8px;
    padding: 7px 10px;
}

.exam-tile-code {
    font-size: 19px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
}

.exam-tile-count {
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.18);
    color: #ffffff;
    font-weight: 700;
    letter-spacing: 0.25px;
    white-space: nowrap;
}

.exam-tile-sub {
    margin-top: 5px;
    font-size: 12px;
    color: #374151;
    font-weight: 600;
}

.exam-tile-meta {
    margin-top: 2px;
    font-size: 11px;
    color: #6b7280;
}

.exam-tile.track-fundamentals {
    border-left-color: #111827;
}

.exam-tile.track-role {
    border-left-color: #2563eb;
}

.exam-tile.track-specialty {
    border-left-color: #7c3aed;
}
</style>
"""

def apply_styles():
    """Apply custom CSS styles to the Streamlit app."""
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
