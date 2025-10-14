import streamlit as st
from nltk import download
from chat_logic import generate_response
from style import set_pastel_theme

# Download VADER lexicon
download('vader_lexicon', quiet=True)

# --- Streamlit page config ---
st.set_page_config(page_title="Mental Health Companion", page_icon="💚", layout="wide")

# --- Apply pastel theme ---
st.markdown(set_pastel_theme(), unsafe_allow_html=True)

# --- Sidebar Tabs ---
tab = st.sidebar.radio("Navigate", ["Chat", "Mood Tracker", "Journal"])

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_sentiment" not in st.session_state:
    st.session_state.last_sentiment = None
if "last_tip" not in st.session_state:
    st.session_state.last_tip = None
if "journal" not in st.session_state:
    st.session_state.journal = []

# --- Chat Tab ---
if tab == "Chat":
    st.title("💚 Mental Health Companion Chatbot")
    st.write("I’m here to listen, motivate, and provide relaxation tips. How are you feeling today?")

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        bot_response, st.session_state.last_sentiment, st.session_state.last_tip = generate_response(
            user_input, st.session_state.last_sentiment, st.session_state.last_tip
        )
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

# --- Mood Tracker Tab ---
elif tab == "Mood Tracker":
    st.title("📊 Mood Tracker")
    mood = st.selectbox("How are you feeling today?", ["Happy 😄", "Sad 😢", "Tired 😴", "Stressed 😣", "Excited 😍"])
    if st.button("Record Mood"):
        st.success(f"Mood recorded: {mood}")

# --- Journal Tab ---
elif tab == "Journal":
    st.title("📝 Personal Journal")
    entry = st.text_area("Write your journal entry here...")
    if st.button("Save Entry"):
        if entry.strip():
            st.session_state.journal.append(entry)
            st.success("Journal entry saved!")
        else:
            st.warning("Please write something before saving.")
    if st.session_state.journal:
        st.subheader("Previous Entries")
        for idx, e in enumerate(reversed(st.session_state.journal), 1):
            st.write(f"{idx}. {e}")
