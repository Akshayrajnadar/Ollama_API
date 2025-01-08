# # Extract from a text file
# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("speech.txt")
# text_loader = loader.load()
# text_loader

# # Extract from web page
# from langchain_community.document_loaders import WebBaseLoader
# import bs4

# loader = WebBaseLoader(
#     web_paths= ("https://en.wikipedia.org/wiki/Large_language_model",),
#     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
#     class_ = ("mw-content-container","mw-page-container-inner")
# )))

# web_page_loader = loader.load()
# web_page_loader

# Extract data from a PDF file
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Data Extraction Techniques in LLM/attention.pdf")
pdf_loader = loader.load()
print(pdf_loader)


# Split data in to chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

documents = text_splitter.split_documents(pdf_loader)
print(documents[0])

# Stre the data in a vector store using embading model like OpenAIEmbedding and OllamaEmbedding

from lanchain_community.embedding import OllamaEmbedding
from langchain_community.vectorstores import FAISS

db=FAISS.from_documents(documents, OllamaEmbedding())

# Perform similarity search
query = "An attention function can be described as mapping a query."
results = db.similarity_search(query)
result[0].page_content

#Combing prompt and retrivers
from langchain_community.llm import Ollama

llm=Ollama(model=("llama3"))
llm

# Define a prompt
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question basedi on the provided context.
    Think step by step before proividing the detailed answer.
    <context>
    {context}
    </context>
    QuestionL {input}
    """
)

# Using langchain to make a chain between the llm model and the prompt
from langchain_chains.combine_documents import create_stuff_documents_chain

document_chain =  create_stuff_documents_chain(llm, prompt)

# Defining the retriver

retriver = db.as_retriver()


# Creating retriver chain

from langchain.chains import create_retriver_chain

retriver_chain = create_retriver_chain(retriver, document_chain)

response = retruvak_chain.invoke({"input": "What is an attention function?"})