def set_pastel_theme():
    pastel_css = """
    <style>
        /* Background & cards */
        .stApp {
            background-color: #fff8f0;
            color: #333333;
        }
        .css-1d391kg {
            background-color: #fdf6f0;
        }
        /* Chat message bubbles */
        .stChatMessage > div {
            border-radius: 15px;
        }
        /* Sidebar */
        .css-1v3fvcr {
            background-color: #ffe8e0;
        }
        /* Buttons & inputs */
        .stButton>button {
            background-color: #ffcccb;
            color: #333;
        }
        .stTextInput>div>input {
            background-color: #fff0f0;
            color: #333;
        }
    </style>
    """
    return pastel_css
