# 📄 agents.py
from dotenv import load_dotenv
import os
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError("❌ OPENAI_API_KEY saknas. Lägg till .env eller exportera variabeln.")

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

creative_agent = ChatOpenAI(model="gpt-4o", temperature=0.7)
technical_agent = ChatOpenAI(model="gpt-4o", temperature=0)

def run_creative(prompt):
    return creative_agent.invoke([
        SystemMessage(content="Du är en kreativ produktutvecklare som föreslår produktidéer, USPar och förbättringar."),
        HumanMessage(content=prompt)
    ])

def run_technical(prompt):
    return technical_agent.invoke([
        SystemMessage(content="Du är teknisk rådgivare och levererar specifikation i tabell samt föreslår förbättringar."),
        HumanMessage(content=prompt)
    ])