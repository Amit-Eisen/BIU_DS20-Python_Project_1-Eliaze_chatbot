import streamlit as st
from main import get_response, get_conversation_stats

# --- App Config ---
st.set_page_config(page_title="ELIZA Chatbot", page_icon="🧠", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧠 ELIZA - Psychotherapist Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>A modern remake of the classic 1960s chatbot</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Init session state ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Chat Input ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 You:", placeholder="Type your message here...", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    response = get_response(user_input)
    # Don't duplicate - the engine handles conversation history
    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("eliza", response))

# --- Display Chat Messages ---
if st.session_state.history:
    # Add CSS to remove ALL Streamlit backgrounds and borders
    st.markdown("""
    <style>
    .stMarkdown > div {
        background-color: transparent !important;
        border: none !important;
    }
    .main .block-container {
        background-color: transparent !important;
    }
    .element-container {
        background-color: transparent !important;
    }
    div[data-testid="stMarkdownContainer"] {
        background-color: transparent !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("### 💬 Chat")

    for sender, msg in st.session_state.history:
        if sender == "user":
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-end; margin-bottom: 15px; width: 100%;'>
                    <div style='background-color: #dcf8c6; padding: 12px 16px; border-radius: 18px; 
                    max-width: 70%; word-wrap: break-word; 
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>{msg}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-start; margin-bottom: 15px; width: 100%;'>
                    <div style='background-color: #f1f1f1; padding: 12px 16px; border-radius: 18px; 
                    max-width: 70%; word-wrap: break-word;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>{msg}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
else:
    st.info("👋 Start the conversation by typing a message above!")

# --- Clear Chat Button ---
if st.session_state.history:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.history = []
            # Also clear the engine's conversation history
            if "conversation_history" in st.session_state:
                st.session_state.conversation_history = []
            if "used_responses" in st.session_state:
                st.session_state.used_responses = {}
            st.rerun()
