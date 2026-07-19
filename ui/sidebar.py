from dotenv import load_dotenv
import streamlit as st

from memory.chat_memory import ChatMemory
from workspace.project_manager import ProjectManager

load_dotenv()

memory = ChatMemory()
project_manager = ProjectManager()


def render_sidebar():

    with st.sidebar:

        st.title("🔬 AI Research Assistant")

        st.markdown("---")

        # =====================================================
        # RESEARCH WORKSPACE
        # =====================================================

        st.subheader("📂 Research Workspace")

        # Session State
        if "project_id" not in st.session_state:
            st.session_state.project_id = None

        if "project_name" not in st.session_state:
            st.session_state.project_name = None

        projects = project_manager.get_projects()

        project_names = [
            project["project_name"]
            for project in projects
        ]

        if project_names:

            default_index = 0

            if (
                st.session_state.project_name
                and st.session_state.project_name in project_names
            ):
                default_index = project_names.index(
                    st.session_state.project_name
                )

            selected_project = st.selectbox(
                "Current Project",
                project_names,
                index=default_index,
            )

            project = project_manager.get_project_by_name(
                selected_project
            )

            st.session_state.project_id = project["project_id"]
            st.session_state.project_name = project["project_name"]

        else:

            st.info("No projects found.")

        # ---------------------------
        # Create New Project
        # ---------------------------

        new_project = st.text_input(
            "New Project"
        )

        if st.button(
            "➕ Create Project",
            use_container_width=True,
        ):

            if new_project.strip():

                project_manager.create_project(
                    new_project.strip()
                )

                st.success("Project created successfully!")

                st.rerun()

            else:

                st.warning("Enter a project name.")

        st.markdown("---")

        # =====================================================
        # MODEL SETTINGS
        # =====================================================

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

        # =====================================================
        # STATISTICS
        # =====================================================

        st.subheader("📊 Statistics")

        st.metric(
            "Messages",
            len(st.session_state.messages)
        )

        st.metric(
            "Research Sessions",
            len(st.session_state.research_history)
        )

        if st.session_state.project_name:

            st.metric(
                "Current Project",
                st.session_state.project_name,
            )

        st.markdown("---")

        # =====================================================
        # CHAT
        # =====================================================

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True,
        ):

            memory.clear(
                st.session_state.session_id,
            )

            st.session_state.messages = []

            st.rerun()

        st.markdown("---")

        # =====================================================
        # PDF Upload
        # =====================================================

        uploaded_pdf = st.file_uploader(
            "📄 Upload Research PDF",
            type=["pdf"],
        )

        return (
            model_name,
            temperature,
            max_results,
            uploaded_pdf,
            st.session_state.project_id,
        )