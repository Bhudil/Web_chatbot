import re
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain import HuggingFaceHub
from langchain.chains import RetrievalQA

st.set_page_config(page_title="Brainlox Chatbot", page_icon=":brain:")

# Set Streamlit app
st.title("Brainlox Chatbot 🧠")
st.markdown("---")

course_urls = [
    "https://brainlox.com/courses/4f629d96-5ed9-4302-ae0e-3479c543a49e",
    "https://brainlox.com/courses/2cf11f62-6452-41f1-9b42-303fb371b873",
    "https://brainlox.com/courses/0deafb39-3208-42db-93e3-bd69f8562f82",
    "https://brainlox.com/courses/fc9e2faf-dbe1-47bf-994c-f566a9ad3b42",
    "https://brainlox.com/courses/b0f2428a-c1c0-4def-8ac2-692a2d51a5b4",
    "https://brainlox.com/courses/fc29b015-962f-41fc-bc93-181d3ed87842",
    "https://brainlox.com/courses/f9f7b907-5f4f-472d-a7e1-d44d38255a42",
    "https://brainlox.com/courses/6a0fc4c9-2074-4854-ac31-c7dfad9ed932",
    "https://brainlox.com/courses/89d301ea-ff81-4224-8d38-a35e8575bffd",
    "https://brainlox.com/courses/category/technical"
]

loader = UnstructuredURLLoader(urls=course_urls)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(data)

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

repo_id = "HuggingFaceH4/zephyr-7b-alpha"
key = "YOUR_HUGGINGFACE_API_KEY"
llm2 = HuggingFaceHub(huggingfacehub_api_token=key,
                      repo_id=repo_id,
                      model_kwargs={"temperature": 0.4, "max_length": 512})

retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm2,
    retriever=retriever,
    return_source_documents=False
)

# Course query input
query = st.text_input("Enter your course-related query:")

if query:
    with st.spinner("Processing your query..."):
        result = qa_chain.invoke({"query": query})
        # Extract the helpful answer using regular expressions
        pattern = r"Helpful Answer: (.*)"
        match = re.search(pattern, result["result"])
        if match:
            helpful_answer = match.group(1)
            st.success(helpful_answer)
        else:
            st.warning("No helpful answer found")
            
