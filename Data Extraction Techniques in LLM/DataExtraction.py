# Extract from a text file
from langchain_community.document_loaders import TextLoader

loader = TextLoader("speech.txt")
text_loader = loader.load()
text_loader

# Extract from web page
from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader(
    web_paths= ("https://en.wikipedia.org/wiki/Large_language_model",),
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(
    class_ = ("mw-content-container","mw-page-container-inner")
)))

web_page_loader = loader.load()
web_page_loader

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

