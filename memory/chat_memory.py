import uuid

from database.mongodb import MongoDBManager


class ChatMemory:

    def __init__(self):

        self.db = MongoDBManager()

    # -----------------------------

    def create_session(self):

        return str(uuid.uuid4())

    # -----------------------------

    def save_user_message(
        self,
        session_id,
        message,
    ):

        self.db.save_message(
            session_id,
            "user",
            message,
        )

    # -----------------------------

    def save_ai_message(
        self,
        session_id,
        message,
    ):

        self.db.save_message(
            session_id,
            "assistant",
            message,
        )

    # -----------------------------

    def load_messages(
        self,
        session_id,
    ):

        return self.db.load_messages(
            session_id
        )

    # -----------------------------

    def clear(
        self,
        session_id,
    ):

        self.db.clear_chat(
            session_id
        )