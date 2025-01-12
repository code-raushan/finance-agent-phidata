from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

from dotenv import load_dotenv

load_dotenv()

finance_agent = Agent(
    name="finance-agent",
    model=OpenAIChat(model="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent.print_response("Which one to invest in - Apple or Google?", stream=True)