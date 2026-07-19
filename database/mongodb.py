import os
from datetime import datetime
from datetime import datetime

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()


class MongoDBManager:

    def __init__(self):
        self.projects_collection = self.db["projects"]

        self.client = MongoClient(
            os.getenv("MONGODB_URI"),
            serverSelectionTimeoutMS=5000,
        )

        try:
            self.client.admin.command("ping")
            print("✅ Connected to MongoDB Atlas")

        except ConnectionFailure as e:
            raise Exception(
                f"MongoDB Connection Failed: {e}"
            )

        self.db = self.client[
            os.getenv("DATABASE_NAME")
        ]

        self.chat_collection = self.db["chats"]

        self.history_collection = self.db["research_history"]

    # ----------------------------

    def save_message(
        self,
        session_id,
        role,
        content,
    ):

        self.chat_collection.insert_one(
            {
                "session_id": session_id,
                "role": role,
                "content": content,
                "created_at": datetime.utcnow(),
            }
        )

    # ----------------------------

    def load_messages(
        self,
        session_id,
    ):

        return list(
            self.chat_collection.find(
                {
                    "session_id": session_id
                },
                {
                    "_id": 0
                }
            ).sort("created_at", 1)
        )

    # ----------------------------

    def clear_chat(
        self,
        session_id,
    ):

        self.chat_collection.delete_many(
            {
                "session_id": session_id
            }
        )

    # ----------------------------

    def save_research(
        self,
        question,
        answer,
        sources,
    ):

        self.history_collection.insert_one(
            {
                "question": question,
                "answer": answer,
                "sources": sources,
                "created_at": datetime.utcnow(),
            }
        )

    # ----------------------------

    def get_research_history(self):

        return list(
            self.history_collection.find(
                {},
                {
                    "_id": 0
                }
            ).sort("created_at", -1)
        )
        
    def get_projects(self):

        return list(

            self.projects_collection.find(
                {},
                {"_id": 0}
            )

        )
        
    def add_pdf(
        self,
        project_name,
        filename,
    ):

        self.projects_collection.update_one(

            {

                "project_name": project_name

            },

            {

                "$push": {

                    "pdfs": filename

                }

            }

        )
        
    def create_project(
            self,
            project_name,
            description="",
        ):

        project = {

            "project_name": project_name,

            "description": description,

            "created_at": datetime.utcnow(),

            "updated_at": datetime.utcnow(),

            "pdfs": []
        }

        result = self.projects_collection.insert_one(project)

        return str(result.inserted_id)