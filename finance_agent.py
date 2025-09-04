"""Finance agent using Phidata (reproduction)

This script creates:
- a web search agent (DuckDuckGo tool)
- a finance agent (YFinance tools)
- composes them into a multi-agent team and runs a sample query

Adjust model/provider configuration below if you want to avoid OpenAI or switch models.
"""

import os
from dotenv import load_dotenv
load_dotenv()

# Phidata imports
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Optional: fallback to OpenAI if you want to explicitly use it
import openai

# ensure OPENAI_API_KEY is set in environment if using OpenAI models
openai_key = os.getenv("OPENAI_API_KEY")
if openai_key:
    openai.api_key = openai_key

# Create a Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Searches the web for information",
    model=Groq(id="llama-3.2-1b-preview", backend="local"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Create a Finance Agent using yfinance tools
finance_agent = Agent(
    name="Finance Agent",
    role="Fetches stock data and analyst recommendations",
    model=Groq(id="llama-3.2-1b-preview", backend="local"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Combine into a multi-agent team
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Run a sample query
if __name__ == "__main__":
    query = "Summarize analyst recommendation and share the latest news for NVDA"
    print("Running query:\n", query)
    multi_ai_agent.print_response(query, stream=False)
