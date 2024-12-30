from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfiannce import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv 
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

## Web search agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include source"],
    show_tools_calls = True,
    markdown = True,
)

## Fianancial agent
fiannce_agent = Agent(
    name = "Fianance AI Agent",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [
        YFinanceTools(stock_price = True, analyst_recomemndations = True, stock_fundamentals = True,
                       company_news = True),
    ],
    instaructions = ["Use tables to display the data"],
    show_tools_calls = True,
    markdown = True,
)

multi_ai_agent = Agent(
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    team = [web_search_agent, fiannce_agent],
    instructions = ["Always include sources", "Use tables to display the data"],
    show_tools_calls = True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize anayst recommendation and share the latest news for NVDA",stream = True)