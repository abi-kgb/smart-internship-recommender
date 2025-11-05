from flask import Flask, render_template_string, request

app = Flask(__name__)

# ----------- DATA: INTERNSHIP, PROJECTS, LANGUAGES & CERTIFICATIONS -----------
recommendations = {
    "web": {
        "bg": "https://img.freepik.com/free-photo/website-design-concept-with-laptop_23-2149402751.jpg",
        "languages": ["HTML", "CSS", "JavaScript", "Python (Flask/Django)"],
        "certifications": [
            {"name": "W3Schools Web Development", "link": "https://www.w3schools.com/cert/default.asp"},
            {"name": "freeCodeCamp Responsive Web Design", "link": "https://www.freecodecamp.org/learn/"}
        ],
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
    "ai": {
        "bg": "https://img.freepik.com/free-photo/futuristic-artificial-intelligence-concept_23-2151701650.jpg",
        "languages": ["Python", "R"],
        "certifications": [
            {"name": "IBM AI Engineering Certificate", "link": "https://www.coursera.org/professional-certificates/ai-engineer"},
            {"name": "Google AI Fundamentals", "link": "https://developers.google.com/machine-learning/crash-course"}
        ],
        "internships": ["AI Research Intern", "ML Assistant Intern"],
        "projects": {
            "Beginner": [
                {"title": "Image Classification using CNN", "link": "https://www.tensorflow.org/tutorials"},
                {"title": "Chatbot using Python", "link": "https://www.geeksforgeeks.org/python-chatbot-tutorial/"},
            ],
            "Intermediate": [
                {"title": "Face Recognition System", "link": "https://realpython.com/face-recognition-with-python/"},
                {"title": "Text Sentiment Analysis", "link": "https://towardsdatascience.com/sentiment-analysis-python-tutorial-6c36a3a34d4c"},
            ],
            "Expert": [
                {"title": "AI-based Fraud Detection", "link": "https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud"},
                {"title": "Autonomous Vehicle Simulation", "link": "https://carla.org/"},
            ],
        }
    },
    "cloud": {
        "bg": "https://img.freepik.com/free-photo/futuristic-server-room-with-blue-lights_23-2148320284.jpg",
        "languages": ["Python", "Java", "Bash", "YAML"],
        "certifications": [
            {"name": "AWS Cloud Practitioner", "link": "https://aws.amazon.com/certification/certified-cloud-practitioner/"},
            {"name": "Google Cloud Fundamentals", "link": "https://www.coursera.org/learn/gcp-fundamentals"}
        ],
        "internships": ["Cloud Engineer Intern", "AWS Trainee", "Azure DevOps Intern"],
        "projects": {
            "Beginner": [
                {"title": "Deploy Flask App on AWS", "link": "https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html"},
                {"title": "Cloud File Storage System", "link": "https://aws.amazon.com/s3/"},
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
        "bg": "https://img.freepik.com/free-photo/cyber-security-lock-padlock-icon-protection_53876-119585.jpg",
        "languages": ["Python", "C", "C++", "Bash"],
        "certifications": [
            {"name": "EC-Council Ethical Hacking", "link": "https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/"},
            {"name": "Google Cybersecurity Professional Certificate", "link": "https://www.coursera.org/professional-certificates/google-cybersecurity"}
        ],
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
    }
}

# ----------- TEMPLATE WITH DYNAMIC BACKGROUND -----------
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Smart Internship & Project Recommender</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('{{ bg }}');
      background-size: cover;
      background-attachment: fixed;
      background-position: center;
      color: white;
      font-family: 'Poppins', sans-serif;
    }
    .container {
      background-color: rgba(0, 0, 0, 0.7);
      border-radius: 20px;
      padding: 30px;
      margin-top: 40px;
    }
    h1, h2, h3 {
      text-align: center;
    }
    a { color: #ffcc70; text-decoration: none; }
    .card {
      background-color: rgba(255,255,255,0.1);
      border: none;
      color: white;
    }
    .btn {
      background-color: #ffb347;
      color: black;
      border: none;
    }
    select {
      border-radius: 8px;
      padding: 8px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🚀 Smart Internship & Project Recommender</h1>
    <form method="POST">
      <div class="text-center mt-4">
        <label>Select Domain: </label>
        <select name="domain">
          <option value="ai">AI & ML</option>
          <option value="cloud">Cloud Computing</option>
          <option value="cybersecurity">Cybersecurity</option>
          <option value="web">Web Development</option>
        </select>
        <button class="btn btn-warning btn-sm" type="submit">Recommend</button>
      </div>
    </form>

    {% if data %}
    <hr>
    <h2>{{ domain.upper() }} Recommendations</h2>
    <h3>Languages to Learn:</h3>
    <ul>{% for lang in data.languages %}<li>{{ lang }}</li>{% endfor %}</ul>

    <h3>Internship Roles:</h3>
    <ul>{% for role in data.internships %}<li>{{ role }}</li>{% endfor %}</ul>

    <h3>Certifications:</h3>
    <div class="row">
      {% for cert in data.certifications %}
      <div class="col-md-6">
        <div class="card p-3 mb-2">
          <a href="{{ cert.link }}" target="_blank">{{ cert.name }}</a>
        </div>
      </div>
      {% endfor %}
    </div>

    <h3>Project Ideas by Level:</h3>
    {% for level, projects in data.projects.items() %}
      <h4>{{ level }} Projects:</h4>
      <ul>
      {% for project in projects %}
        <li><a href="{{ project.link }}" target="_blank">{{ project.title }}</a></li>
      {% endfor %}
      </ul>
    {% endfor %}
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    domain = None
    data = None
    bg = "https://img.freepik.com/free-photo/abstract-network-background_53476-10026.jpg"
    if request.method == "POST":
        domain = request.form["domain"]
        data = recommendations.get(domain)
        bg = data["bg"]
    return render_template_string(TEMPLATE, data=data, domain=domain, bg=bg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
