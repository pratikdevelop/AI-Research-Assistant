import streamlit as st
from dotenv import load_dotenv

from agents.research_agent import create_research_agent

from ui.sidebar import render_sidebar
from ui.chat import display_messages
from ui.pdf_manager import process_pdf
from memory.chat_memory import ChatMemory
from workspace.project_manager import ProjectManager

load_dotenv()
memory = ChatMemory()
project_manager = ProjectManager()

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide",
)



if "research_history" not in st.session_state:
    st.session_state.research_history = []

if "session_id" not in st.session_state:

    st.session_state.session_id = (
        memory.create_session()
    )

if "messages" not in st.session_state:

    st.session_state.messages = memory.load_messages(
        st.session_state.session_id
    )
    
if "project_id" not in st.session_state:
    st.session_state.project_id = None

if "project_name" not in st.session_state:
    st.session_state.project_name = None
    
# if "vector_store" not in st.session_state:
#     st.session_state.vector_store = None

(
    model_name,
    temperature,
    max_results,
    uploaded_pdf,
    project_id,
) = render_sidebar()

process_pdf(uploaded_pdf, project_id,)

st.title("🔬 AI Research Assistant")

display_messages()

@st.cache_resource
def load_agent(
    model,
    temp,
    results,
    project_id,
):
    return create_research_agent(
        model,
        temp,
        results,
        project_id,
    )

agent = load_agent(
    model_name,
    temperature,
    max_results,
    st.session_state.project_id,
)
question = st.chat_input("Ask a research question...")

if question:

    memory.save_user_message(
        st.session_state.session_id,
        question,
    )

    st.session_state.messages = memory.load_messages(
        st.session_state.session_id
    )

    with st.chat_message("assistant"):

        with st.spinner("Researching..."):

            response = agent.invoke(
                {
                    "input": question,
                    "chat_history": [],
                }
            )

            answer = response["output"]

            st.markdown(answer)

            memory.save_ai_message(
                st.session_state.session_id,
                answer,
            )

            st.session_state.messages = memory.load_messages(
                st.session_state.session_id
            )
