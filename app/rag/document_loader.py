from langchain.document_loaders import PyPDFLoader
import os

DATA_PATH = "data"

all_documents = []

for file in os.listdir(DATA_PATH):

    if file.endswith(".pdf"):

        path = os.path.join(DATA_PATH, file)

        loader = PyPDFLoader(path)

        documents = loader.load()

        all_documents.extend(documents)

print(f"Loaded {len(all_documents)} pages")