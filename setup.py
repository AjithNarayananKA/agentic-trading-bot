from setuptools import setup, find_packages


setup(
    name = "trading-chatbot",
    version = "0.0.1",
    author = "ajithnarayanan",
    author_email="ajithnarayananka@gmail.com",
    packages=find_packages(),
    install_requires = [
        "langchain","langgraph","tavily-python","polygon","langchain_community","langchain_google_genai","streamlit","fastapi[all]","uvicorn","langchain-pinecone","pypdf"]
)