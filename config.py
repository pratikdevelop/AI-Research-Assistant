from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    MONGODB_URI = os.getenv("MONGODB_URI")

    DATABASE_NAME = os.getenv("DATABASE_NAME")

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    DEFAULT_MODEL = "llama-3.3-70b-versatile"

    DEFAULT_TEMPERATURE = 0.2

    DEFAULT_SEARCH_RESULTS = 3


settings = Settings()