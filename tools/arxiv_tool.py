from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper


def get_arxiv_tool(max_results=3):

    wrapper = ArxivAPIWrapper(
        top_search_results=max_results,
        load_max_docs=max_results,
        load_all_available_meta=True
    )

    return ArxivQueryRun(api_wrapper=wrapper)