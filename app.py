<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RicchCode Pro - Interface de Test</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
        }

        .header h1 {
            font-size: 2.5em;
            color: #4a5568;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .header p {
            font-size: 1.2em;
            color: #718096;
        }

        .status-bar {
            display: flex;
            justify-content: space-around;
            background: linear-gradient(45deg, #48bb78, #38a169);
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 30px;
            color: white;
            font-weight: bold;
        }

        .status-item {
            text-align: center;
        }

        .status-item span {
            display: block;
            font-size: 0.9em;
            opacity: 0.8;
        }

        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        .input-section, .results-section {
            background: #f7fafc;
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #e2e8f0;
        }

        .input-section h3, .results-section h3 {
            color: #2d3748;
            margin-bottom: 20px;
            font-size: 1.3em;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #4a5568;
        }

        textarea, select, input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            font-size: 16px;
            transition: all 0.3s ease;
        }

        textarea:focus, select:focus, input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        textarea {
            height: 120px;
            resize: vertical;
        }

        .btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }

        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .results-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border-left: 4px solid #667eea;
        }

        .score-display {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
        }

        .score-item {
            text-align: center;
            flex: 1;
        }

        .score-value {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .score-label {
            color: #718096;
            font-size: 0.9em;
        }

        .viral-score { color: #e53e3e; }
        .sentiment-score { color: #38a169; }
        .readability-score { color: #3182ce; }

        .suggestions-list {
            list-style: none;
            padding: 0;
        }

        .suggestions-list li {
            background: #f0fff4;
            padding: 10px;
            margin-bottom: 8px;
            border-radius: 8px;
            border-left: 3px solid #38a169;
        }

        .engagement-prediction {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }

        .prediction-item {
            text-align: center;
            background: #f7fafc;
            padding: 15px;
            border-radius: 10px;
        }

        .prediction-value {
            font-size: 1.5em;
            font-weight: bold;
            color: #667eea;
        }

        .prediction-label {
            color: #718096;
            font-size: 0.9em;
        }

        .loading {
            text-align: center;
            padding: 20px;
            color: #718096;
        }

        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #667eea;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .error {
            background: #fed7d7;
            color: #c53030;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            border-left: 4px solid #e53e3e;
        }

        .test-section {
            background: #f7fafc;
            padding: 25px;
            border-radius: 15px;
            margin-top: 30px;
            border: 1px solid #e2e8f0;
        }

        .test-buttons {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .test-btn {
            background: linear-gradient(45deg, #48bb78, #38a169);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .test-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
        }

        @media (max-width: 768px) {
            .main-content {
                grid-template-columns: 1fr;
            }
            
            .status-bar {
                flex-direction: column;
                gap: 10px;
            }
            
            .test-buttons {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 RicchCode Pro</h1>
            <p>Interface de Test - Analyse de Contenu Viral avec IA</p>
        </div>

        <div class="status-bar" id="statusBar">
            <div class="status-item">
                <div id="backendStatus">🔄 Vérification...</div>
                <span>Backend</span>
            </div>
            <div class="status-item">
                <div id="mongoStatus">🔄 Vérification...</div>
                <span>MongoDB</span>
            </div>
            <div class="status-item">
                <div id="mlStatus">🔄 Vérification...</div>
                <span>Modèle ML</span>
            </div>
        </div>

        <div class="main-content">
            <div class="input-section">
                <h3>📝 Analyser du Contenu</h3>
                <form id="analyzeForm">
                    <div class="form-group">
                        <label for="contentText">Texte du contenu :</label>
                        <textarea id="contentText" placeholder="Écrivez votre contenu ici pour l'analyser..." required></textarea>
                    </div>
                    
                    <div class="form-group">
                        <label for="platform">Plateforme :</label>
                        <select id="platform">
                            <option value="general">Général</option>
                            <option value="instagram">Instagram</option>
                            <option value="twitter">Twitter</option>
                            <option value="tiktok">TikTok</option>
                            <option value="youtube">YouTube</option>
                            <option value="facebook">Facebook</option>
                            <option value="linkedin">LinkedIn</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="userId">ID Utilisateur (optionnel) :</label>
                        <input type="text" id="userId" placeholder="user123">
                    </div>
                    
                    <button type="submit" class="btn" id="analyzeBtn">
                        🔍 Analyser le Contenu
                    </button>
                </form>
            </div>

            <div class="results-section">
                <h3>📊 Résultats d'Analyse</h3>
                <div id="resultsContainer">
                    <p style="text-align: center; color: #718096; padding: 40px;">
                        Entrez du contenu et cliquez sur "Analyser" pour voir les résultats
                    </p>
                </div>
            </div>
        </div>

        <div class="test-section">
            <h3>🧪 Tests Rapides</h3>
            <p style="margin-bottom: 20px; color: #718096;">Testez avec des exemples pré-définis :</p>
            <div class="test-buttons">
                <button class="test-btn" onclick="testContent('Découvrez cette astuce incroyable pour devenir viral ! 🔥 #marketing #viral #tips', 'instagram')">
                    Test Instagram
                </button>
                <button class="test-btn" onclick="testContent('Thread 🧵 Les 5 secrets pour créer du contenu viral que personne ne vous dit jamais !', 'twitter')">
                    Test Twitter
                </button>
                <button class="test-btn" onclick="testContent('POV: Tu découvres la technique secrète pour 1M de vues 👀 #fyp #viral #tiktok', 'tiktok')">
                    Test TikTok
                </button>
                <button class="test-btn" onclick="testContent('Dans cette vidéo, je vais vous révéler comment jai réussi à gagner 100k abonnés en 30 jours ! Abonnez-vous pour plus de conseils !', 'youtube')">
                    Test YouTube
                </button>
                <button class="test-btn" onclick="testContent('Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 'general')">
                    Test Contenu Neutre
                </button>
            </div>
        </div>
    </div>

    <script>
        // Configuration de l'API (pour les tests locaux)
        const API_BASE_URL = 'http://localhost:8000';
        
        // Variables globales
        let isAnalyzing = false;

        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {
            checkBackendStatus();
            setupEventListeners();
        });

        function setupEventListeners() {
            document.getElementById('analyzeForm').addEventListener('submit', handleAnalyze);
        }

        async function checkBackendStatus() {
            try {
                // Vérification du backend principal
                const response = await fetch(`${API_BASE_URL}/`);
                const data = await response.json();
                
                document.getElementById('backendStatus').textContent = '✅ En ligne';
                document.getElementById('backendStatus').style.color = '#38a169';
                
                // Vérification de la santé
                const healthResponse = await fetch(`${API_BASE_URL}/sante`);
                const healthData = await healthResponse.json();
                
                // Statut MongoDB
                const mongoStatus = healthData.mongodb === 'connecté' ? '✅ Connecté' : '❌ Déconnecté';
                document.getElementById('mongoStatus').textContent = mongoStatus;
                document.getElementById('mongoStatus').style.color = healthData.mongodb === 'connecté' ? '#38a169' : '#e53e3e';
                
                // Statut ML
                const mlStatus = healthData.modele_ml === 'entraîné' ? '✅ Entraîné' : '⚠️ Non entraîné';
                document.getElementById('mlStatus').textContent = mlStatus;
                document.getElementById('mlStatus').style.color = healthData.modele_ml === 'entraîné' ? '#38a169' : '#f56500';
                
            } catch (error) {
                console.error('Erreur de connexion au backend:', error);
                document.getElementById('backendStatus').textContent = '❌ Hors ligne';
                document.getElementById('backendStatus').style.color = '#e53e3e';
                document.getElementById('mongoStatus').textContent = '❌ N/A';
                document.getElementById('mongoStatus').style.color = '#e53e3e';
                document.getElementById('mlStatus').textContent = '❌ N/A';
                document.getElementById('mlStatus').style.color = '#e53e3e';
                
                showError('Impossible de se connecter au backend. Assurez-vous que le serveur FastAPI est démarré sur le port 8000.');
            }
        }

        async function handleAnalyze(event) {
            event.preventDefault();
            
            if (isAnalyzing) return;
            
            const contentText = document.getElementById('contentText').value.trim();
            const platform = document.getElementById('platform').value;
            const userId = document.getElementById('userId').value.trim();
            
            if (!contentText) {
                showError('Veuillez entrer du contenu à analyser.');
                return;
            }
            
            await analyzeContent(contentText, platform, userId);
        }

        async function analyzeContent(text, platform, userId = null) {
            if (isAnalyzing) return;
            
            isAnalyzing = true;
            const analyzeBtn = document.getElementById('analyzeBtn');
            analyzeBtn.disabled = true;
            analyzeBtn.textContent = '🔄 Analyse en cours...';
            
            showLoading();
            
            try {
                const requestData = {
                    texte: text,
                    plateforme: platform
                };
                
                if (userId) {
                    requestData.id_utilisateur = userId;
                }
                
                const response = await fetch(`${API_BASE_URL}/analyser`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(requestData)
                });
                
                if (!response.ok) {
                    throw new Error(`Erreur HTTP: ${response.status}`);
                }
                
                const results = await response.json();
                displayResults(results);
                
            } catch (error) {
                console.error('Erreur lors de l\'analyse:', error);
                showError(`Erreur lors de l'analyse: ${error.message}`);
            } finally {
                isAnalyzing = false;
                analyzeBtn.disabled = false;
                analyzeBtn.textContent = '🔍 Analyser le Contenu';
            }
        }

        function showLoading() {
            const resultsContainer = document.getElementById('resultsContainer');
            resultsContainer.innerHTML = `
                <div class="loading">
                    <div class="spinner"></div>
                    <p>Analyse en cours...</p>
                </div>
            `;
        }

        function showError(message) {
            const resultsContainer = document.getElementById('resultsContainer');
            resultsContainer.innerHTML = `
                <div class="error">
                    <strong>Erreur:</strong> ${message}
                </div>
            `;
        }

        function displayResults(results) {
            const resultsContainer = document.getElementById('resultsContainer');
            
            // Formatage des scores
            const viralScore = Math.round(results.score_viral * 10) / 10;
            const sentimentScore = Math.round(results.score_sentiment * 100) / 100;
            const readabilityScore = Math.round(results.score_lisibilite * 10) / 10;
            
            // Couleur du sentiment
            let sentimentColor = '#718096';
            if (sentimentScore > 0.1) sentimentColor = '#38a169';
            else if (sentimentScore < -0.1) sentimentColor = '#e53e3e';
            
            resultsContainer.innerHTML = `
                <div class="results-card">
                    <div class="score-display">
                        <div class="score-item">
                            <div class="score-value viral-score">${viralScore}</div>
                            <div class="score-label">Score Viral</div>
                        </div>
                        <div class="score-item">
                            <div class="score-value sentiment-score" style="color: ${sentimentColor}">${sentimentScore}</div>
                            <div class="score-label">Sentiment</div>
                        </div>
                        <div class="score-item">
                            <div class="score-value readability-score">${readabilityScore}</div>
                            <div class="score-label">Lisibilité</div>
                        </div>
                    </div>
                    
                    <div class="engagement-prediction">
                        <div class="prediction-item">
                            <div class="prediction-value">❤️ ${results.prediction_engagement.likes}</div>
                            <div class="prediction-label">Likes</div>
                        </div>
                        <div class="prediction-item">
                            <div class="prediction-value">🔄 ${results.prediction_engagement.partages}</div>
                            <div class="prediction-label">Partages</div>
                        </div>
                        <div class="prediction-item">
                            <div class="prediction-value">💬 ${results.prediction_engagement.commentaires}</div>
                            <div class="prediction-label">Commentaires</div>
                        </div>
                        <div class="prediction-item">
                            <div class="prediction-value">📊 ${results.prediction_engagement.confiance}%</div>
                            <div class="prediction-label">Confiance</div>
                        </div>
                    </div>
                </div>
                
                ${Array.isArray(results.suggestions_optimisation) && results.suggestions_optimisation.length > 0 ? `
                <div class="results-card">
                    <h4 style="margin-bottom: 15px; color: #2d3748;">💡 Suggestions d'Optimisation</h4>
                    <ul class="suggestions-list">
                        ${results.suggestions_optimisation.map(suggestion => `
                            <li>✨ ${suggestion}</li>
                        `).join('')}
                    </ul>
                </div>
                ` : ''}
                
                <div class="results-card">
                    <h4 style="margin-bottom: 15px; color: #2d3748;">📋 Détails</h4>
                    <p><strong>ID Contenu:</strong> ${results.id_contenu}</p>
                    <p><strong>Plateforme:</strong> ${results.plateforme}</p>
                    <p><strong>Horodatage:</strong> ${new Date(results.horodatage_analyse).toLocaleString('fr-FR')}</p>
                </div>
            `;
        }

        function testContent(text, platform) {
            document.getElementById('contentText').value = text;
            document.getElementById('platform').value = platform;
            document.getElementById('userId').value = 'test-user';
            
            // Analyser automatiquement
            setTimeout(() => {
                analyzeContent(text, platform, 'test-user');
            }, 100);
        }

        // Fonction pour tester la connectivité
        async function testConnectivity() {
            console.log('Test de connectivité...');
            await checkBackendStatus();
        }

        // Rafraîchir le statut toutes les 30 secondes
        setInterval(checkBackendStatus, 30000);
    </script>
</body>
</html>
