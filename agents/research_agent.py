from langchain_groq import ChatGroq
from langchain_classic.agents import (
    create_tool_calling_agent,
    AgentExecutor
)

from agents.prompts import get_prompt
from tools.wikipedia_tool import get_wikipedia_tool
from tools.tavily_tool import get_tavily_tool
from tools.arxiv_tool import get_arxiv_tool
from tools.pdf_tool import pdf_search
def create_research_agent(
    model_name,
    temperature,
    max_results,
):

    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        max_tokens=1024,
    )

    wiki_tool = get_wikipedia_tool(max_results)
    tavily_tool = get_tavily_tool()
    arxiv_tool = get_arxiv_tool(max_results)
    tools = [
        wiki_tool,
        tavily_tool,
        arxiv_tool,
        pdf_search,

    ]

    prompt = get_prompt()

    agent = create_tool_calling_agent(
        llm,
        tools,
        prompt
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
    )

    return executor