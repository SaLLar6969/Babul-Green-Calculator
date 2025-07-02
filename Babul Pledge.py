<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Green Footprint Calculator - Babul Films Society</title>
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
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #2ecc71, #27ae60);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }

        .progress-container {
            background: #f8f9fa;
            padding: 20px;
            border-bottom: 1px solid #e9ecef;
        }

        .progress-bar {
            background: #e9ecef;
            border-radius: 10px;
            height: 12px;
            overflow: hidden;
        }

        .progress-fill {
            background: linear-gradient(90deg, #2ecc71, #27ae60);
            height: 100%;
            width: 0%;
            transition: width 0.3s ease;
            border-radius: 10px;
        }

        .progress-text {
            text-align: center;
            margin-top: 10px;
            font-weight: 600;
            color: #495057;
        }

        .question-container {
            padding: 40px;
            min-height: 400px;
        }

        .question {
            display: none;
            animation: fadeIn 0.5s ease-in;
        }

        .question.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .question h3 {
            font-size: 1.4em;
            color: #2c3e50;
            margin-bottom: 25px;
            line-height: 1.4;
        }

        .options {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .option {
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 12px;
            padding: 18px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1.1em;
        }

        .option:hover {
            background: #e3f2fd;
            border-color: #2196f3;
            transform: translateY(-2px);
        }

        .option.selected {
            background: #e8f5e8;
            border-color: #2ecc71;
            color: #27ae60;
            font-weight: 600;
        }

        .navigation {
            padding: 30px 40px;
            display: flex;
            justify-content: space-between;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
        }

        .btn {
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-primary {
            background: linear-gradient(135deg, #2ecc71, #27ae60);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(46, 204, 113, 0.3);
        }

        .btn-secondary {
            background: #6c757d;
            color: white;
        }

        .btn-secondary:hover {
            background: #5a6268;
            transform: translateY(-2px);
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none !important;
        }

        .results {
            display: none;
            padding: 40px;
            text-align: center;
        }

        .results.active {
            display: block !important;
            animation: fadeIn 0.5s ease-in;
        }

        .co2-score {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
        }

        .co2-score h2 {
            font-size: 3em;
            margin-bottom: 10px;
        }

        .rating {
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            font-size: 1.3em;
            font-weight: 700;
        }

        .rating.excellent { background: #d4edda; color: #155724; }
        .rating.good { background: #d1ecf1; color: #0c5460; }
        .rating.fair { background: #fff3cd; color: #856404; }
        .rating.poor { background: #f8d7da; color: #721c24; }

        .tree-count {
            background: #e8f5e8;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 30px;
            font-size: 1.2em;
            color: #27ae60;
        }

        .tips {
            text-align: left;
            background: #f8f9fa;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
        }

        .tips h3 {
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
        }

        .tips ul {
            list-style: none;
        }

        .tips li {
            padding: 12px 0;
            border-bottom: 1px solid #e9ecef;
            color: #495057;
            line-height: 1.5;
        }

        .tips li:before {
            content: "🌱 ";
            margin-right: 10px;
        }

        .tips li:last-child {
            border-bottom: none;
        }

        .share-btn {
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            margin-top: 20px;
        }

        .share-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(52, 152, 219, 0.3);
        }

        @media (max-width: 768px) {
            .container {
                margin: 0;
                border-radius: 0;
                min-height: 100vh;
            }
            
            .question-container, .navigation {
                padding: 20px;
            }
            
            .header {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌱 Green Footprint Calculator</h1>
            <p>Discover your environmental impact - Babul Films Society</p>
        </div>

        <div class="progress-container">
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill"></div>
            </div>
            <div class="progress-text" id="progressText">Question 1 of 10</div>
        </div>

        <div class="question-container" id="questionContainer">
            <!-- Questions will be generated here -->
        </div>

        <div class="navigation" id="navigation">
            <button class="btn btn-secondary" id="prevBtn" onclick="previousQuestion()">Previous</button>
            <button class="btn btn-primary" id="nextBtn" onclick="nextQuestion()" disabled>Next</button>
        </div>

        <div class="results" id="results">
            <!-- Results will be shown here -->
        </div>
    </div>

    <script>
        const allQuestions = [
            {
                question: "How do you usually get to work or school?",
                options: [
                    { text: "Walk or bike", value: 0 },
                    { text: "Public transport", value: 1 },
                    { text: "Car (shared)", value: 3 },
                    { text: "Car (alone)", value: 5 },
                    { text: "Work from home", value: 0 }
                ]
            },
            {
                question: "How often do you fly for travel?",
                options: [
                    { text: "Never", value: 0 },
                    { text: "Once a year", value: 2 },
                    { text: "2-3 times a year", value: 4 },
                    { text: "More than 3 times", value: 6 }
                ]
            },
            {
                question: "What's your home energy source?",
                options: [
                    { text: "100% renewable energy", value: 0 },
                    { text: "Mostly renewable", value: 1 },
                    { text: "Mixed sources", value: 3 },
                    { text: "Mostly fossil fuels", value: 5 }
                ]
            },
            {
                question: "How much meat do you eat?",
                options: [
                    { text: "Vegetarian/Vegan", value: 0 },
                    { text: "Rarely (1-2 times/week)", value: 1 },
                    { text: "Occasionally (3-4 times/week)", value: 3 },
                    { text: "Daily", value: 5 }
                ]
            },
            {
                question: "How do you handle food waste?",
                options: [
                    { text: "Compost and minimal waste", value: 0 },
                    { text: "Try to minimize waste", value: 1 },
                    { text: "Some food waste", value: 3 },
                    { text: "Significant food waste", value: 5 }
                ]
            },
            {
                question: "What's your shopping style for clothes?",
                options: [
                    { text: "Buy only when needed, second-hand", value: 0 },
                    { text: "Buy occasionally, good quality", value: 1 },
                    { text: "Regular shopping", value: 3 },
                    { text: "Frequent fast fashion", value: 5 }
                ]
            },
            {
                question: "How do you heat/cool your home?",
                options: [
                    { text: "Very efficient system, well-insulated", value: 0 },
                    { text: "Efficient system", value: 1 },
                    { text: "Standard system", value: 3 },
                    { text: "Old, inefficient system", value: 5 }
                ]
            },
            {
                question: "How much do you recycle?",
                options: [
                    { text: "Everything possible", value: 0 },
                    { text: "Most items", value: 1 },
                    { text: "Some items", value: 3 },
                    { text: "Rarely recycle", value: 5 }
                ]
            },
            {
                question: "What's your water usage like?",
                options: [
                    { text: "Very conservative, short showers", value: 0 },
                    { text: "Mindful of usage", value: 1 },
                    { text: "Average usage", value: 3 },
                    { text: "High usage, long showers/baths", value: 5 }
                ]
            },
            {
                question: "How often do you buy new electronics?",
                options: [
                    { text: "Only when broken, repair first", value: 0 },
                    { text: "Every few years when needed", value: 1 },
                    { text: "Every 2-3 years", value: 3 },
                    { text: "Love getting latest gadgets", value: 5 }
                ]
            },
            {
                question: "How do you usually dispose of plastic waste?",
                options: [
                    { text: "Avoid plastic completely", value: 0 },
                    { text: "Recycle all plastic properly", value: 1 },
                    { text: "Some recycling, some trash", value: 3 },
                    { text: "Mostly throw in general trash", value: 5 }
                ]
            },
            {
                question: "What's your approach to buying groceries?",
                options: [
                    { text: "Local farmers market, organic", value: 0 },
                    { text: "Mix of local and supermarket", value: 1 },
                    { text: "Mainly supermarket shopping", value: 3 },
                    { text: "Convenience stores, packaged food", value: 5 }
                ]
            },
            {
                question: "How often do you eat out or order takeaway?",
                options: [
                    { text: "Rarely, mostly home cooking", value: 0 },
                    { text: "Once a week", value: 1 },
                    { text: "2-3 times a week", value: 3 },
                    { text: "Almost daily", value: 5 }
                ]
            },
            {
                question: "What's your car usage pattern?",
                options: [
                    { text: "Don't own a car", value: 0 },
                    { text: "Use only for long trips", value: 1 },
                    { text: "Use for most errands", value: 3 },
                    { text: "Use for everything, even short trips", value: 5 }
                ]
            },
            {
                question: "How do you manage your home's lighting?",
                options: [
                    { text: "LED bulbs, natural light when possible", value: 0 },
                    { text: "Energy-efficient bulbs, mindful usage", value: 1 },
                    { text: "Mix of bulb types, average usage", value: 3 },
                    { text: "Keep lights on, older bulbs", value: 5 }
                ]
            },
            {
                question: "What's your approach to packaging when shopping?",
                options: [
                    { text: "Bring own bags, avoid packaged items", value: 0 },
                    { text: "Reusable bags, minimal packaging", value: 1 },
                    { text: "Sometimes forget bags", value: 3 },
                    { text: "Don't think about packaging", value: 5 }
                ]
            },
            {
                question: "How do you handle household chemicals and cleaners?",
                options: [
                    { text: "Eco-friendly, homemade cleaners", value: 0 },
                    { text: "Green products when possible", value: 1 },
                    { text: "Mix of regular and eco products", value: 3 },
                    { text: "Use whatever's cheapest/strongest", value: 5 }
                ]
            },
            {
                question: "What's your digital consumption like?",
                options: [
                    { text: "Minimal streaming, energy-saving devices", value: 0 },
                    { text: "Moderate usage, turn off when not needed", value: 1 },
                    { text: "Regular streaming and device usage", value: 3 },
                    { text: "Heavy streaming, devices always on", value: 5 }
                ]
            },
            {
                question: "How do you handle yard waste and gardening?",
                options: [
                    { text: "Compost everything, native plants", value: 0 },
                    { text: "Some composting, eco-friendly gardening", value: 1 },
                    { text: "Basic lawn care, some waste disposal", value: 3 },
                    { text: "Heavy fertilizers, all waste to trash", value: 5 }
                ]
            },
            {
                question: "What's your approach to paper usage?",
                options: [
                    { text: "Paperless, digital everything", value: 0 },
                    { text: "Minimal paper, recycle everything", value: 1 },
                    { text: "Moderate paper use, some recycling", value: 3 },
                    { text: "Print freely, don't always recycle", value: 5 }
                ]
            }
        ];

        let questions = [];

        const tips = [
            "Switch to LED bulbs - they use 75% less energy than traditional bulbs",
            "Take shorter showers to save water and energy",
            "Use public transport, walk, or bike instead of driving alone",
            "Eat more plant-based meals - even one day a week makes a difference",
            "Unplug electronics when not in use to avoid phantom energy drain",
            "Buy local and seasonal produce to reduce transportation emissions",
            "Use reusable bags, water bottles, and containers",
            "Set your thermostat 2°C lower in winter and higher in summer",
            "Air-dry clothes instead of using the dryer when possible",
            "Choose quality items that last longer over cheap disposables",
            "Start composting food scraps to reduce methane emissions",
            "Use cold water for washing clothes - it saves energy",
            "Plant trees or support reforestation projects in your area",
            "Choose renewable energy options if available in your area",
            "Reduce food waste by meal planning and proper storage"
        ];

        let currentQuestion = 0;
        let answers = [];
        let totalScore = 0;

        function initializeQuiz() {
            // Shuffle all questions and select 10 random ones
            const shuffled = [...allQuestions].sort(() => 0.5 - Math.random());
            questions = shuffled.slice(0, 10);
            
            showQuestion(0);
            updateProgress();
        }

        function showQuestion(index) {
            const container = document.getElementById('questionContainer');
            container.innerHTML = `
                <div class="question active">
                    <h3>${questions[index].question}</h3>
                    <div class="options">
                        ${questions[index].options.map((option, i) => `
                            <div class="option" onclick="selectOption(${i}, ${option.value})" id="option-${i}">
                                ${option.text}
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;

            // Pre-select if answer exists
            if (answers[index] !== undefined) {
                const selectedIndex = questions[index].options.findIndex(opt => opt.value === answers[index]);
                if (selectedIndex !== -1) {
                    document.getElementById(`option-${selectedIndex}`).classList.add('selected');
                    document.getElementById('nextBtn').disabled = false;
                }
            }

            updateNavigation();
        }

        function selectOption(optionIndex, value) {
            // Remove previous selection
            document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
            
            // Add selection to clicked option
            document.getElementById(`option-${optionIndex}`).classList.add('selected');
            
            // Store answer
            answers[currentQuestion] = value;
            
            // Enable next button
            document.getElementById('nextBtn').disabled = false;
        }

        function nextQuestion() {
            console.log('Next question clicked. Current:', currentQuestion, 'Total questions:', questions.length);
            console.log('Answers so far:', answers);
            
            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                showQuestion(currentQuestion);
                updateProgress();
            } else {
                console.log('Quiz complete, showing results...');
                showResults();
            }
        }

        function previousQuestion() {
            if (currentQuestion > 0) {
                currentQuestion--;
                showQuestion(currentQuestion);
                updateProgress();
            }
        }

        function updateProgress() {
            const progress = ((currentQuestion + 1) / questions.length) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
            document.getElementById('progressText').textContent = `Question ${currentQuestion + 1} of ${questions.length}`;
        }

        function updateNavigation() {
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            
            prevBtn.style.display = currentQuestion === 0 ? 'none' : 'block';
            nextBtn.textContent = currentQuestion === questions.length - 1 ? 'See Results' : 'Next';
            nextBtn.disabled = answers[currentQuestion] === undefined;
        }

        function calculateScore() {
            totalScore = answers.reduce((sum, answer) => sum + answer, 0);
            return totalScore;
        }

        function getRating(score) {
            if (score <= 10) return { rating: 'Excellent', class: 'excellent', message: 'Outstanding! You\'re living very sustainably!' };
            if (score <= 20) return { rating: 'Good', class: 'good', message: 'Great job! You\'re making a positive environmental impact!' };
            if (score <= 35) return { rating: 'Fair', class: 'fair', message: 'You\'re on the right track, but there\'s room for improvement!' };
            return { rating: 'Poor', class: 'poor', message: 'There\'s significant opportunity to reduce your environmental impact!' };
        }

        function getRandomTips() {
            const shuffled = tips.sort(() => 0.5 - Math.random());
            return shuffled.slice(0, 5);
        }

        function showResults() {
            console.log('Showing results...'); // Debug log
            
            const score = calculateScore();
            const co2Tons = (score * 0.8 + 2).toFixed(1); // Rough calculation
            const rating = getRating(score);
            const treesNeeded = Math.ceil(co2Tons * 16); // Roughly 16 trees per ton of CO2
            const randomTips = getRandomTips();

            console.log('Score:', score, 'CO2:', co2Tons, 'Rating:', rating); // Debug log

            // Hide quiz elements
            const questionContainer = document.getElementById('questionContainer');
            const navigation = document.getElementById('navigation');
            const progressContainer = document.getElementById('progressContainer');
            const resultsContainer = document.getElementById('results');

            if (questionContainer) questionContainer.style.display = 'none';
            if (navigation) navigation.style.display = 'none';
            if (progressContainer) progressContainer.style.display = 'none';

            // Show results
            if (resultsContainer) {
                resultsContainer.innerHTML = `
                    <div class="co2-score">
                        <h2>${co2Tons}</h2>
                        <p>Tons of CO₂ per year</p>
                    </div>

                    <div class="rating ${rating.class}">
                        <strong>${rating.rating}</strong><br>
                        ${rating.message}
                    </div>

                    <div class="tree-count">
                        <strong>🌳 ${treesNeeded} trees</strong><br>
                        needed to offset your annual carbon footprint
                    </div>

                    <div class="tips">
                        <h3>💡 Personalized Tips for You</h3>
                        <ul>
                            ${randomTips.map(tip => `<li>${tip}</li>`).join('')}
                        </ul>
                    </div>

                    <button class="btn btn-primary share-btn" onclick="shareResults()">Share My Results</button>
                    <button class="btn btn-secondary" onclick="restartQuiz()" style="margin-left: 10px;">Take Again</button>
                `;

                resultsContainer.style.display = 'block';
                resultsContainer.classList.add('active');
                
                console.log('Results should now be visible'); // Debug log
            } else {
                console.error('Results container not found!');
            }
        }

        function shareResults() {
            const score = calculateScore();
            const co2Tons = (score * 0.8 + 2).toFixed(1);
            const rating = getRating(score);
            
            const shareText = `I just calculated my carbon footprint! 🌱\n\n` +
                            `My annual CO₂ emissions: ${co2Tons} tons\n` +
                            `Rating: ${rating.rating}\n\n` +
                            `Calculate yours with Babul Films Society's Green Footprint Calculator!`;

            if (navigator.share) {
                navigator.share({
                    title: 'My Green Footprint Results',
                    text: shareText
                });
            } else {
                navigator.clipboard.writeText(shareText).then(() => {
                    alert('Results copied to clipboard! Share it with your friends!');
                });
            }
        }

        function restartQuiz() {
            currentQuestion = 0;
            answers = [];
            totalScore = 0;
            
            document.getElementById('questionContainer').style.display = 'block';
            document.getElementById('navigation').style.display = 'flex';
            document.getElementById('progressContainer').style.display = 'block';
            document.getElementById('results').classList.remove('active');
            
            initializeQuiz();
        }

        // Initialize the quiz when page loads
        window.onload = function() {
            initializeQuiz();
        };
    </script>

    <footer style="text-align: center; padding: 20px; background: #2c3e50; color: white; font-size: 0.9em;">
        <p>Created with ❤️ by <strong>Raja Vardhan D</strong></p>
        <p style="margin-top: 5px; opacity: 0.8;">Green Footprint Calculator - Babul Films Society</p>
    </footer>
</body>
</html>