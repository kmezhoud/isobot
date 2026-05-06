# `isobot` is a pdf reader for ISO normes

## Project Structure
```
isobot/
│
├── isobot/
│   ├── main.py
│   ├── api/
│   │   └── routes_docs.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── services/
│   │   ├── doc_service.py
│   │   ├── iso_checker.py
│   │   ├── ai_service.py
│   │   ├── rag/
│   │   │   ├── ingest.py        # ingestion PDF
│   │   │   ├── embedding.py     # embeddings
│   │   │   ├── vector_store.py  # stockage vecteurs
│   │   │   ├── search.py        # recherche
│   │   │   └── qa.py            # question/réponse
│   ├── utils/
│   │   ├── word_parser.py
│   │   ├── pdf_reader.py
│   │   └── 
│   │
│   ├── models/
│   │    └── document.py
│   └──── .env
├── data/
│   └── iso_docs/
│       ├── iso_9001.pdf
│       ├── iso_27001.pdf
│
├── uploads/
├── requirements.txt
├── Dockerfile
└── README.md

```

## Ollama (AI Local)

```{bash}
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral

# lancer ollama
ollama serve
# view service
# http://localhost:11434"
```

```
#Installer modèle embedding Ollama
ollama pull nomic-embed-text

```

## Lancer le projet

### Créer un environnement virtuel 

```bash
# créer un environnement pour installer les packages là de-dans sans affecter 
# les packages du système

# remove venv if exist
rm -rf venv
# create venv
python3 -m venv venv

# activer l'environnement
source venv/bin/activate
```


### 1. Installer
python -m pip install -r requirements.txt

### 2. Variable environnement

export OPENAI_API_KEY=your_key

### 3. Lancer
uvicorn isobot.main:isobot --reload
#python -m uvicorn isobot.main:isobot --reload

### 4. Tester
http://127.0.0.1:8000
