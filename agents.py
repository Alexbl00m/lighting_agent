# 📄 agents.py
from langchain.chat_models import ChatOpenAI
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


# 📄 pdf_utils.py
import PyPDF2

def extract_pdf_text(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])


# 📄 vision_utils.py
import base64
from openai import OpenAI

client = OpenAI()

def analyze_image(image_path):
    with open(image_path, "rb") as img:
        image_b64 = base64.b64encode(img.read()).decode('utf-8')
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": [
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_b64}"},
                {"role": "user", "content": "Analysera produktbilden och sammanfatta tekniska nyckelvärden"}
            ]}
        ]
    )
    return response.choices[0].message.content