import streamlit as st
from langchain_core.messages import HumanMessage

from agent import agent

st.set_page_config(page_title="PUCIT GPA/CGPA Assistant", page_icon="🎓")
st.title("🎓 PUCIT GPA/CGPA Assistant")
st.caption(
    "Ask about your semester GPA, projected CGPA, or what you need to hit a "
    "target CGPA."
)

# Streamlit reruns this whole script on every interaction, so the running
# conversation history has to live in st.session_state to survive reruns.
# This mirrors exactly what chat() in agent.py does with its own `history`
# list — same idea, just stored somewhere that persists across reruns.
if "history" not in st.session_state:
    st.session_state.history = []

# Redraw all past turns so the chat looks continuous after each rerun.
for msg in st.session_state.history:
    role = "user" if msg.type == "human" else "assistant"
    # Tool-call/tool-result messages don't have meaningful .content to show
    # directly as chat bubbles; only render messages that have real text.
    if getattr(msg, "content", None):
        with st.chat_message(role):
            st.markdown(msg.content)

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                result = agent.invoke({"messages": st.session_state.history})
                st.session_state.history = result["messages"]
                reply = st.session_state.history[-1]
                st.markdown(reply.content)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

with st.sidebar:
    st.subheader("Session")
    if st.button("Start a new conversation"):
        st.session_state.history = []
        st.rerun()
    st.caption(
        "Each session starts empty — nothing about you is remembered "
        "between separate runs of this app."
    )