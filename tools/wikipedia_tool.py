from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


def get_wikipedia_tool(max_results=3):

    wrapper = WikipediaAPIWrapper(
        top_k_results=max_results,
        lang="en"
    )

    return WikipediaQueryRun(api_wrapper=wrapper)