def set_pastel_theme():
    pastel_css = """
    <style>
        /* Background & app text */
        .stApp {
            background-color: #fff8f0;
            color: #333333;
        }

        /* Chat message bubbles */
        .stChatMessage > div {
            border-radius: 15px;
        }

        /* Bot messages text */
        .stChatMessageAssistant p {
            color: black !important;
        }

        /* User messages text */
        .stChatMessageUser p {
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
