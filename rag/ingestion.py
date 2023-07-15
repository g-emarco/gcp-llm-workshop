from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings.vertexai import VertexAIEmbeddings
from dotenv import load_dotenv

from rag.consts import COLLECTION_NAME, DB_URL

load_dotenv()


def ingest() -> None:
    url = "https://learn.torq.io/"
    loader = RecursiveUrlLoader(url=url)
    docs = loader.load()
    print(len(docs))

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    splitted_docs = text_splitter.split_documents(docs)

    embeddings = VertexAIEmbeddings()

    PGVector.from_documents(
        embedding=embeddings,
        documents=splitted_docs,
        collection_name=COLLECTION_NAME,
        connection_string=DB_URL,
    )

    print("**** FINISHED INGESTING *****")


if __name__ == "__main__":
    ingest()
