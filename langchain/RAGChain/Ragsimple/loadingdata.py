from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, WebBaseLoader
from tqdm import tqdm

from dotenv import load_dotenv
load_dotenv()


textdata = TextLoader("../data/requirement.txt").load()
pdfdata = PyPDFLoader("../data/LLMarchitecture.pdf").load()
csvdata = CSVLoader("../data/bigmac.csv").load()
webdata = WebBaseLoader("https://www.warpstream.com/blog/zero-disks-is-better-for-kafka").load()

doc1 = []

for i in textdata + pdfdata + csvdata + webdata:
    doc1.append(i)
# print(f"Total Documents Loaded: {len(doc1)}")
# print(doc1) 

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
chunks = []
for d in tqdm(doc1, desc="splitting"):
        chunks.extend(text_splitter.split_documents([d]))

print(f"Created {len(chunks)} chunks")

 # 100MB + 300MB + 400MB + 5MB == 805MB( 100mb -- 8 chunk )  -- number(embedding) -- stored(db)
# chunk to embedding -- > vector db 
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
# from langchain_ollama import OllamaEmbeddings
# embeddings = OllamaEmbeddings(
#     model="llama3",
# )
from langchain_community.vectorstores import FAISS, Chroma, Weaviate
vectorstore = FAISS.from_documents(documents=chunks, embeddings) 

Text generation ( chatgpt) 
# 1 read the question 
# 2 convert the question into vector( embeddings)
# 3 load the data from the vectordb
# 4 matching of the information from my question to data in the db 
# 5 display output in the screen 

 # how to learn llm  ?  -- embedding( number ) -- vectordb( number matching information is theire or not )
 retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

  