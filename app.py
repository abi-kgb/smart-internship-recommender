from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# ----------- DATA: INTERNSHIP & PROJECT RECOMMENDATIONS -----------
recommendations = {
    "web": {
        "internships": ["Frontend Developer Intern", "Web Design Intern", "Full Stack Developer Intern"],
        "projects": {
            "Beginner": [
                {"title": "Personal Portfolio Website", "link": "https://www.w3schools.com/html/"},
                {"title": "Simple Blog Site", "link": "https://flask.palletsprojects.com/en/3.0.x/tutorial/"},
            ],
            "Intermediate": [
                {"title": "College Event Management System", "link": "https://www.geeksforgeeks.org/flask-tutorial/"},
                {"title": "E-commerce Website", "link": "https://realpython.com/flask-by-example-part-1-project-setup/"},
            ],
            "Expert": [
                {"title": "AI-based Content Generator", "link": "https://openai.com/blog/chatgpt"},
                {"title": "Social Media Automation Platform", "link": "https://developers.facebook.com/docs/graph-api"},
            ],
        }
    },
    "data": {
        "internships": ["Data Analyst Intern", "Business Intelligence Intern", "ML Assistant Intern"],
        "projects": {
            "Beginner": [
                {"title": "Data Visualization Dashboard", "link": "https://matplotlib.org/stable/gallery/index.html"},
                {"title": "Student Result Analysis", "link": "https://pandas.pydata.org/docs/getting_started/index.html"},
            ],
            "Intermediate": [
                {"title": "Movie Recommendation System", "link": "https://realpython.com/build-recommendation-engine-collaborative-filtering/"},
                {"title": "Data Cleaning Automation", "link": "https://towardsdatascience.com/data-cleaning-101-4d429e29f9e4"},
            ],
            "Expert": [
                {"title": "Predictive Analytics System", "link": "https://scikit-learn.org/stable/supervised_learning.html"},
                {"title": "AI-driven Customer Insights", "link": "https://cloud.google.com/ai"},
            ],
        }
    },
    "cloud": {
        "internships": ["Cloud Engineer Intern", "AWS Trainee", "Azure DevOps Intern"],
        "projects": {
            "Beginner": [
                {"title": "Cloud File Storage System", "link": "https://aws.amazon.com/s3/"},
                {"title": "Deploy Flask App on AWS", "link": "https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html"},
            ],
            "Intermediate": [
                {"title": "Multi-cloud Backup System", "link": "https://learn.microsoft.com/en-us/azure/"},
                {"title": "Serverless API using AWS Lambda", "link": "https://aws.amazon.com/lambda/"},
            ],
            "Expert": [
                {"title": "Cloud Security Monitoring System", "link": "https://cloud.google.com/security"},
                {"title": "Kubernetes-based Microservice App", "link": "https://kubernetes.io/docs/tutorials/"},
            ],
        }
    },
    "cybersecurity": {
        "internships": ["Network Security Intern", "Ethical Hacking Intern"],
        "projects": {
            "Beginner": [
                {"title": "Password Strength Checker", "link": "https://www.geeksforgeeks.org/password-strength-checker-in-python/"},
                {"title": "Simple Encryption Tool", "link": "https://pypi.org/project/cryptography/"},
            ],
            "Intermediate": [
                {"title": "Vulnerability Scanner", "link": "https://owasp.org/www-project-web-security-testing-guide/"},
                {"title": "Network Packet Analyzer", "link": "https://scapy.readthedocs.io/en/latest/"},
            ],
            "Expert": [
                {"title": "Intrusion Detection System", "link": "https://github.com/AI-IDS"},
                {"title": "Penetration Testing Automation", "link": "https://www.kali.org/tools/metasploit-framework/"},
            ],
        }
    },
    "gamedev": {
        "internships": ["Unity Developer Intern", "Game Designer Intern"],
        "projects": {
            "Beginner": [
                {"title": "Snake Game in Python", "link": "https://www.geeksforgeeks.org/snake-game-in-python-using-pygame/"},
                {"title": "Flappy Bird Clone", "link": "https://github.com/sourabhv/FlapPyBird"},
            ],
            "Intermediate": [
                {"title": "2D Platformer Game", "link": "https://realpython.com/pygame-a-primer/"},
                {"title": "Multiplayer Game with Python Sockets", "link": "https://www.geeksforgeeks.org/socket-programming-python/"},
            ],
            "Expert": [
                {"title": "3D Shooter Game using Unity", "link": "https://learn.unity.com/"},
                {"title": "AI-driven Game Bot", "link": "https://www.tensorflow.org/agents"},
            ],
        }
    },
    "uiux": {
        "internships": ["UI Designer Intern", "UX Research Intern"],
        "projects": {
            "Beginner": [
                {"title": "Landing Page Prototype", "link": "https://www.figma.com/templates/"},
                {"title": "Portfolio Website UI", "link": "https://dribbble.com/tags/portfolio"},
            ],
            "Intermediate": [
                {"title": "Mobile App Wireframe Design", "link": "https://www.figma.com/"},
                {"title": "Dark Mode Web UI", "link": "https://getbootstrap.com/docs/5.3/customize/color-modes/"},
            ],
            "Expert": [
                {"title": "Design System Library", "link": "https://mui.com/material-ui/getting-started/overview/"},
                {"title": "UX Redesign for Existing App", "link": "https://www.nngroup.com/articles/ux-case-studies/"},
            ],
        }
    },
    "devops": {
        "internships": ["DevOps Intern", "Automation Engineer Intern"],
        "projects": {
            "Beginner": [
                {"title": "CI/CD Pipeline Setup", "link": "https://github.com/features/actions"},
                {"title": "Dockerized Flask App", "link": "https://docs.docker.com/get-started/"},
            ],
            "Intermediate": [
                {"title": "Kubernetes Deployment", "link": "https://kubernetes.io/docs/tutorials/"},
                {"title": "Monitoring with Prometheus", "link": "https://prometheus.io/docs/introduction/overview/"},
            ],
            "Expert": [
                {"title": "Infrastructure as Code using Terraform", "link": "https://developer.hashicorp.com/terraform/docs"},
                {"title": "Jenkins CI Pipeline", "link": "https://www.jenkins.io/doc/book/pipeline/"},
            ],
        }
    },
    "robotics": {
        "internships": ["Robotics Intern", "Embedded Systems Trainee"],
        "projects": {
            "Beginner": [
                {"title": "Line Following Robot", "link": "https://www.instructables.com/Line-Following-Robot/"},
                {"title": "Obstacle Avoidance Bot", "link": "https://create.arduino.cc/projecthub/"},
            ],
            "Intermediate": [
                {"title": "Voice Controlled Robot", "link": "https://www.hackster.io/"},
                {"title": "Gesture Controlled Car", "link": "https://www.electronicshub.org/gesture-controlled-robot/"},
            ],
            "Expert": [
                {"title": "AI-based Navigation Robot", "link": "https://ros.org/"},
                {"title": "Humanoid Robot using Raspberry Pi", "link": "https://www.raspberrypi.org/"},
            ],
        }
    }
}

