from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from langsmith import Client

client = Client()
prompt = client.pull_prompt("rlm/rag-prompt")

llm = ChatOpenAI(temperature=0)
generation_chain = prompt | llm | StrOutputParser()