# ISO 9001 Robot

## Structure du projet
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
│   │   └── ai_service.py
│   ├── utils/
│   │   └── word_parser.py
│   └── models/
│       └── document.py
│
├── uploads/
├── requirements.txt
├── Dockerfile
└── README.md

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
http://127.0.0.1:8000/home# isobot
Robot for ISO
