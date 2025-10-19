# Importieren von Bibliotheken
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate

# Lade Umgebungsvariable OPENAI_API_KEY
load_dotenv()
DOC_PATH = "170206_Eckpunktepapier_Trusted_Computing-clean.pdf"
CHROMA_PATH = "MyVectorStore" 

# *** Indizierung der Daten ***
# PDF laden
loader = PyPDFLoader(DOC_PATH)
documents = loader.load()

# Aufspalten in Chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Einbetten der Chunks
embeddings = OpenAIEmbeddings()

# Einbettungen in Chroma Vector-Datenbank abspeichern
db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)

# Finden von relevanten Informationen und Generierung ***
# Frage des Nutzers
query = "Welche Anforderungen stellt die Bundesregierung an Trusted Computing?"
print("Frage:", query)

# Finden von Informationen (5 relevanteste Chunks bzgl. der Frage)
docs_chroma = db.similarity_search_with_score(query, k=5)

# Generieren der angereicherten Abfrage
context_text = "\n\n".join([doc.page_content for doc, _score in docs_chroma])

# Prompt-Vorlage
PROMPT_TEMPLATE = """
Sie sind ein persönlicher Assistent.
Beantworten Sie die Frage ausschließlich basierend auf den folgenden Informationen:
{context}
Die Frage ist: {question}.
Antworten Sie nur in vollständigen Sätzen. Wenn die Antwort nicht aus den mitgegebenen Informationen abgeleitet werden kann, antworten Sie mit "Ich weiß es nicht."
"""
# Generieren der Prompt-Vorlage
prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
prompt = prompt_template.format(context=context_text, question=query)

# Stellen der Frage
model = ChatOpenAI(model="gpt-3.5-turbo")
response = model.invoke(prompt)

# Ausgabe der Antwort
print("Antwort:", response.content)

