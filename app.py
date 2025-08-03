from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# HTML template with dark, masculine styling
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Kubernetes GitOps Pipeline</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Courier New', 'Monaco', 'Menlo', monospace;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            color: #e0e0e0;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            border: 1px solid #333;
            backdrop-filter: blur(10px);
        }

        .title {
            font-size: 3rem;
            font-weight: bold;
            background: linear-gradient(45deg, #00d4ff, #0099cc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        }

        .subtitle {
            font-size: 1.2rem;
            color: #888;
            margin-bottom: 1rem;
        }

        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.5);
            padding: 1rem 2rem;
            border-radius: 10px;
            border: 1px solid #333;
            margin-bottom: 2rem;
        }

        .status-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #00ff00;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .content-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .card {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid #333;
            border-radius: 10px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00d4ff, #0099cc);
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.2);
            border-color: #00d4ff;
        }

        .card-title {
            font-size: 1.5rem;
            font-weight: bold;
            color: #00d4ff;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .card-content {
            line-height: 1.6;
            color: #ccc;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .tech-tag {
            background: linear-gradient(45deg, #333, #555);
            color: #00d4ff;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
            border: 1px solid #00d4ff;
        }

        .terminal {
            background: #000;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            font-family: 'Courier New', monospace;
            color: #00ff00;
            overflow-x: auto;
        }

        .command {
            color: #00d4ff;
        }

        .output {
            color: #888;
        }

        .cta-section {
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            border: 1px solid #333;
        }

        .btn {
            background: linear-gradient(45deg, #00d4ff, #0099cc);
            color: #000;
            padding: 1rem 2rem;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            margin: 0.5rem;
            font-family: 'Courier New', monospace;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0, 212, 255, 0.4);
        }

        .footer {
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            color: #666;
            border-top: 1px solid #333;
        }

        .matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            opacity: 0.1;
            z-index: -1;
        }

        .matrix-char {
            position: absolute;
            color: #00ff00;
            font-size: 1rem;
            animation: fall 3s linear infinite;
        }

        @keyframes fall {
            to {
                transform: translateY(100vh);
            }
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            .title {
                font-size: 2rem;
            }
            
            .content-grid {
                grid-template-columns: 1fr;
            }
            
            .status-bar {
                flex-direction: column;
                gap: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="matrix-bg" id="matrix"></div>
    
    <div class="container">
        <div class="header">
            <h1 class="title">🚀 Kubernetes GitOps Pipeline</h1>
            <p class="subtitle">Jenkins CI + ArgoCD CD + Kubernetes Deployment</p>
        </div>

        <div class="status-bar">
            <div class="status-item">
                <div class="status-indicator"></div>
                <span>Jenkins: Running</span>
            </div>
            <div class="status-item">
                <div class="status-indicator"></div>
                <span>ArgoCD: Active</span>
            </div>
            <div class="status-item">
                <div class="status-indicator"></div>
                <span>Kubernetes: Healthy</span>
            </div>
            <div class="status-item">
                <span>🕐 {{ current_time }}</span>
            </div>
        </div>

        <div class="content-grid">
            <div class="card">
                <h3 class="card-title">🔧 What This Does</h3>
                <div class="card-content">
                    <p>This repository creates a complete Jenkins pipeline with GitOps to deploy code into a Kubernetes cluster.</p>
                    <ul style="margin-top: 1rem; padding-left: 1.5rem;">
                        <li><strong>CI:</strong> Jenkins handles Continuous Integration</li>
                        <li><strong>CD:</strong> ArgoCD manages Continuous Deployment</li>
                        <li><strong>GitOps:</strong> Infrastructure as Code approach</li>
                        <li><strong>Kubernetes:</strong> Container orchestration platform</li>
                    </ul>
                    <div class="tech-stack">
                        <span class="tech-tag">Jenkins</span>
                        <span class="tech-tag">ArgoCD</span>
                        <span class="tech-tag">Kubernetes</span>
                        <span class="tech-tag">GitOps</span>
                    </div>
                </div>
            </div>

            <div class="card">
                <h3 class="card-title">⚙️ Jenkins Setup</h3>
                <div class="card-content">
                    <p>Jenkins is installed on EC2 with the following components:</p>
                    <div class="terminal">
                        <div class="command"># Install Jenkins on EC2</div>
                        <div class="output">sudo yum install jenkins java-1.8.0-openjdk-devel -y</div>
                        <div class="command"># Install Docker</div>
                        <div class="output">sudo yum install docker -y</div>
                        <div class="command"># Configure permissions</div>
                        <div class="output">sudo chmod 666 /var/run/docker.sock</div>
                    </div>
                    <p><strong>Required Plugins:</strong></p>
                    <ul style="margin-top: 0.5rem; padding-left: 1.5rem;">
                        <li>Amazon EC2 plugin</li>
                        <li>Docker plugin</li>
                        <li>GitHub Integration Plugin</li>
                        <li>Parameterized trigger Plugin</li>
                    </ul>
                </div>
            </div>

            <div class="card">
                <h3 class="card-title">🎯 ArgoCD Installation</h3>
                <div class="card-content">
                    <p>ArgoCD is installed in your Kubernetes cluster for GitOps workflow:</p>
                    <div class="terminal">
                        <div class="command"># Install ArgoCD</div>
                        <div class="output">kubectl create namespace argocd</div>
                        <div class="output">kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml</div>
                    </div>
                    <p>ArgoCD provides:</p>
                    <ul style="margin-top: 0.5rem; padding-left: 1.5rem;">
                        <li>Declarative GitOps</li>
                        <li>Automated deployments</li>
                        <li>Rollback capabilities</li>
                        <li>Multi-cluster management</li>
                    </ul>
                </div>
            </div>

            <div class="card">
                <h3 class="card-title">📚 Learning Resources</h3>
                <div class="card-content">
                    <p>Follow along with the Udemy Kubernetes course lectures (GitOps Chapter) to understand:</p>
                    <ul style="margin-top: 1rem; padding-left: 1.5rem;">
                        <li>Detailed setup instructions</li>
                        <li>Step-by-step demo</li>
                        <li>Best practices</li>
                        <li>Real-world implementation</li>
                    </ul>
                    <p style="margin-top: 1rem;"><strong>Course:</strong> Highest rated Kubernetes EKS course</p>
                    <p><strong>Website:</strong> www.cloudwithraj.com</p>
                </div>
            </div>
        </div>

        <div class="cta-section">
            <h3 style="color: #00d4ff; margin-bottom: 1rem;">🚀 Ready to Deploy?</h3>
            <p style="margin-bottom: 2rem;">Start your GitOps journey with Jenkins and ArgoCD</p>
            <button class="btn" onclick="showDeployMessage()">🚀 Deploy Pipeline</button>
            <button class="btn" onclick="showCourseMessage()">📖 View Course</button>
        </div>

        <div class="footer">
            <p>Built with ❤️ using Flask & Modern Web Technologies</p>
            <p>Last updated: {{ current_date }}</p>
            <p>Pipeline Status: <span style="color: #00ff00;">●</span> Active</p>
        </div>
    </div>

    <script>
        function showDeployMessage() {
            alert('🚀 Pipeline deployment initiated!\n\nJenkins → ArgoCD → Kubernetes');
        }

        function showCourseMessage() {
            alert('📚 Check out the Udemy course at www.cloudwithraj.com\n\nLearn GitOps with Jenkins and ArgoCD!');
        }

        // Matrix background effect
        function createMatrixEffect() {
            const matrix = document.getElementById('matrix');
            const chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
            
            for (let i = 0; i < 50; i++) {
                const char = document.createElement('div');
                char.className = 'matrix-char';
                char.textContent = chars[Math.floor(Math.random() * chars.length)];
                char.style.left = Math.random() * 100 + '%';
                char.style.animationDelay = Math.random() * 3 + 's';
                char.style.animationDuration = (Math.random() * 3 + 2) + 's';
                matrix.appendChild(char);
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            createMatrixEffect();
            
            // Add hover effects to cards
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-5px) scale(1.02)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0) scale(1)';
                });
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
    
    return render_template_string(HTML_TEMPLATE, 
                                current_time=current_time,
                                current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
