# Structure corrigée de RicchCode Alpha (backend FastAPI + interface HTML)

# ==== app.py (backend FastAPI) ====

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# CORS pour permettre à ton frontend d'appeler l'API si besoin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/sante")
async def sante():
    # Simule les états pour test (à remplacer par des vrais appels Mongo/ML plus tard)
    return {
        "mongodb": "connecté",
        "modele_ml": "entraîné"
    }

@app.post("/analyser")
async def analyser_contenu(payload: dict):
    texte = payload.get("texte", "")
    plateforme = payload.get("plateforme", "general")
    id_utilisateur = payload.get("id_utilisateur", "auto")

    # Simulation de réponse (à remplacer par le vrai modèle ML)
    return {
        "score_viral": 7.3,
        "score_sentiment": 0.42,
        "score_lisibilite": 6.8,
        "prediction_engagement": {
            "likes": 123,
            "partages": 45,
            "commentaires": 32,
            "confiance": 87
        },
        "suggestions_optimisation": [
            "Ajoutez un appel à l'action clair",
            "Utilisez des hashtags populaires",
            "Posez une question pour inciter à commenter"
        ],
        "id_contenu": "rcp-001",
        "plateforme": plateforme,
        "horodatage_analyse": "2025-06-08T12:00:00"
    }

# ==== Arborescence recommandée ====
# - app.py
# - templates/
#     - index.html (ton fichier HTML complet que tu m’as donné)

# === Lancer le serveur ===
# uvicorn app:app --reload