# ----------- TEMPLATE -----------
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Smart Internship & Project Recommender</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {font-family: 'Poppins', sans-serif; background: linear-gradient(135deg,#74ebd5,#ACB6E5); min-height: 100vh; padding: 2rem;}
    .card {border-radius: 20px; box-shadow: 0 5px 20px rgba(0,0,0,0.2); padding: 2rem; background: #fff;}
    .title {color:#2b5876; font-weight:700;}
    a {text-decoration:none;}
    a:hover {text-decoration:underline;}
  </style>
</head>
<body>

<div class="container mt-4">
  <div class="card">
    <h1 class="text-center title">Smart Internship & Project Recommender</h1>
    <p class="text-center text-muted">Enter your area of interest below (e.g., AI, Cloud, Cybersecurity, DevOps, Robotics...)</p>

    <form method="POST" class="mb-4">
      <div class="input-group input-group-lg">
        <input type="text" name="skills" class="form-control" placeholder="Enter domain name..." required>
        <button class="btn btn-primary">Recommend</button>
      </div>
    </form>

    {% if recs %}
      <h3 class="text-success mt-4">Recommended Internships</h3>
      <ul>{% for i in recs['internships'] %}<li>🌟 {{ i }}</li>{% endfor %}</ul>
      
      <h3 class="text-info mt-4">Project Ideas</h3>
      {% for level, plist in recs['projects'].items() %}
        <h5 class="mt-3">{{ level }} Level</h5>
        <ul>
          {% for p in plist %}
            <li>💡 <a href="{{ p.link }}" target="_blank">{{ p.title }}</a></li>
          {% endfor %}
        </ul>
      {% endfor %}
    {% elif not first %}
      <div class="alert alert-warning mt-3">
        No matching recommendations found 😕. Try using keywords like <b>web</b>, <b>ai</b>, <b>cloud</b>, <b>data</b>, <b>robotics</b>.
      </div>
    {% endif %}
  </div>
</div>
</body>
</html>
"""

# ----------- ROUTE -----------
@app.route("/", methods=["GET", "POST"])
def index():
    recs = None
    first = True
    if request.method == "POST":
        skills = request.form.get("skills", "").lower()
        first = False
        for key, val in recommendations.items():
            if key in skills:
                recs = val
                break
    return render_template_string(TEMPLATE, recs=recs, first=first)

# ----------- RUN -----------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
