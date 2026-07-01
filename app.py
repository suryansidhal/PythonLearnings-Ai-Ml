#AI IMPROVED UI VERSION OF MY PYTHON FILE HANDLING

import streamlit as st
from pathlib import Path
import os

# Page configuration
st.set_page_config(
    page_title="File Manager",
    page_icon="Suryansi's File Manager",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark cinematic theme
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 50%, #16213e 100%);
        color: #e0e0e0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }
    
    [data-testid="stHeader"] {
        background: transparent;
        padding: 0;
    }
    
    .main {
        padding: 2rem 1rem;
    }
    
    h1 {
        background: linear-gradient(90deg, #a78bfa 0%, #c084fc 30%, #60a5fa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 3rem;
        letter-spacing: 0.5px;
    }
    
    .operation-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-bottom: 3rem;
    }
    
    .stTabs [role="tablist"] {
        background: rgba(255, 255, 255, 0.05);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px 12px 0 0;
        backdrop-filter: blur(10px);
        padding: 0.5rem;
    }
    
    .stTabs [role="tab"] {
        background: transparent;
        color: #94a3b8;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stTabs [role="tab"]:hover {
        background: rgba(255, 255, 255, 0.1);
        color: #e0e0e0;
    }
    
    .stTabs [role="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 100%);
        color: #ffffff;
        border: none;
        box-shadow: 0 4px 15px rgba(167, 139, 250, 0.3);
    }
    
    .form-container {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .stTextInput, .stTextArea {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
        color: #e0e0e0 !important;
    }
    
    .stTextInput:focus, .stTextArea:focus {
        border: 1px solid #a78bfa !important;
        box-shadow: 0 0 0 3px rgba(167, 139, 250, 0.1) !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 100%);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(167, 139, 250, 0.3);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(167, 139, 250, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .success-box {
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        color: #86efac;
        margin-top: 1rem;
    }
    
    .error-box {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        color: #fca5a5;
        margin-top: 1rem;
    }
    
    .info-box {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        color: #93c5fd;
        margin-top: 1rem;
    }
    
    .section-label {
        color: #cbd5e1;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
        margin-top: 1.5rem;
    }
    
    .operation-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 1.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .operation-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(167, 139, 250, 0.5);
        transform: translateY(-4px);
    }
    
    .operation-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .operation-title {
        color: #e0e0e0;
        font-weight: 600;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    
    .operation-desc {
        color: #94a3b8;
        font-size: 0.9rem;
    }
    
    [data-testid="stSelectbox"] {
        background: rgba(255, 255, 255, 0.08) !important;
    }
    
    .stSelectbox [data-testid="baseButton-secondary"] {
        color: #e0e0e0 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 8px !important;
    }

    .expander {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        backdrop-filter: blur(10px);
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    
    .metric-value {
        color: #a78bfa;
        font-size: 2rem;
        font-weight: 700;
    }
    
    .metric-label {
        color: #94a3b8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Remove default Streamlit padding */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# File management functions
def createfile(name, data):
    try:
        path = Path(name)
        if not path.exists():
            with open(path, "w") as f:
                f.write(data)
            return True, f"File '{name}' created successfully!"
        else:
            return False, f"File '{name}' already exists"
    except Exception as e:
        return False, f"Error: {str(e)}"

def readfile(name):
    try:
        path = Path(name)
        if path.exists():
            with open(path, "r") as f:
                data = f.read()
            return True, data
        else:
            return False, "File does not exist"
    except Exception as e:
        return False, f"Error: {str(e)}"

def writefile(name, new_content, choice):
    try:
        path = Path(name)
        if path.exists():
            if choice == "rename":
                new_title = new_content
                new_path = Path(new_title)
                if not new_path.exists():
                    path.rename(new_path)
                    return True, f"File renamed to '{new_title}' successfully"
                else:
                    return False, "File with new name already exists"
            elif choice == "append":
                with open(path, "a") as f:
                    f.write(new_content)
                return True, f"Content appended to '{name}' successfully"
            elif choice == "overwrite":
                with open(path, "w") as f:
                    f.write(new_content)
                return True, f"File '{name}' overwritten successfully"
        else:
            return False, "File does not exist"
    except Exception as e:
        return False, f"Error: {str(e)}"

def deletefile(name):
    try:
        path = Path(name)
        if path.exists():
            path.unlink()
            return True, f"File '{name}' deleted successfully"
        else:
            return False, "File does not exist"
    except Exception as e:
        return False, f"Error: {str(e)}"

# Initialize session state
if "tab_selected" not in st.session_state:
    st.session_state.tab_selected = "Create"
if "result_message" not in st.session_state:
    st.session_state.result_message = None
if "result_success" not in st.session_state:
    st.session_state.result_success = None

# Header
st.markdown("<h1>✨ File Manager</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Elegant file operations with a cinematic touch</p>", unsafe_allow_html=True)

# Main tabs for operations
tab1, tab2, tab3, tab4 = st.tabs(["Create", "Read", "Write", "Delete"])

# ==================== CREATE TAB ====================
with tab1:
    st.markdown("<div class='section-label'>Create a new file</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            create_filename = st.text_input(
                "File name",
                placeholder="example.txt",
                key="create_filename",
                label_visibility="collapsed"
            )
        
        with col2:
            st.write("")  # Spacer
        
        create_content = st.text_area(
            "File content",
            placeholder="Enter the content you want to save...",
            height=200,
            key="create_content",
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns([1, 1, 3])
        
        with col1:
            if st.button("✨ Create File", key="create_btn", use_container_width=True):
                if create_filename.strip():
                    success, message = createfile(create_filename, create_content)
                    st.session_state.result_success = success
                    st.session_state.result_message = message
                else:
                    st.session_state.result_success = False
                    st.session_state.result_message = "Please enter a file name"
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.session_state.result_message:
            if st.session_state.result_success:
                st.markdown(f"<div class='success-box'>✓ {st.session_state.result_message}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='error-box'>✕ {st.session_state.result_message}</div>", unsafe_allow_html=True)

# ==================== READ TAB ====================
with tab2:
    st.markdown("<div class='section-label'>Read file contents</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        
        read_filename = st.text_input(
            "File name to read",
            placeholder="example.txt",
            key="read_filename",
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns([1, 1, 3])
        
        with col1:
            if st.button("📖 Read File", key="read_btn", use_container_width=True):
                if read_filename.strip():
                    success, content = readfile(read_filename)
                    if success:
                        st.session_state.result_success = True
                        st.session_state.result_message = "File read successfully!"
                        st.markdown(f"<div class='info-box'><strong>File Contents:</strong><br><br><code>{content}</code></div>", unsafe_allow_html=True)
                    else:
                        st.session_state.result_success = False
                        st.session_state.result_message = content
                else:
                    st.session_state.result_success = False
                    st.session_state.result_message = "Please enter a file name"
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.session_state.result_message and not (st.session_state.result_success and "File read" in st.session_state.result_message):
            if st.session_state.result_success:
                st.markdown(f"<div class='success-box'>✓ {st.session_state.result_message}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='error-box'>✕ {st.session_state.result_message}</div>", unsafe_allow_html=True)

# ==================== WRITE TAB ====================
with tab3:
    st.markdown("<div class='section-label'>Modify existing files</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        
        write_filename = st.text_input(
            "File name to modify",
            placeholder="example.txt",
            key="write_filename",
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns(3, gap="small")
        
        with col1:
            choice = st.radio(
                "Choose action",
                ["Rename", "Append", "Overwrite"],
                label_visibility="collapsed",
                horizontal=False
            )
        
        write_content = st.text_area(
            "New content or new filename",
            placeholder="Enter new content or filename...",
            height=150,
            key="write_content",
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns([1, 1, 3])
        
        with col1:
            if st.button("✏️ Write File", key="write_btn", use_container_width=True):
                if write_filename.strip() and write_content.strip():
                    choice_map = {"Rename": "rename", "Append": "append", "Overwrite": "overwrite"}
                    success, message = writefile(write_filename, write_content, choice_map[choice])
                    st.session_state.result_success = success
                    st.session_state.result_message = message
                else:
                    st.session_state.result_success = False
                    st.session_state.result_message = "Please enter both filename and content"
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.session_state.result_message:
            if st.session_state.result_success:
                st.markdown(f"<div class='success-box'>✓ {st.session_state.result_message}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='error-box'>✕ {st.session_state.result_message}</div>", unsafe_allow_html=True)

# ==================== DELETE TAB ====================
with tab4:
    st.markdown("<div class='section-label'>Remove files permanently</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        
        delete_filename = st.text_input(
            "File name to delete",
            placeholder="example.txt",
            key="delete_filename",
            label_visibility="collapsed"
        )
        
        st.warning("⚠️ This action cannot be undone. Make sure you want to delete this file.", icon="⚠️")
        
        col1, col2, col3 = st.columns([1, 1, 3])
        
        with col1:
            if st.button("🗑️ Delete File", key="delete_btn", use_container_width=True):
                if delete_filename.strip():
                    success, message = deletefile(delete_filename)
                    st.session_state.result_success = success
                    st.session_state.result_message = message
                else:
                    st.session_state.result_success = False
                    st.session_state.result_message = "Please enter a file name"
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.session_state.result_message:
            if st.session_state.result_success:
                st.markdown(f"<div class='success-box'>✓ {st.session_state.result_message}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='error-box'>✕ {st.session_state.result_message}</div>", unsafe_allow_html=True)

# Footer with divider
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.caption("✨ Built with Streamlit • Elegant file management with cinematic design")