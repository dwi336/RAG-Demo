# RAG-Demo
Retrieval-Augmented Generation Demonstration

# Voraussetzungen
- Python 3.8+
- OpenAI API key (<https://openai.com/index/openai-api/>)

# Installation (Ubuntu)
1. Virtuelle Python-Umgebung einrichten
   ```
   mkdir -p ~/Dev  
   cd ~/Dev  
   python3 -m venv venv  
   source venv/bin/activate
   ```
2. Dieses Repository klonen
   ```
   git clone https://github.com/dwi336/RAG-Demo
   ```
3. Abhängige Pakete installieren
   ```
   cd RAG-Demo  
   pip install -r requirements.txt
   ```
4. `.env`-Datei für Umgebungsvariable für OpenAI API Key erstellen
   ```
   OPENAI_API_KEY=dein-openai-api-key
   ```
# Nutzung
   ```
   python demo_rag.py
   ```
