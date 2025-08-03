from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# HTML template with modern styling
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌟 Stylish Flask App</title>
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
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 3rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 600px;
            width: 90%;
            animation: fadeInUp 0.8s ease-out;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .title {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .subtitle {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 2rem;
            font-weight: 300;
        }

        .message {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #555;
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(240, 147, 251, 0.3);
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }

        .stat-card {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #666;
            margin-top: 0.5rem;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 2rem;
        }

        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: linear-gradient(45deg, #f093fb, #f5576c);
            color: white;
            box-shadow: 0 8px 25px rgba(240, 147, 251, 0.3);
        }

        .btn-secondary:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(240, 147, 251, 0.4);
        }

        .footer {
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #888;
        }

        .emoji {
            font-size: 1.5rem;
            margin: 0 0.5rem;
        }

        @media (max-width: 768px) {
            .container {
                padding: 2rem;
            }
            
            .title {
                font-size: 2rem;
            }
            
            .cta-buttons {
                flex-direction: column;
                align-items: center;
            }
            
            .btn {
                width: 100%;
                max-width: 250px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">🌟 Welcome to My Stylish App! 🚀</h1>
        <p class="subtitle">Built with Flask & Modern Web Design</p>
        
        <div class="message">
            <span class="emoji">💖</span>
            Please subscribe, like, and comment on this video! 
            <span class="emoji">💖</span>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{{ visitor_count }}</div>
                <div class="stat-label">Visitors Today</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ current_time }}</div>
                <div class="stat-label">Current Time</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">100%</div>
                <div class="stat-label">Stylish Design</div>
            </div>
        </div>

        <div class="cta-buttons">
            <button class="btn btn-primary" onclick="showMessage()">
                <span class="emoji">👍</span> Like This App
            </button>
            <button class="btn btn-secondary" onclick="showMessage()">
                <span class="emoji">💬</span> Leave a Comment
            </button>
        </div>

        <div class="footer">
            <p>Made with ❤️ using Flask & Modern CSS</p>
            <p>Last updated: {{ current_date }}</p>
        </div>
    </div>

    <script>
        function showMessage() {
            alert('Thank you for your support! 🙏✨');
        }

        // Add some interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.stat-card');
            cards.forEach((card, index) => {
                card.style.animationDelay = `${index * 0.1}s`;
                card.style.animation = 'fadeInUp 0.8s ease-out forwards';
            });
        });
    </script>
</body>
</html>
'''

@app.route('/')
def hello_world():
    # Get current time and date
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%B %d, %Y")
    
    # Simple visitor counter (in a real app, you'd use a database)
    visitor_count = 42  # This would normally come from a database
    
    return render_template_string(HTML_TEMPLATE, 
                                visitor_count=visitor_count,
                                current_time=current_time,
                                current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
