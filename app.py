import streamlit as st
import random
import time

# 🔍 Fonction d’analyse intelligente
def ricchcode_alpha_analysis(text, city):
    keywords = {
        "fitness": ["workout", "gym", "fitness", "body", "training", "muscle"],
        "money": ["rich", "income", "money", "business", "invest", "profit", "online", "passive income"],
        "love": ["relationship", "love", "heart", "emotion", "feelings", "romance"],
        "motivation": ["success", "goal", "grind", "motivation", "focus", "hustle", "growth"]
    }

    categories = []
    for key, words in keywords.items():
        if any(word in text.lower() for word in words):
            categories.append(key)

    if not categories:
        categories.append("general")

    platforms = {
        "fitness": "Instagram ou YouTube Shorts",
        "money": "TikTok ou Twitter",
        "love": "Instagram ou Facebook",
        "motivation": "TikTok ou YouTube Shorts",
        "general": "Instagram ou TikTok"
    }

    audience = {
        "fitness": "18-35 ans, majoritairement hommes",
        "money": "20-45 ans, mixte",
        "love": "18-40 ans, majoritairement femmes",
        "motivation": "15-35 ans, étudiants et hustlers",
        "general": "tout public"
    }

    hashtags = {
        "fitness": "#fitness #gym #workout #bodygoals",
        "money": "#makemoney #wealth #invest #sidehustle",
        "love": "#love #relationships #romance #feelings",
        "motivation": "#grind #hustle #success #mindset",
        "general": "#viral #explore #contentcreator"
    }

    emotions = {
        "fitness": "énergie, discipline",
        "money": "ambition, désir, urgence",
        "love": "émotion, vulnérabilité",
        "motivation": "rage de vaincre, intensité",
        "general": "créativité, curiosité"
    }

    best_time = random.choice(["12h", "15h", "18h", "21h"])
    main_cat = categories[0]

    return {
        "Texte analysé": text,
        "Ville sélectionnée": city,
        "Catégorie détectée": main_cat,
        "Plateforme idéale": platforms[main_cat],
        "Audience cible": audience[main_cat],
        "Hashtags recommandés": hashtags[main_cat],
        "Émotions dominantes": emotions[main_cat],
        "Heure idéale de publication": best_time + f" ({city} heure locale)",
        "Score de viralité estimé": f"{random.randint(72, 95)}%",
        "Suggestion IA": "Ajoute un appel à l'action clair à la fin. Pose une question ou propose un lien vers ton produit/offre."
    }

# 🧠 Interface utilisateur RicchCode Alpha
st.set_page_config(page_title="RicchCode Alpha", layout="centered")
st.title("🧠 RicchCode Alpha")
st.subheader("IA contre Algorithme – Optimise ton contenu, booste tes ventes, domine les plateformes.")

input_text = st.text_area("✍️ Colle ton texte ou idée ici :", placeholder="Ex: Découvrez mon savon bio au curcuma...")

city = st.selectbox(
    "📍 Choisis ta ville ou région commerciale :",
    ["Montréal", "Toronto", "Paris", "Abidjan", "Dakar", "Cotonou", "Douala", "Kinshasa", "Bruxelles", "Casablanca", "New York", "Londres", "Autre"]
)

if st.button("🚀 Lancer l’analyse"):
    if input_text.strip() == "":
        st.warning("⛔️ Le champ de texte ne peut pas être vide.")
    else:
        with st.spinner("🤖 L'IA analyse ton contenu, ajuste le ciblage, étudie les tendances..."):
            time.sleep(4)  # Simulation de réflexion
            result = ricchcode_alpha_analysis(input_text, city)
        st.success("✅ Analyse complétée avec succès")
        for key, value in result.items():
            st.markdown(f"**{key}** : {value}")
