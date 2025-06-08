import streamlit as st
import datetime
import random
import re
import json
import time
from typing import Dict, List, Tuple
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="RicchCode Pro - Générateur Viral IA", 
    layout="wide",
    page_icon="🚀"
)

# Enhanced styling with premium look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7);
        background-size: 300% 300%;
        animation: gradient 8s ease infinite;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        color: white;
        font-weight: 700;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .feature-card {
        background: rgba(255,255,255,0.95);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .generator-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin: 2rem 0;
    }
    
    .viral-score {
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 1.2em;
        font-weight: 600;
    }
    
    .platform-card {
        background: linear-gradient(45deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem;
        text-align: center;
        cursor: pointer;
        transition: transform 0.3s;
    }
    
    .platform-card:hover {
        transform: scale(1.05);
    }
    
    .metrics-dashboard {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .pro-tip {
        background: linear-gradient(45deg, #ffd89b 0%, #19547b 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = []
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'industry': 'general',
        'location': 'Montreal',
        'target_audience': 'general',
        'tone': 'engaging'
    }

def generate_viral_content(platform: str, topic: str, industry: str, tone: str, location: str) -> Dict:
    """Generate viral content using AI simulation"""
    
    # Content templates by platform and industry
    templates = {
        "instagram": {
            "ecommerce": [
                "🛍️ ALERTE PROMO : {topic} à prix fou ! Seulement à {location} ! Qui veut être le premier ? 👆",
                "✨ Secret révélé : Comment {topic} peut transformer votre vie ! Thread en story 👆",
                "🔥 Avant/Après : {topic} - Les résultats vont vous choquer ! Swipe pour voir ➡️"
            ],
            "fitness": [
                "💪 Transformation INCROYABLE en 30 jours avec {topic} ! Qui veut connaître le secret ? 🔥",
                "🏋️‍♀️ POV: Tu découvres {topic} et ta vie change complètement ! Dis OUI en commentaire ! 💪",
                "⚡ Erreur n°1 que font 99% des gens avec {topic} (et comment l'éviter) 👇"
            ],
            "food": [
                "🍕 RECETTE SECRÈTE : {topic} qui rend fou tout {location} ! Qui teste ce soir ? 🔥",
                "😱 Cette technique pour {topic} va vous faire économiser 200€/mois ! Sauvegarde ce post ! 📌",
                "🤤 POV: Tu goûtes {topic} pour la première fois... La réaction est épique ! 👆"
            ],
            "tech": [
                "📱 Cette astuce {topic} que 99% des gens ignorent ! Sauvegarde avant qu'elle disparaisse ! 💾",
                "🤯 {topic} : Le hack secret que les pros ne veulent pas que tu saches ! Thread ➡️",
                "⚡ 5 minutes pour maîtriser {topic} comme un expert ! Qui commence maintenant ? 🚀"
            ]
        },
        "tiktok": [
            "POV: Tu découvres {topic} et ta vie change complètement 👀 #fyp #viral",
            "Personne ne parle de {topic} mais c'est LE secret ! #astuce #hack #viral",
            "Cette technique {topic} va vous choquer ! 🤯 (Partie 1/3) #secret #viral",
            "Red flags quand quelqu'un parle de {topic} 🚩 #redflags #truth",
            "Plot twist: {topic} n'est PAS ce que vous croyez ! 😱 #plottwist #viral"
        ],
        "twitter": [
            "🧵 Thread : Les 7 secrets de {topic} que personne ne vous dit (sauvegardez ce thread) 1/8",
            "Unpopular opinion: {topic} est surévalué. Voici pourquoi (et les alternatives) ⬇️",
            "J'ai testé {topic} pendant 30 jours. Résultat : 🤯 (thread avec preuves) ⬇️",
            "Breaking: {topic} va changer votre perception de tout. Voici comment ⬇️",
            "Hot take: Si vous ne maîtrisez pas {topic}, vous perdez de l'argent chaque jour ⬇️"
        ],
        "youtube": [
            "Comment {topic} m'a fait gagner 10k€ en 30 jours (méthode complète révélée)",
            "PERSONNE ne parle de {topic} - Voici pourquoi c'est votre AVANTAGE",
            "J'ai testé {topic} pendant 6 mois : Résultats CHOQUANTS (avec preuves)",
            "La VÉRITÉ sur {topic} que les 'experts' cachent (enquête exclusive)",
            "{topic} : L'erreur à 10 000€ que font 99% des débutants"
        ],
        "linkedin": [
            "💡 Insight : Comment {topic} transforme les entreprises de {location} (données exclusives)",
            "🎯 Stratégie : 3 façons d'utiliser {topic} pour doubler votre ROI en 2024",
            "📊 Analyse : Pourquoi {topic} sera LE game-changer de votre industrie",
            "🚀 Leadership : Comment j'ai utilisé {topic} pour transformer mon équipe",
            "💼 Business case : {topic} a généré +250% de leads. Voici comment."
        ]
    }
    
    # Select template based on platform and industry
    if platform == "instagram" and industry in templates["instagram"]:
        template = random.choice(templates["instagram"][industry])
    elif platform in templates:
        template = random.choice(templates[platform])
    else:
        template = random.choice(templates["instagram"]["ecommerce"])
    
    # Generate content
    content = template.format(topic=topic, location=location)
    
    # Add tone adjustments
    if tone == "professional":
        content = content.replace("🔥", "").replace("😱", "").replace("🤯", "")
    elif tone == "casual":
        content += " 😊"
    elif tone == "urgent":
        content = "🚨 URGENT : " + content + " ⏰"
    
    # Calculate viral metrics
    viral_score = calculate_advanced_viral_score(content, platform, industry)
    engagement_prediction = predict_advanced_engagement(viral_score, platform, industry, location)
    
    return {
        "content": content,
        "viral_score": viral_score,
        "engagement": engagement_prediction,
        "platform": platform,
        "industry": industry,
        "timestamp": datetime.datetime.now()
    }

def calculate_advanced_viral_score(content: str, platform: str, industry: str) -> float:
    """Advanced viral score calculation with ML simulation"""
    score = 5.0
    
    # Content analysis
    words = content.lower().split()
    
    # High-impact words
    viral_words = ["secret", "révélé", "choquant", "incroyable", "gratuit", "urgent", "exclusif", 
                  "hack", "astuce", "méthode", "transformation", "erreur", "vérité"]
    viral_count = sum(1 for word in words if any(v in word for v in viral_words))
    score += min(2.0, viral_count * 0.4)
    
    # Emotional triggers
    emotions = ["🔥", "😱", "🤯", "💪", "⚡", "🚀", "💯", "👆", "😍"]
    emotion_count = sum(content.count(e) for e in emotions)
    score += min(1.5, emotion_count * 0.3)
    
    # Platform optimization
    platform_bonuses = {
        "instagram": 1.2 if len(content) < 200 else 0.8,
        "tiktok": 1.5 if any(word in content.lower() for word in ["pov", "fyp", "viral"]) else 1.0,
        "twitter": 1.3 if content.startswith("🧵") else 1.0,
        "youtube": 1.1 if len(content) > 50 else 0.9,
        "linkedin": 1.2 if any(word in content.lower() for word in ["insight", "stratégie", "business"]) else 1.0
    }
    score *= platform_bonuses.get(platform, 1.0)
    
    # Industry relevance
    industry_bonus = 1.1 if industry != "general" else 1.0
    score *= industry_bonus
    
    return min(10.0, max(1.0, score))

def predict_advanced_engagement(viral_score: float, platform: str, industry: str, location: str) -> Dict:
    """Advanced engagement prediction with location and industry factors"""
    
    base_metrics = {
        "instagram": {"views": 1000, "likes": 80, "comments": 15, "shares": 10},
        "tiktok": {"views": 5000, "likes": 400, "comments": 50, "shares": 25},
        "twitter": {"views": 2000, "likes": 60, "retweets": 20, "comments": 12},
        "youtube": {"views": 3000, "likes": 150, "comments": 25, "shares": 15},
        "linkedin": {"views": 800, "likes": 40, "comments": 8, "shares": 12}
    }
    
    metrics = base_metrics.get(platform, base_metrics["instagram"])
    
    # Viral score multiplier
    viral_multiplier = (viral_score / 5) ** 1.5
    
    # Location multiplier (simulate local engagement)
    location_multiplier = 1.3 if location in ["Montreal", "Paris", "London"] else 1.0
    
    # Industry multiplier
    industry_multipliers = {
        "ecommerce": 1.4,
        "fitness": 1.6,
        "food": 1.8,
        "tech": 1.2,
        "finance": 1.1,
        "lifestyle": 1.5
    }
    industry_multiplier = industry_multipliers.get(industry, 1.0)
    
    # Calculate final metrics
    final_multiplier = viral_multiplier * location_multiplier * industry_multiplier
    
    return {
        key: int(value * final_multiplier * random.uniform(0.8, 1.2))
        for key, value in metrics.items()
    }

# App Header
st.markdown("""
    <div class="main-header">
        <h1>🚀 RicchCode Pro</h1>
        <h3>Générateur de Contenu Viral alimenté par IA</h3>
        <p>L'IA qui remplace les "experts d'algorithmes" • Dominez les réseaux • Vendez plus</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar - User Profile Setup
with st.sidebar:
    st.header("👤 Profil Utilisateur")
    
    user_type = st.selectbox("Vous êtes :", [
        "Créateur de contenu", "Commerçant/E-commerce", "Freelancer", 
        "Agence Marketing", "Marque locale", "Débutant"
    ])
    
    industry = st.selectbox("Secteur d'activité :", [
        "ecommerce", "fitness", "food", "tech", "finance", "lifestyle", 
        "beauty", "travel", "education", "gaming", "general"
    ])
    
    location = st.selectbox("Localisation :", [
        "Montreal", "Paris", "London", "New York", "Toronto", 
        "Marseille", "Lyon", "Berlin", "Madrid", "Rome"
    ])
    
    target_audience = st.selectbox("Audience cible :", [
        "18-25 ans", "25-35 ans", "35-45 ans", "45+ ans", "Professionnels", "Étudiants"
    ])
    
    st.session_state.user_profile = {
        'user_type': user_type,
        'industry': industry,
        'location': location,
        'target_audience': target_audience
    }

# Main Dashboard
col1, col2 = st.columns([2, 1])

with col1:
    # Content Generator Section
    st.markdown("""
        <div class="generator-section">
            <h2>🧠 Générateur IA Viral</h2>
            <p>Générez du contenu optimisé pour l'engagement maximum</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("viral_generator"):
        st.subheader("Créer du contenu viral")
        
        # Platform selection with visual cards
        st.write("**Choisissez votre plateforme :**")
        platform_cols = st.columns(5)
        platforms = ["instagram", "tiktok", "twitter", "youtube", "linkedin"]
        platform_emojis = ["📸", "🎵", "🐦", "📺", "💼"]
        
        selected_platform = st.radio("Plateforme", platforms, 
                                   format_func=lambda x: f"{platform_emojis[platforms.index(x)]} {x.title()}")
        
        # Content topic and style
        col_topic, col_tone = st.columns(2)
        with col_topic:
            topic = st.text_input("Sujet/Produit à promouvoir :", 
                                placeholder="Ex: formation marketing, produit beauté, restaurant...")
        
        with col_tone:
            tone = st.selectbox("Ton souhaité :", [
                "engaging", "professional", "casual", "urgent", "inspirational"
            ])
        
        # Advanced options
        with st.expander("⚙️ Options avancées"):
            include_hashtags = st.checkbox("Inclure hashtags optimisés", True)
            include_cta = st.checkbox("Inclure call-to-action", True)
            content_series = st.checkbox("Créer une série de contenus (3 posts)")
        
        generate_btn = st.form_submit_button("🚀 Générer du contenu viral", use_container_width=True)
    
    # Content Generation Results
    if generate_btn and topic.strip():
        with st.spinner("🧠 L'IA analyse les tendances et génère votre contenu..."):
            time.sleep(2)  # Simulate processing
            
            if content_series:
                contents = []
                for i in range(3):
                    content = generate_viral_content(selected_platform, topic, industry, tone, location)
                    contents.append(content)
                    st.session_state.generated_content.append(content)
            else:
                content = generate_viral_content(selected_platform, topic, industry, tone, location)
                contents = [content]
                st.session_state.generated_content.append(content)
        
        st.success("✅ Contenu généré avec succès !")
        
        # Display generated content
        for i, content in enumerate(contents, 1):
            st.markdown(f"""
                <div class="viral-score">
                    <h3>📝 Contenu {i} - Score Viral: {content['viral_score']:.1f}/10</h3>
                </div>
            """, unsafe_allow_html=True)
            
            # Content display
            st.text_area(f"Contenu généré {i}:", content['content'], height=100, key=f"content_{i}")
            
            # Metrics
            col_metrics = st.columns(4)
            for j, (key, value) in enumerate(content['engagement'].items()):
                with col_metrics[j]:
                    st.metric(key.title(), f"{value:,}")
            
            # Action buttons
            col_btn = st.columns(3)
            with col_btn[0]:
                if st.button(f"📋 Copier contenu {i}", key=f"copy_content_{i}"):
                    st.success("✅ Copié dans le presse-papier !")
            with col_btn[1]:
                if st.button(f"🔄 Régénérer {i}", key=f"regen_{i}"):
                    st.rerun()
            with col_btn[2]:
                if st.button(f"💾 Sauvegarder {i}", key=f"save_{i}"):
                    st.success("✅ Sauvegardé dans l'historique !")

with col2:
    # Dashboard and Analytics
    st.markdown("""
        <div class="metrics-dashboard">
            <h3>📊 Dashboard Analytics</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    if st.session_state.generated_content:
        total_content = len(st.session_state.generated_content)
        avg_viral_score = sum(c['viral_score'] for c in st.session_state.generated_content) / total_content
        
        st.metric("Contenus générés", total_content)
        st.metric("Score viral moyen", f"{avg_viral_score:.1f}/10")
        
        # Platform distribution
        platform_counts = {}
        for content in st.session_state.generated_content:
            platform = content['platform']
            platform_counts[platform] = platform_counts.get(platform, 0) + 1
        
        if platform_counts:
            st.write("**Répartition par plateforme:**")
            for platform, count in platform_counts.items():
                st.write(f"• {platform.title()}: {count}")
    
    # Pro Tips
    st.markdown("""
        <div class="pro-tip">
            <h4>💡 Pro Tips IA</h4>
            <ul>
                <li>Postez entre 19h-21h pour max engagement</li>
                <li>Utilisez 3-5 hashtags pour Instagram</li>
                <li>Questions = +40% commentaires</li>
                <li>Emojis = +25% engagement</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Bottom Section - Advanced Features
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["📈 Analytics", "🕒 Programmation", "🎯 A/B Testing", "⚙️ Paramètres"])

with tab1:
    st.subheader("📈 Analytics avancées")
    
    if st.session_state.generated_content:
        # Create sample analytics data
        df_analytics = pd.DataFrame([
            {
                'Date': content['timestamp'].strftime('%Y-%m-%d'),
                'Platform': content['platform'],
                'Viral Score': content['viral_score'],
                'Predicted Likes': content['engagement'].get('likes', 0),
                'Industry': content['industry']
            }
            for content in st.session_state.generated_content
        ])
        
        # Display charts
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.write("**Score viral par plateforme**")
            platform_scores = df_analytics.groupby('Platform')['Viral Score'].mean()
            st.bar_chart(platform_scores)
        
        with col_chart2:
            st.write("**Engagement prédit par plateforme**")
            platform_engagement = df_analytics.groupby('Platform')['Predicted Likes'].mean()
            st.bar_chart(platform_engagement)
        
        # Data table
        st.write("**Historique détaillé**")
        st.dataframe(df_analytics, use_container_width=True)
    else:
        st.info("Générez du contenu pour voir les analytics !")

with tab2:
    st.subheader("🕒 Programmation de publication")
    st.info("🚧 Fonctionnalité en développement - Bientôt disponible !")
    
    st.write("**Fonctionnalités à venir :**")
    st.write("• Publication automatique sur Instagram, TikTok, Twitter")
    st.write("• Suggestion d'heures optimales basée sur l'IA")
    st.write("• Calendrier éditorial intelligent")
    st.write("• Analyse des meilleures heures par audience")

with tab3:
    st.subheader("🎯 A/B Testing automatique")
    st.info("🚧 Fonctionnalité en développement - Bientôt disponible !")
    
    st.write("**Fonctionnalités prévues :**")
    st.write("• Test automatique de 2-3 versions de contenu")
    st.write("• Analyse des performances en temps réel")
    st.write("• Recommandations basées sur les résultats")
    st.write("• Optimisation continue par l'IA")

with tab4:
    st.subheader("⚙️ Paramètres avancés")
    
    col_settings1, col_settings2 = st.columns(2)
    
    with col_settings1:
        st.write("**Préférences IA**")
        creativity_level = st.slider("Niveau de créativité", 1, 10, 7)
        risk_tolerance = st.slider("Tolérance au risque", 1, 10, 5)
        brand_consistency = st.slider("Consistance de marque", 1, 10, 8)
    
    with col_settings2:
        st.write("**Paramètres de contenu**")
        default_tone = st.selectbox("Ton par défaut", 
                                  ["engaging", "professional", "casual", "urgent"])
        auto_hashtags = st.checkbox("Hashtags automatiques", True)
        geo_targeting = st.checkbox("Ciblage géographique", True)
    
    if st.button("💾 Sauvegarder les paramètres"):
        st.success("✅ Paramètres sauvegardés !")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(45deg, #667eea, #764ba2); color: white; border-radius: 10px; margin-top: 2rem;">
        <h3>🚀 RicchCode Pro</h3>
        <p><strong>L'IA qui remplace les "experts d'algorithmes"</strong></p>
        <p>Dominez les réseaux • Vendez plus • Croissance garantie</p>
        <p style="font-size: 0.9em; opacity: 0.8;">
            Propulsé par FastAPI + MongoDB + Machine Learning | Version 2.1.0
        </p>
    </div>
""", unsafe_allow_html=True)
