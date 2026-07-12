# 🗂️ FileVault — File Handling App

A clean, minimal file management tool built with **Python** and **Streamlit**. Create, read, update, and delete files right from your browser — no terminal required.

## ✨ Features

- **Create** — generate a new file with custom content
- **Read** — view the contents of any file
- **Update** — rename a file, append to it, or overwrite it entirely
- **Delete** — remove a file (with a confirmation check to prevent accidents)
- Built-in error handling for missing files, duplicate names, and invalid input
- Simple, dark-themed UI

## 🛠️ Tech Stack

- Python 3
- [Streamlit](https://streamlit.io/) — for the web interface
- `pathlib` — for file system operations

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. (Optional but recommended) create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run file_manager_app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## 📂 Project Structure
```
.
├── file_manager_app.py   # Main Streamlit application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 💡 What I Learned

<!-- Optional — great for LinkedIn credibility. Example: -->
- Handling file I/O safely with `pathlib` and exception handling
- Translating a CLI-based script into an interactive web UI
- Structuring a Streamlit app with reusable components and custom styling

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋 Author

Built by **[Your Name]** — feel free to connect on [LinkedIn](#) or check out more of my work on [GitHub](https://github.com/<your-username>).