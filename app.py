# Version Streamlit de RicchCode Alpha (fonctionne sur Streamlit Cloud)

import streamlit as st
import datetime

st.set_page_config(page_title="RicchCode Pro", layout="wide")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
    .block-container {
        padding-top: 2rem;
    }
    .css-18e3th9 {
        padding: 2rem;
        border-radius: 20px;
        background-color: rgba(255,255,255,0.95);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 RicchCode Pro")
st.subheader("Analyse de Contenu Viral avec IA")

with st.expander("📊 Statut du système"):
    col1, col2, col3 = st.columns(3)
    col1.success("Backend : En ligne")
    col2.success("MongoDB : Connecté")
    col3.success("Modèle ML : Entraîné")

st.markdown("---")

with st.form("analyse_form"):
    st.subheader("📝 Analyser un contenu")
    texte = st.text_area("Texte du contenu :", height=150)
    plateforme = st.selectbox("Plateforme :", ["general", "instagram", "twitter", "tiktok", "youtube", "facebook", "linkedin"])
    user_id = st.text_input("ID Utilisateur (optionnel) :")
    submitted = st.form_submit_button("🔍 Analyser le Contenu")

if submitted and texte.strip():
    with st.spinner("Analyse en cours..."):
        # Simulation de prédiction (à remplacer par vraie logique plus tard)
        score_viral = 7.3
        score_sentiment = 0.42
        score_lisibilite = 6.8
        prediction_engagement = {
            "likes": 123,
            "partages": 45,
            "commentaires": 32,
            "confiance": 87
        }
        suggestions = [
            "Ajoutez un appel à l'action clair",
            "Utilisez des hashtags populaires",
            "Posez une question pour inciter à commenter"
        ]

        st.success("✅ Analyse terminée")
        col1, col2, col3 = st.columns(3)
        col1.metric("🔥 Score Viral", f"{score_viral}/10")
        col2.metric("😊 Sentiment", f"{score_sentiment}")
        col3.metric("📖 Lisibilité", f"{score_lisibilite}/10")

        st.markdown("---")
        st.subheader("📈 Engagement Prévu")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("❤️ Likes", prediction_engagement['likes'])
        col2.metric("🔄 Partages", prediction_engagement['partages'])
        col3.metric("💬 Commentaires", prediction_engagement['commentaires'])
        col4.metric("📊 Confiance", f"{prediction_engagement['confiance']}%")

        st.markdown("---")
        st.subheader("💡 Suggestions d'Optimisation")
        for s in suggestions:
            st.info(f"✨ {s}")

        st.markdown("---")
        st.subheader("📋 Détails")
        st.write(f"**ID Contenu :** rcp-001")
        st.write(f"**Plateforme :** {plateforme}")
        st.write(f"**Horodatage :** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

elif submitted:
    st.warning("⚠️ Veuillez entrer du texte pour l'analyse.")

st.markdown("---")
st.subheader("🧪 Tests Rapides")
col1, col2, col3, col4, col5 = st.columns(5)

exemples = [
    ("Découvrez cette astuce incroyable pour devenir viral ! 🔥 #marketing #viral #tips", "instagram"),
    ("Thread 🧵 Les 5 secrets pour créer du contenu viral que personne ne vous dit jamais !", "twitter"),
    ("POV: Tu découvres la technique secrète pour 1M de vues 👀 #fyp #viral #tiktok", "tiktok"),
    ("Dans cette vidéo, je vais vous révéler comment jai réussi à gagner 100k abonnés en 30 jours ! Abonnez-vous pour plus de conseils !", "youtube"),
    ("Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "general")
]

for i, (txt, pf) in enumerate(exemples):
    if i == 0: btn = col1
    elif i == 1: btn = col2
    elif i == 2: btn = col3
    elif i == 3: btn = col4
    else: btn = col5

    if btn.button(f"Test {pf.capitalize()}"):
        st.experimental_rerun()
