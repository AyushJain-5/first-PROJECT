import streamlit as st
from pathlib import Path

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(
    page_title="FileVault | File Handling Suite",
    page_icon="🗂️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------- CUSTOM CSS -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #0f1116;
    }
    .stApp {
        background: linear-gradient(180deg, #0f1116 0%, #14161d 100%);
    }
    h1 {
        font-weight: 800;
        letter-spacing: -1px;
    }
    .subtitle {
        color: #9ca3af;
        font-size: 1.05rem;
        margin-top: -10px;
        margin-bottom: 25px;
    }
    .card {
        background-color: #1a1d27;
        padding: 1.6rem;
        border-radius: 16px;
        border: 1px solid #2a2e3a;
        margin-bottom: 1rem;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        border: none;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        transition: 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        opacity: 0.85;
        transform: translateY(-1px);
    }
    .stTextInput > div > div > input, .stTextArea textarea {
        border-radius: 10px;
    }
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ----------------------------- HEADER -----------------------------
st.title("🗂️ FileVault")
st.markdown('<p class="subtitle">A clean, minimal file handling suite — Create, Read, Update & Delete files, all from your browser.</p>', unsafe_allow_html=True)

# ----------------------------- SIDEBAR -----------------------------
st.sidebar.title("Navigation")
operation = st.sidebar.radio(
    "Choose an operation",
    ["📄 Create", "🔍 Read", "✏️ Update", "🗑️ Delete"],
    label_visibility="collapsed"
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "**About**\n\n"
    "FileVault is a lightweight Python + Streamlit project demonstrating "
    "core file I/O operations (create, read, update, delete) with `pathlib`."
)

# ----------------------------- CREATE -----------------------------
if operation == "📄 Create":
    st.subheader("Create a new file")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        filename = st.text_input("File name", placeholder="e.g. notes.txt")
        content = st.text_area("File content", placeholder="Write something...", height=150)
        if st.button("Create File"):
            if not filename.strip():
                st.warning("Please enter a file name.")
            else:
                path = Path(filename)
                if path.exists():
                    st.error(f"❌ A file named **{filename}** already exists.")
                else:
                    try:
                        path.write_text(content)
                        st.success(f"✅ File **{filename}** created successfully!")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- READ -----------------------------
elif operation == "🔍 Read":
    st.subheader("Read a file")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        filename = st.text_input("File name to read", placeholder="e.g. notes.txt")
        if st.button("Read File"):
            if not filename.strip():
                st.warning("Please enter a file name.")
            else:
                path = Path(filename)
                if not path.exists():
                    st.error(f"❌ No such file: **{filename}**")
                else:
                    try:
                        content = path.read_text()
                        st.success(f"✅ Contents of **{filename}**:")
                        st.code(content if content.strip() else "(file is empty)", language=None)
                    except Exception as err:
                        st.error(f"An error occurred: {err}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- UPDATE -----------------------------
elif operation == "✏️ Update":
    st.subheader("Update a file")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        filename = st.text_input("File name to update", placeholder="e.g. notes.txt")
        action = st.selectbox("What would you like to do?", ["Rename", "Append content", "Overwrite content"])

        if action == "Rename":
            new_name = st.text_input("New file name")
            if st.button("Rename File"):
                path = Path(filename)
                new_path = Path(new_name)
                if not filename.strip() or not new_name.strip():
                    st.warning("Please fill in both file names.")
                elif not path.exists():
                    st.error(f"❌ No such file: **{filename}**")
                elif new_path.exists():
                    st.error(f"❌ A file named **{new_name}** already exists.")
                else:
                    try:
                        path.rename(new_path)
                        st.success(f"✅ Renamed **{filename}** → **{new_name}**")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")

        elif action == "Append content":
            data = st.text_area("Content to append", height=120)
            if st.button("Append"):
                path = Path(filename)
                if not filename.strip():
                    st.warning("Please enter a file name.")
                elif not path.exists():
                    st.error(f"❌ No such file: **{filename}**")
                else:
                    try:
                        with open(path, "a") as fs:
                            fs.write("\n" + data)
                        st.success(f"✅ Content appended to **{filename}**")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")

        elif action == "Overwrite content":
            data = st.text_area("New content (replaces old content)", height=120)
            if st.button("Overwrite"):
                path = Path(filename)
                if not filename.strip():
                    st.warning("Please enter a file name.")
                elif not path.exists():
                    st.error(f"❌ No such file: **{filename}**")
                else:
                    try:
                        path.write_text(data)
                        st.success(f"✅ **{filename}** overwritten successfully")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- DELETE -----------------------------
elif operation == "🗑️ Delete":
    st.subheader("Delete a file")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        filename = st.text_input("File name to delete", placeholder="e.g. notes.txt")
        confirm = st.checkbox("I understand this action cannot be undone.")
        if st.button("Delete File"):
            path = Path(filename)
            if not filename.strip():
                st.warning("Please enter a file name.")
            elif not confirm:
                st.warning("Please confirm before deleting.")
            elif not path.exists():
                st.error(f"❌ No such file: **{filename}**")
            else:
                try:
                    path.unlink()
                    st.success(f"✅ **{filename}** deleted successfully")
                except Exception as err:
                    st.error(f"An error occurred: {err}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- FOOTER -----------------------------
st.markdown("---")
st.caption("Built with Python & Streamlit · File I/O Project")