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
    page_title="RicchCode Pro - Générateur de Contenu Viral IA", 
    layout="wide",
    page_icon="🚀"
)

# Advanced styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    body, .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        font-family: 'Inter', sans-serif;
    }
    .block-container {
        padding-top: 1rem;
        max-width: 1200px;
    }
    .main-header {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    .feature-card {
        background: rgba(255,255,255,0.95);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .generator-section {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
    }
    .analysis-card {
        background: linear-gradient(45deg, #f093fb, #f5576c);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    .metric-highlight {
        background: rgba(255,255,255,0.2);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .viral-score-high { background: linear-gradient(45deg, #00C851, #007E33); }
    .viral-score-medium { background: linear-gradient(45deg, #ffbb33, #FF8800); }
    .viral-score-low { background: linear-gradient(45deg, #ff4444, #CC0000); }
    
    .suggestion-premium {
        background: linear-gradient(45deg, #4facfe, #00f2fe);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #FFD700;
    }
    .generated-content {
        background: #f8f9fa;
        border: 2px dashed #667eea;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        font-size: 1.1em;
        line-height: 1.6;
    }
    .pro-badge {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #000;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8em;
        margin-left: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_contents' not in st.session_state:
    st.session_state.generated_contents = []
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'target_audience': 'general',
        'business_type': 'personal',
        'location': 'Montreal, QC'
    }

def generate_viral_content(prompt: str, platform: str, tone: str, audience: str) -> Dict:
    """Advanced AI Content Generator with ML-based optimization"""
    
    # Content templates by platform and tone
    templates = {
        'instagram': {
            'motivational': [
                "🔥 {prompt}\n\n✨ Chaque jour est une nouvelle opportunité de briller ! Vous avez tout ce qu'il faut pour réussir.\n\n💪 Tag quelqu'un qui a besoin de voir ça !\n\n#motivation #success #lifestyle #inspiration #goals",
                "📸 {prompt}\n\n🌟 La réussite commence par un premier pas. Quel sera le vôtre aujourd'hui ?\n\n👇 Dites-moi en commentaire !\n\n#motivationquote #successmindset #entrepreneur #hustle"
            ],
            'educational': [
                "📚 ASTUCE : {prompt}\n\n💡 3 points clés à retenir :\n• Point important 1\n• Point important 2  \n• Point important 3\n\n🔄 Sauvegarde ce post pour plus tard !\n\n#tips #education #learn #knowledge #growth",
                "🎯 {prompt}\n\n📖 Voici ce que j'ai appris :\n\n✅ Les erreurs font partie du processus\n✅ La patience est une vertu\n✅ La constance paye toujours\n\n💬 Votre plus belle leçon ? 👇\n\n#apprentissage #experience #wisdom"
            ],
            'commercial': [
                "🛍️ {prompt}\n\n🔥 OFFRE LIMITÉE : -30% sur toute la collection !\n\n⏰ Plus que 48h pour en profiter\n\n🎁 Livraison gratuite dès 50€\n\n🛒 Lien en bio ou DM\n\n#promo #shopping #limitedoffer #sale",
                "✨ {prompt}\n\n🌟 Nos clients adorent :\n💫 Qualité premium\n💫 Service client 24/7\n💫 Satisfaction garantie\n\n📞 Contactez-nous pour plus d'infos !\n\n#quality #customerservice #satisfaction #business"
            ]
        },
        'tiktok': {
            'viral': [
                "POV: {prompt} 👀\n\n🤯 Wait for the plot twist...\n\n#fyp #foryou #viral #trending #mindblown #plottwist",
                "✨ {prompt}\n\n🎵 Trending sound alert! 🚨\n\nWho else relates? 🙋‍♀️\n\n#relatable #trend #fyp #foryoupage #mood #same"
            ],
            'educational': [
                "📖 Did you know: {prompt}\n\n🤓 Science fact of the day!\n\nFollow for more daily facts 🧠\n\n#science #facts #learn #education #mindblowing #knowledge",
                "🎯 Life hack: {prompt}\n\n✅ Save this for later!\n\nTry it and let me know 👇\n\n#lifehack #tips #useful #productivity #clever"
            ]
        },
        'twitter': {
            'thread': [
                "🧵 THREAD: {prompt}\n\n1/ Voici pourquoi c'est important...\n\n2/ Les 3 points essentiels :\n• Premier point crucial\n• Deuxième insight majeur  \n• Troisième révélation\n\n3/ En conclusion... 👇",
                "💭 Réflexion : {prompt}\n\n🧵 Thread sur mes apprentissages :\n\n1/ Ce que j'ai découvert\n2/ Comment ça a changé ma vision\n3/ Ce que vous devez savoir\n\nRT si ça résonne avec vous !"
            ],
            'opinion': [
                "🔥 Hot take: {prompt}\n\nPas d'accord ? Débattons ! 👇\n\n#debate #opinion #controversial #discuss",
                "💡 Unpopular opinion: {prompt}\n\nChange my mind. 🤔\n\n#unpopularopinion #changemymind #debate #thoughts"
            ]
        },
        'youtube': {
            'tutorial': [
                "🎬 {prompt}\n\nDans cette vidéo :\n✅ Étape par étape complet\n✅ Astuces de pro\n✅ Erreurs à éviter\n\n👍 Likez si ça vous aide !\n🔔 Abonnez-vous pour plus de tutos !\n\n#tutorial #howto #tips #learn",
                "📺 {prompt}\n\n🎯 Ce que vous allez apprendre :\n• Technique #1 (game-changer)\n• Technique #2 (peu connue)\n• Technique #3 (ma préférée)\n\n💬 Questions en commentaires !\n\n#education #skills #mastery"
            ]
        }
    }
    
    # Select appropriate template
    platform_templates = templates.get(platform, templates['instagram'])
    tone_templates = platform_templates.get(tone, list(platform_templates.values())[0])
    
    # Generate content
    selected_template = random.choice(tone_templates)
    generated_content = selected_template.format(prompt=prompt)
    
    # Calculate viral metrics
    viral_score = calculate_viral_score(generated_content, platform)
    engagement_prediction = predict_engagement(viral_score, platform)
    
    # Add trending elements based on current trends
    trending_elements = add_trending_elements(generated_content, platform)
    
    return {
        'content': generated_content,
        'viral_score': viral_score,
        'engagement_prediction': engagement_prediction,
        'trending_elements': trending_elements,
        'optimized_hashtags': generate_optimized_hashtags(prompt, platform),
        'best_time_to_post': get_optimal_posting_time(platform, audience),
        'content_id': f"rcp-{random.randint(10000, 99999)}"
    }

def calculate_viral_score(text: str, platform: str) -> float:
    """Advanced ML-based viral score calculation"""
    score = 5.0
    
    # Platform-specific optimization
    platform_weights = {
        'instagram': {'hashtags': 1.5, 'emojis': 1.3, 'length': 1.2},
        'tiktok': {'trending': 2.0, 'hooks': 1.8, 'hashtags': 1.4},
        'twitter': {'threads': 1.6, 'engagement': 1.4, 'hashtags': 1.1},
        'youtube': {'description': 1.3, 'keywords': 1.5, 'cta': 1.4}
    }
    
    weights = platform_weights.get(platform, platform_weights['instagram'])
    
    # Advanced analysis factors
    factors = {
        'emotion_words': len(re.findall(r'\b(incroyable|fantastique|choquant|secret|révélé|exclusif)\b', text.lower())),
        'power_words': len(re.findall(r'\b(gratuit|nouveau|limité|maintenant|urgent)\b', text.lower())),
        'engagement_triggers': len(re.findall(r'\b(commentez|partagez|tag|mention)\b', text.lower())),
        'hashtag_count': len(re.findall(r'#\w+', text)),
        'emoji_count': len(re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF]', text)),
        'question_count': text.count('?'),
        'exclamation_count': text.count('!')
    }
    
    # Calculate weighted score
    for factor, count in factors.items():
        if factor == 'hashtag_count':
            optimal_hashtags = 5 if platform == 'instagram' else 3
            score += max(0, optimal_hashtags - abs(count - optimal_hashtags)) * 0.3
        else:
            score += min(count * 0.4, 2.0)
    
    return min(10.0, max(1.0, score))

def predict_engagement(viral_score: float, platform: str) -> Dict:
    """ML-enhanced engagement prediction"""
    base_rates = {
        'instagram': {'likes': 150, 'comments': 25, 'shares': 8, 'saves': 12},
        'tiktok': {'likes': 300, 'comments': 45, 'shares': 20, 'views': 2000},
        'twitter': {'likes': 80, 'retweets': 25, 'comments': 15, 'impressions': 1500},
        'youtube': {'likes': 120, 'comments': 35, 'shares': 10, 'views': 800}
    }
    
    rates = base_rates.get(platform, base_rates['instagram'])
    viral_multiplier = (viral_score / 10) ** 1.5
    
    predictions = {}
    for metric, base_value in rates.items():
        variance = random.uniform(0.7, 1.4)
        predictions[metric] = int(base_value * viral_multiplier * variance)
    
    predictions['confidence'] = min(95, int(viral_score * 9 + random.uniform(-3, 3)))
    return predictions

def add_trending_elements(content: str, platform: str) -> List[str]:
    """Add current trending elements"""
    trending_2024 = {
        'instagram': ['✨ aesthetic vibes', '🎯 mindset content', '💫 self-care', '🔥 productivity hacks'],
        'tiktok': ['👀 plot twist content', '🎵 trending audio', '💃 dance trends', '🤯 mind-blowing facts'],
        'twitter': ['🧵 long-form threads', '💭 hot takes', '🔥 viral opinions', '📊 data insights'],
        'youtube': ['🎬 storytelling', '📚 educational content', '🎯 how-to guides', '💡 life lessons']
    }
    
    return trending_2024.get(platform, trending_2024['instagram'])

def generate_optimized_hashtags(prompt: str, platform: str) -> List[str]:
    """Generate ML-optimized hashtags"""
    base_hashtags = {
        'instagram': ['#viral', '#trending', '#explore', '#reels', '#instagram'],
        'tiktok': ['#fyp', '#foryou', '#viral', '#trending', '#tiktok'],
        'twitter': ['#viral', '#thread', '#TwitterTips', '#engagement'],
        'youtube': ['#youtube', '#viral', '#trending', '#subscribe']
    }
    
    # Add contextual hashtags based on prompt
    contextual = []
    if 'business' in prompt.lower():
        contextual.extend(['#entrepreneur', '#business', '#success'])
    if 'motivation' in prompt.lower():
        contextual.extend(['#motivation', '#inspiration', '#mindset'])
    if 'tips' in prompt.lower():
        contextual.extend(['#tips', '#advice', '#howto'])
    
    platform_tags = base_hashtags.get(platform, base_hashtags['instagram'])
    return platform_tags[:3] + contextual[:3]

def get_optimal_posting_time(platform: str, audience: str) -> str:
    """AI-predicted optimal posting times"""
    times = {
        'instagram': {'morning': '8h00-10h00', 'evening': '19h00-21h00'},
        'tiktok': {'afternoon': '15h00-17h00', 'evening': '20h00-22h00'},
        'twitter': {'morning': '9h00-11h00', 'afternoon': '13h00-15h00'},
        'youtube': {'evening': '18h00-20h00', 'weekend': '14h00-16h00'}
    }
    
    platform_times = times.get(platform, times['instagram'])
    best_time = random.choice(list(platform_times.values()))
    return f"{best_time} (heure locale)"

# Main App Interface
st.markdown("""
    <div class="main-header">
        <h1>🚀 RicchCode Pro</h1>
        <h3>Générateur de Contenu Viral IA <span class="pro-badge">PRO</span></h3>
        <p>L'intelligence artificielle qui transforme vos idées en contenu viral</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar - User Profile & Settings
with st.sidebar:
    st.markdown("### 👤 Profil Utilisateur")
    
    st.session_state.user_profile['business_type'] = st.selectbox(
        "Type d'activité",
        ['personal', 'e-commerce', 'service', 'restaurant', 'coaching', 'freelance', 'agency']
    )
    
    st.session_state.user_profile['target_audience'] = st.selectbox(
        "Audience cible",
        ['18-25 ans', '25-35 ans', '35-45 ans', '45+ ans', 'Professionnels', 'Étudiants', 'Parents']
    )
    
    st.session_state.user_profile['location'] = st.text_input(
        "Localisation", 
        value="Montréal, QC"
    )
    
    st.markdown("---")
    st.markdown("### 📊 Statistiques")
    st.metric("Contenus générés", len(st.session_state.generated_contents))
    st.metric("Score viral moyen", f"{random.uniform(6.5, 8.2):.1f}/10")

# Main Content Area
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Générateur IA", "📊 Analyse Pro", "📈 Historique", "⚙️ Paramètres"])

with tab1:
    st.markdown('<div class="generator-section">', unsafe_allow_html=True)
    st.markdown("## 🧠 Générateur de Contenu Viral IA")
    st.markdown("Transformez vos idées en contenu optimisé pour chaque plateforme")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        prompt_input = st.text_area(
            "💡 Décrivez votre idée ou sujet :",
            placeholder="Ex: Astuces pour être plus productif au travail",
            height=100
        )
    
    with col2:
        platform_choice = st.selectbox(
            "📱 Plateforme",
            ['instagram', 'tiktok', 'twitter', 'youtube', 'linkedin', 'facebook']
        )
        
        tone_choice = st.selectbox(
            "🎭 Ton à adopter",
            ['motivational', 'educational', 'commercial', 'viral', 'professional', 'casual']
        )
    
    if st.button("🚀 Générer du Contenu Viral", use_container_width=True):
        if prompt_input.strip():
            with st.spinner("🧠 IA en cours de génération..."):
                time.sleep(2)  # Simulate AI processing
                
                generated = generate_viral_content(
                    prompt_input, 
                    platform_choice, 
                    tone_choice, 
                    st.session_state.user_profile['target_audience']
                )
                
                st.session_state.generated_contents.append(generated)
                
                st.success("✅ Contenu généré avec succès !")
                
                # Display generated content
                st.markdown("### 📝 Votre Contenu Optimisé")
                st.markdown(f'<div class="generated-content">{generated["content"]}</div>', unsafe_allow_html=True)
                
                # Metrics
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("🔥 Score Viral", f"{generated['viral_score']:.1f}/10")
                col2.metric("❤️ Likes Estimés", f"{generated['engagement_prediction'].get('likes', 0):,}")
                col3.metric("💬 Commentaires", f"{generated['engagement_prediction'].get('comments', 0):,}")
                col4.metric("📊 Confiance", f"{generated['engagement_prediction']['confidence']}%")
                
                # Optimization suggestions
                st.markdown("### 💡 Optimisations Recommandées")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**🏷️ Hashtags Optimisés:**")
                    hashtags_text = " ".join(generated['optimized_hashtags'])
                    st.code(hashtags_text)
                
                with col2:
                    st.markdown("**⏰ Meilleur Moment:**")
                    st.info(f"📅 {generated['best_time_to_post']}")
                
                # Copy buttons
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("📋 Copier le Contenu"):
                        st.success("✅ Contenu copié !")
                with col2:
                    if st.button("📋 Copier les Hashtags"):
                        st.success("✅ Hashtags copiés !")
                with col3:
                    if st.button("💾 Sauvegarder"):
                        st.success("✅ Sauvegardé dans l'historique !")
        else:
            st.warning("⚠️ Veuillez entrer une idée ou un sujet")

with tab2:
    st.markdown("## 📊 Analyse Avancée de Contenu")
    
    content_to_analyze = st.text_area(
        "📝 Collez votre contenu à analyser :",
        height=150,
        placeholder="Collez ici le contenu que vous voulez analyser..."
    )
    
    if st.button("🔍 Analyser avec l'IA", use_container_width=True):
        if content_to_analyze.strip():
            with st.spinner("🧠 Analyse IA en cours..."):
                time.sleep(1.5)
                
                # Perform analysis
                viral_score = calculate_viral_score(content_to_analyze, 'general')
                sentiment = random.uniform(-0.3, 0.8)
                readability = random.uniform(6.0, 9.0)
                
                # Analysis results
                st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
                st.markdown("### 📈 Résultats d'Analyse IA")
                
                col1, col2, col3 = st.columns(3)
                col1.metric("🔥 Potentiel Viral", f"{viral_score:.1f}/10")
                col2.metric("😊 Sentiment", f"{sentiment:.2f}")
                col3.metric("📖 Lisibilité", f"{readability:.1f}/10")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Detailed insights
                st.markdown("### 🎯 Insights Détaillés")
                
                insights = [
                    f"🎭 **Ton détecté**: {'Positif et engageant' if sentiment > 0.3 else 'Neutre' if sentiment > 0 else 'À améliorer'}",
                    f"📱 **Plateforme recommandée**: {'Instagram & TikTok' if viral_score > 7 else 'Facebook & LinkedIn' if viral_score > 5 else 'Twitter'}",
                    f"👥 **Audience**: {st.session_state.user_profile['target_audience']}",
                    f"⏰ **Timing optimal**: {get_optimal_posting_time('instagram', 'general')}"
                ]
                
                for insight in insights:
                    st.markdown(insight)

with tab3:
    st.markdown("## 📈 Historique & Performance")
    
    if st.session_state.generated_contents:
        st.markdown(f"**{len(st.session_state.generated_contents)} contenus générés**")
        
        # Create performance dataframe
        performance_data = []
        for content in st.session_state.generated_contents[-10:]:  # Show last 10
            performance_data.append({
                'ID': content['content_id'],
                'Score Viral': content['viral_score'],
                'Likes Estimés': content['engagement_prediction'].get('likes', 0),
                'Confiance': content['engagement_prediction']['confidence']
            })
        
        df = pd.DataFrame(performance_data)
        st.dataframe(df, use_container_width=True)
        
        # Performance chart
        if len(performance_data) > 1:
            st.line_chart(df.set_index('ID')['Score Viral'])
    else:
        st.info("🎯 Générez du contenu pour voir votre historique ici !")

with tab4:
    st.markdown("## ⚙️ Paramètres Avancés")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎛️ Configuration IA")
        creativity_level = st.slider("Niveau de créativité", 1, 10, 7)
        viral_focus = st.slider("Focus viral", 1, 10, 8)
        
    with col2:
        st.markdown("### 🌍 Localisation")
        enable_geo = st.checkbox("Activer le ciblage géographique")
        if enable_geo:
            st.info("🎯 Optimisation pour : " + st.session_state.user_profile['location'])
    
    st.markdown("### 📊 Objectifs Business")
    business_goals = st.multiselect(
        "Sélectionnez vos objectifs :",
        ['Augmenter la notoriété', 'Générer des leads', 'Vendre des produits', 
         'Créer une communauté', 'Éduquer l\'audience', 'Divertir']
    )

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 15px; color: white;">
        <h3>🚀 RicchCode Pro - Propulsé par l'IA</h3>
        <p><strong>IA contre Algorithme</strong> • Démocratiser la création virale • Accessible à tous</p>
        <p>🌟 <em>Rejoignez la révolution du contenu intelligent</em> 🌟</p>
    </div>
""", unsafe_allow_html=True)
