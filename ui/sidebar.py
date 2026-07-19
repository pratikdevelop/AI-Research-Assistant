from dotenv import load_dotenv
import streamlit as st
from memory.chat_memory import ChatMemory

load_dotenv()
memory = ChatMemory()


def render_sidebar():

    with st.sidebar:

        st.title("🔬 AI Research Assistant")

        st.markdown("---")

        st.subheader("⚙️ Model Settings")

        model_name = st.selectbox(
            "Groq Model",
            [
                "llama-3.3-70b-versatile",
                "mixtral-8x7b-32768",
                "gemma2-9b-it",
            ],
        )

        temperature = st.slider(
            "Temperature",
            0.0,
            1.0,
            0.2,
            0.1,
        )

        max_results = st.slider(
            "Maximum Search Results",
            1,
            10,
            3,
        )

        st.divider()

        st.metric("Messages", len(st.session_state.messages))
        st.metric("Research Sessions", len(st.session_state.research_history))

        st.divider()

        if st.button("🗑 Clear Chat", use_container_width=True):
            memory.clear(
                st.session_state.session_id
            )

            st.session_state.messages=[]
            st.rerun()

        uploaded_pdf = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
        )

        return model_name, temperature, max_results, uploaded_pdf