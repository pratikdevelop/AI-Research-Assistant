import streamlit as st
from dotenv import load_dotenv

from agents.research_agent import create_research_agent
import os

load_dotenv()

# ------------------ PAGE CONFIG ------------------ #

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide",
)

# ------------------ SESSION STATE ------------------ #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "research_history" not in st.session_state:
    st.session_state.research_history = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


# ------------------ SIDEBAR ------------------ #

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

    st.markdown("---")

    st.subheader("📊 Statistics")

    st.metric("Messages", len(st.session_state.messages))
    st.metric("Research Sessions", len(st.session_state.research_history))
    st.metric("Tools", "3")

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    uploaded_pdf = st.file_uploader(
        "Upload Research PDF",
        type=["pdf"],
    )

    st.button(
        "🗃️ Research History (Coming Soon)",
        disabled=True,
        use_container_width=True,
    )

# ------------------ MAIN PAGE ------------------ #

st.title("🔬 AI Research Assistant")

st.caption(
    "Powered by Groq • LangChain • Wikipedia • ArXiv • Tavily"
)


if uploaded_pdf:


    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_pdf.name,
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    st.success("PDF uploaded successfully!")
# ------------------ LOAD AGENT ------------------ #

@st.cache_resource
def load_agent(model, temp, results):
    return create_research_agent(
        model,
        temp,
        results,
    )

agent = load_agent(
    model_name,
    temperature,
    max_results,
)

# ------------------ WELCOME SCREEN ------------------ #

if len(st.session_state.messages) == 0:

    st.info(
        """
### 👋 Welcome!

I can help you research information using:

- 📚 Wikipedia
- 📄 ArXiv Research Papers
- 🌐 Live Web Search
- 🧠 AI Summarization

#### Try asking:

- What is Retrieval-Augmented Generation?
- Latest Transformer research papers
- History of Artificial Intelligence
- Compare GPT-4 and Gemini
"""
    )

# ------------------ CHAT HISTORY ------------------ #

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ------------------ CHAT INPUT ------------------ #

question = st.chat_input(
    "Ask me anything..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching Wikipedia, ArXiv and the Web..."
        ):

            try:

                response = agent.invoke(
                    {
                        "input": question,
                        "chat_history": []
                    }
                )

                answer = response["output"]

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

                st.session_state.research_history.append(question)

            except Exception as e:

                st.error("❌ Something went wrong.")
                st.exception(e)

# ------------------ FOOTER ------------------ #

st.markdown("---")

st.caption(
    "🚀 AI Research Assistant v1.0 | Built with Streamlit, Groq, LangChain, Wikipedia, ArXiv and Tavily"
)