def set_pastel_theme():
    pastel_css = """
    <style>
        .stApp {
            background-color: #fff8f0;
            color: #333333;
        }

        /* Chat message bubbles */
        .stChatMessage {
            border-radius: 15px;
        }

        /* Make all chat text black */
        .stChatMessage p, .stMarkdown p {
            color: black !important;
        }

        /* Sidebar */
        .css-1v3fvcr {
            background-color: #ffe8e0;
        }

        /* Buttons */
        .stButton>button {
            background-color: #ffcccb;
            color: #333;
        }

        /* Text input box */
        .stTextInput>div>input {
            background-color: #fff0f0;
            color: #333;
        }
    </style>
    """
    return pastel_css
