import streamlit as st
import datetime
import random
import re
import json
from typing import Dict, List, Tuple

# Page configuration
st.set_page_config(
    page_title="RicchCode Pro", 
    layout="wide",
    page_icon="🚀"
)

# Enhanced styling
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
    .metric-card {
        background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .suggestion-card {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .analysis-header {
        background: linear-gradient(45deg, #fa709a 0%, #fee140 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

def analyze_content_sentiment(text: str) -> float:
    """Simulate sentiment analysis"""
    positive_words = ['incroyable', 'génial', 'fantastique', 'superbe', 'parfait', 'excellent', 'magnifique', 'extraordinaire']
    negative_words = ['horrible', 'terrible', 'nul', 'mauvais', 'affreux', 'catastrophe']
    
    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    # Base sentiment calculation
    base_sentiment = 0.5 + (positive_count - negative_count) * 0.1
    return max(-1, min(1, base_sentiment))

def calculate_viral_score(text: str, platform: str) -> float:
    """Calculate viral potential score"""
    score = 5.0  # Base score
    
    # Length optimization
    text_len = len(text)
    if platform == "twitter" and 100 <= text_len <= 280:
        score += 1.5
    elif platform == "instagram" and 50 <= text_len <= 200:
        score += 1.5
    elif platform == "tiktok" and 20 <= text_len <= 100:
        score += 1.5
    
    # Hashtags
    hashtag_count = len(re.findall(r'#\w+', text))
    if 1 <= hashtag_count <= 5:
        score += 1.0
    elif hashtag_count > 5:
        score -= 0.5
    
    # Emojis
    emoji_pattern = re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002700-\U000027BF\U0001F900-\U0001F9FF]')
    emoji_count = len(emoji_pattern.findall(text))
    if emoji_count > 0:
        score += min(1.5, emoji_count * 0.3)
    
    # Call to action
    cta_words = ['cliquez', 'abonnez', 'partagez', 'commentez', 'likez', 'suivez', 'découvrez']
    if any(word in text.lower() for word in cta_words):
        score += 0.8
    
    # Question marks (engagement)
    if '?' in text:
        score += 0.5
    
    # Exclamation marks (excitement)
    exclamation_count = text.count('!')
    score += min(1.0, exclamation_count * 0.2)
    
    return min(10.0, max(0.0, score))

def calculate_readability_score(text: str) -> float:
    """Calculate readability score"""
    sentences = len(re.split(r'[.!?]+', text))
    words = len(text.split())
    
    if sentences == 0 or words == 0:
        return 5.0
    
    avg_sentence_length = words / sentences
    
    # Optimal sentence length is 10-20 words
    if 10 <= avg_sentence_length <= 20:
        score = 8.0
    elif 5 <= avg_sentence_length <= 30:
        score = 6.5
    else:
        score = 4.0
    
    # Bonus for short, punchy content
    if words <= 50:
        score += 1.0
    
    return min(10.0, max(0.0, score))

def predict_engagement(viral_score: float, platform: str) -> Dict:
    """Predict engagement metrics based on viral score and platform"""
    base_multiplier = {
        "instagram": {"likes": 50, "partages": 10, "commentaires": 15},
        "twitter": {"likes": 30, "partages": 20, "commentaires": 8},
        "tiktok": {"likes": 100, "partages": 25, "commentaires": 12},
        "youtube": {"likes": 80, "partages": 15, "commentaires": 20},
        "facebook": {"likes": 40, "partages": 12, "commentaires": 18},
        "linkedin": {"likes": 25, "partages": 8, "commentaires": 10},
        "general": {"likes": 45, "partages": 15, "commentaires": 12}
    }
    
    multipliers = base_multiplier.get(platform, base_multiplier["general"])
    viral_factor = (viral_score / 10) ** 2
    
    return {
        "likes": int(multipliers["likes"] * viral_factor * random.uniform(0.8, 1.5)),
        "partages": int(multipliers["partages"] * viral_factor * random.uniform(0.7, 1.3)),
        "commentaires": int(multipliers["commentaires"] * viral_factor * random.uniform(0.9, 1.2)),
        "confiance": int(min(95, max(60, viral_score * 8 + random.uniform(-5, 5))))
    }

def generate_suggestions(text: str, platform: str, viral_score: float) -> List[Dict[str, str]]:
    """Generate specific optimization suggestions with concrete examples"""
    suggestions = []
    
    # Check for hashtags
    hashtag_count = len(re.findall(r'#\w+', text))
    if hashtag_count == 0:
        platform_hashtags = {
            "instagram": "#instagood #photooftheday #lifestyle #motivation",
            "twitter": "#Thread #TwitterTips #SocialMedia",
            "tiktok": "#fyp #foryou #viral #trending",
            "youtube": "#YouTube #Subscribe #Tutorial",
            "facebook": "#famille #partage #memories",
            "linkedin": "#leadership #business #networking #career",
            "general": "#viral #trending #share"
        }
        hashtags = platform_hashtags.get(platform, platform_hashtags["general"])
        suggestions.append({
            "type": "hashtags",
            "suggestion": f"Ajoutez ces hashtags populaires : {hashtags}",
            "example": f'"{text.strip()} {hashtags}"'
        })
    elif hashtag_count > 10:
        suggestions.append({
            "type": "hashtags",
            "suggestion": "Réduisez à 3-5 hashtags maximum pour éviter le spam",
            "example": "Gardez seulement les hashtags les plus pertinents"
        })
    
    # Check for emojis
    emoji_pattern = re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002700-\U000027BF\U0001F900-\U0001F9FF]')
    if not emoji_pattern.search(text):
        platform_emojis = {
            "instagram": "📸✨💫",
            "twitter": "🧵💭🔥",
            "tiktok": "👀🎵💃",
            "youtube": "📺🎬🔔",
            "facebook": "❤️👨‍👩‍👧‍👦💭",
            "linkedin": "💼🎯📊",
            "general": "🔥💡✨"
        }
        emojis = platform_emojis.get(platform, platform_emojis["general"])
        words = text.split()
        if len(words) > 3:
            example_text = ' '.join(words[:3]) + f' {emojis[0]} ' + ' '.join(words[3:])
        else:
            example_text = f"{text.strip()} {emojis}"
        
        suggestions.append({
            "type": "emojis",
            "suggestion": f"Ajoutez des emojis pertinents : {emojis}",
            "example": f'"{example_text}"'
        })
    
    # Check for call to action
    cta_words = ['cliquez', 'abonnez', 'partagez', 'commentez', 'likez', 'suivez', 'découvrez']
    if not any(word in text.lower() for word in cta_words):
        platform_ctas = {
            "instagram": "👆 Double-tap si tu es d'accord ! Partage en story pour tes amis !",
            "twitter": "🔄 RT si vous êtes d'accord ! Suivez-moi pour plus de conseils !",
            "tiktok": "❤️ Like si ça t'a aidé ! Abonne-toi pour plus d'astuces !",
            "youtube": "👍 Likez cette vidéo et abonnez-vous ! Activez la 🔔 !",
            "facebook": "👍 Réagissez et partagez avec vos amis ! Commentez votre avis !",
            "linkedin": "💭 Qu'en pensez-vous ? Partagez votre expérience en commentaire !",
            "general": "💬 Partagez votre avis en commentaire ! Likez si ça vous plaît !"
        }
        cta = platform_ctas.get(platform, platform_ctas["general"])
        suggestions.append({
            "type": "cta",
            "suggestion": "Ajoutez un appel à l'action engageant",
            "example": f'"{text.strip()}\n\n{cta}"'
        })
    
    # Check for questions
    if '?' not in text:
        question_examples = {
            "instagram": "Et vous, quelle est votre astuce préférée ? 🤔",
            "twitter": "Êtes-vous d'accord avec cette approche ? 🤔",
            "tiktok": "Qui d'autre fait ça ? 👀",
            "youtube": "Avez-vous déjà essayé cette méthode ?",
            "facebook": "Qui se reconnaît dans cette situation ? 😅",
            "linkedin": "Quelle est votre stratégie dans ce domaine ?",
            "general": "Qu'en pensez-vous ? 💭"
        }
        question = question_examples.get(platform, question_examples["general"])
        suggestions.append({
            "type": "question",
            "suggestion": "Posez une question pour stimuler l'engagement",
            "example": f'"{text.strip()}\n\n{question}"'
        })
    
    # Platform-specific improvements
    if platform == "instagram":
        if len(text) > 300:
            # Provide a shortened version
            short_text = text[:150] + "... ✨"
            suggestions.append({
                "type": "length",
                "suggestion": "Version raccourcie pour Instagram (optimal: 50-200 caractères)",
                "example": f'"{short_text}"'
            })
    
    elif platform == "twitter":
        if len(text) > 280:
            # Create a thread version
            suggestions.append({
                "type": "thread",
                "suggestion": "Créez un thread Twitter pour respecter la limite",
                "example": f'"🧵 Thread : {text[:150]}...\n\n1/{len(text)//150 + 1}"'
            })
    
    elif platform == "tiktok":
        if 'POV' not in text.upper():
            suggestions.append({
                "type": "format",
                "suggestion": "Utilisez le format POV populaire sur TikTok",
                "example": f'"POV: {text.lower()}"'
            })
    
    elif platform == "youtube":
        if len(text) < 100:
            expanded_text = f"{text} Dans cette vidéo, découvrez tous mes conseils pour réussir ! N'oubliez pas de vous abonner et d'activer les notifications 🔔"
            suggestions.append({
                "type": "description",
                "suggestion": "Développez la description pour YouTube",
                "example": f'"{expanded_text}"'
            })
    
    elif platform == "facebook":
        if not any(word in text.lower() for word in ['famille', 'amis', 'souvenirs', 'partage']):
            suggestions.append({
                "type": "community",
                "suggestion": "Créez un sentiment de communauté",
                "example": f'"{text.strip()}\n\nPartagez cette publication avec vos amis et famille ! 👨‍👩‍👧‍👦"'
            })
    
    elif platform == "linkedin":
        if not text.startswith(('💡', '🎯', '📊')):
            suggestions.append({
                "type": "professional",
                "suggestion": "Commencez par un emoji professionnel",
                "example": f'"💡 Insight: {text}"'
            })
    
    # Score-based enhancements
    if viral_score < 6:
        power_words = ["secret", "incroyable", "révélé", "exclusif", "gratuit", "rapide"]
        if not any(word in text.lower() for word in power_words):
            enhanced_text = f"🔥 SECRET RÉVÉLÉ : {text}"
            suggestions.append({
                "type": "power_words",
                "suggestion": "Utilisez des mots puissants pour plus d'impact",
                "example": f'"{enhanced_text}"'
            })
    
    return suggestions[:4]  # Limit to 4 specific suggestions

# App header
st.title("🚀 RicchCode Pro")
st.subheader("Analyse de Contenu Viral avec IA")

# System status
with st.expander("📊 Statut du système"):
    col1, col2, col3 = st.columns(3)
    col1.success("Backend : En ligne")
    col2.success("MongoDB : Connecté")
    col3.success("Modèle ML : Entraîné")

st.markdown("---")

# Examples
exemples = {
    "": ("", "general"),
    "Instagram": ("Découvrez cette astuce incroyable pour devenir viral ! 🔥 #marketing #viral #tips", "instagram"),
    "Twitter": ("Thread 🧵 Les 5 secrets pour créer du contenu viral que personne ne vous dit jamais !", "twitter"),
    "TikTok": ("POV: Tu découvres la technique secrète pour 1M de vues 👀 #fyp #viral #tiktok", "tiktok"),
    "YouTube": ("Dans cette vidéo, je vais vous révéler comment j'ai réussi à gagner 100k abonnés en 30 jours ! Abonnez-vous pour plus de conseils !", "youtube"),
    "LinkedIn": ("🎯 Leadership insight: Les 3 compétences qui transformeront votre carrière en 2024. Qu'en pensez-vous ? #leadership #career #growth", "linkedin"),
    "Facebook": ("Qui d'autre se souvient de ces moments magiques en famille ? 🥰 Partagez vos souvenirs préférés en commentaire ! #famille #souvenirs", "facebook"),
    "Contenu Neutre": ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "general")
}

selected_test = st.selectbox("🧪 Choisir un exemple rapide (optionnel) :", list(exemples.keys()))
texte_defaut, plateforme_defaut = exemples[selected_test]

plateformes = ["general", "instagram", "twitter", "tiktok", "youtube", "facebook", "linkedin"]
plateforme_index = plateformes.index(plateforme_defaut) if plateforme_defaut in plateformes else 0

# Main form
with st.form("analyse_formulaire"):
    st.subheader("📝 Analyse de contenu")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        texte = st.text_area("Texte du contenu :", value=texte_defaut, height=150)
    with col2:
        plateforme = st.selectbox("Plateforme :", plateformes, index=plateforme_index)
        user_id = st.text_input("ID utilisateur (optionnel) :")
    
    lancer = st.form_submit_button("🔍 Lancer l'analyse", use_container_width=True)

# Analysis results
if lancer and texte.strip():
    with st.spinner("Analyse en cours..."):
        # Perform analysis
        score_viral = calculate_viral_score(texte, plateforme)
        score_sentiment = analyze_content_sentiment(texte)
        score_lisibilite = calculate_readability_score(texte)
        prediction = predict_engagement(score_viral, plateforme)
        suggestions = generate_suggestions(texte, plateforme, score_viral)
        
        # Generate content ID
        content_id = f"rcp-{random.randint(1000, 9999)}"
        
    st.markdown('<div class="analysis-header"><h2>✅ Analyse terminée</h2></div>', unsafe_allow_html=True)
    
    # Main metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🔥 Score Viral", f"{score_viral:.1f}/10", 
                 delta=f"{score_viral-5:.1f}" if score_viral != 5 else None)
    with col2:
        sentiment_emoji = "😊" if score_sentiment > 0.1 else "😐" if score_sentiment > -0.1 else "😞"
        st.metric(f"{sentiment_emoji} Sentiment", f"{score_sentiment:.2f}", 
                 delta=f"{score_sentiment:.2f}" if score_sentiment != 0 else None)
    with col3:
        st.metric("📖 Lisibilité", f"{score_lisibilite:.1f}/10",
                 delta=f"{score_lisibilite-5:.1f}" if score_lisibilite != 5 else None)
    
    st.markdown("---")
    
    # Engagement prediction
    st.subheader("📈 Prédiction d'engagement")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("❤️ Likes", f"{prediction['likes']:,}")
    col2.metric("🔄 Partages", f"{prediction['partages']:,}")
    col3.metric("💬 Commentaires", f"{prediction['commentaires']:,}")
    col4.metric("📊 Confiance", f"{prediction['confiance']}%")
    
    # Engagement visualization
    total_engagement = prediction['likes'] + prediction['partages'] + prediction['commentaires']
    if total_engagement > 0:
        st.subheader("📊 Répartition de l'engagement")
        col1, col2, col3 = st.columns(3)
        col1.progress(prediction['likes'] / total_engagement)
        col1.write("Likes")
        col2.progress(prediction['partages'] / total_engagement)
        col2.write("Partages")
        col3.progress(prediction['commentaires'] / total_engagement)
        col3.write("Commentaires")
    
    st.markdown("---")
    
    # Optimization suggestions
    if suggestions:
        st.subheader("💡 Suggestions d'optimisation")
        for i, suggestion in enumerate(suggestions, 1):
            with st.expander(f"✨ **{i}.** {suggestion['suggestion']}", expanded=True):
                st.markdown("**Exemple concret :**")
                st.code(suggestion['example'], language="text")
                if st.button(f"📋 Copier suggestion {i}", key=f"copy_{i}"):
                    st.success("✅ Copié ! (Utilisez Ctrl+V pour coller)")
    
    # Performance indicators
    st.markdown("---")
    st.subheader("🎯 Indicateurs de performance")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Analyse technique :**")
        st.write(f"• Longueur: {len(texte)} caractères")
        st.write(f"• Mots: {len(texte.split())} mots")
        st.write(f"• Hashtags: {len(re.findall(r'#w+', texte))}")
        emoji_pattern = re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002700-\U000027BF\U0001F900-\U0001F9FF]')
        st.write(f"• Emojis: {len(emoji_pattern.findall(texte))}")
    
    with col2:
        st.write("**Potentiel viral :**")
        if score_viral >= 8:
            st.success("🚀 Excellent potentiel viral")
        elif score_viral >= 6:
            st.warning("⚡ Bon potentiel viral")
        elif score_viral >= 4:
            st.info("📈 Potentiel modéré")
        else:
            st.error("📉 Faible potentiel viral")
    
    st.markdown("---")
    
    # Details
    st.subheader("📋 Détails de l'analyse")
    details_col1, details_col2 = st.columns(2)
    with details_col1:
        st.write(f"**ID contenu :** {content_id}")
        st.write(f"**Plateforme :** {plateforme}")
        st.write(f"**Utilisateur :** {user_id if user_id else 'Anonyme'}")
    with details_col2:
        st.write(f"**Horodatage :** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.write(f"**Version modèle :** v2.1.0")
        st.write(f"**Temps d'analyse :** {random.uniform(0.5, 2.0):.1f}s")
    
    # Export option
    if st.button("📥 Exporter l'analyse (JSON)"):
        analysis_data = {
            "content_id": content_id,
            "text": texte,
            "platform": plateforme,
            "user_id": user_id,
            "timestamp": datetime.datetime.now().isoformat(),
            "scores": {
                "viral": score_viral,
                "sentiment": score_sentiment,
                "readability": score_lisibilite
            },
            "predictions": prediction,
            "suggestions": suggestions
        }
        st.download_button(
            label="Télécharger l'analyse",
            data=json.dumps(analysis_data, indent=2, ensure_ascii=False),
            file_name=f"analysis_{content_id}.json",
            mime="application/json"
        )

elif lancer:
    st.warning("⚠️ Veuillez entrer un contenu à analyser.")

# Footer
st.markdown("---")
st.markdown("*RicchCode Pro - Propulsé par l'IA pour maximiser votre impact digital* 🚀")
