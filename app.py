from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama

app = FastAPI(
    title="LangChain API",
    description="API for LangChain",
    version="1.0.0",
)

llm = Ollama(model="llama3")

prompt=ChatPromptTemplate.from_template(
    "You are a conversational AI. Please respond to the following input: {input}. "
)

app_routes(
    app,
    prompt|llm,
    "/chat",
)

for __name__="__main__":
    uvicorn.run(app, host="localhost", port=8000)