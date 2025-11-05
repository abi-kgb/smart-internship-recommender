from flask import Flask, render_template_string, request

app = Flask(__name__)

# ----------- DATA: INTERNSHIP, PROJECTS, LANGUAGES & CERTIFICATIONS -----------
recommendations = {
    "web": {
        "bg": "https://static.vecteezy.com/system/resources/previews/000/523/309/original/web-development-and-programming-coding-concept-seo-optimization-modern-web-design-on-laptop-screen-vector.jpg",
        "gif": "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
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
        "bg": "https://en.sepoin.com/wp-content/uploads/2020/01/AI-ML-4.jpg",
        "gif": "https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif",
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
        "bg": "https://cdn.pixabay.com/photo/2024/01/26/08/07/ai-generated-8533603_1280.jpg",
        "gif": "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif",
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
        "bg": "https://images.wallpapersden.com/image/download/cybersecurity-core_bmdrZ2mUmZqaraWkpJRmbmdsrWZlbWU.jpg",
        "gif": "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif",
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
    },
    "devops": {
        "bg": "https://www.tekcent.com/media/yncjty2t/devops-1600x900-1423173157.jpg",
        "gif": "https://media.giphy.com/media/fwbzI2kV3Qrlpkh59e/giphy.gif",
        "languages": ["Python", "Bash", "YAML", "Dockerfile", "Groovy (Jenkins)"],
        "certifications": [
            {"name": "Docker & Kubernetes Certification", "link": "https://www.coursera.org/specializations/docker-kubernetes"},
            {"name": "AWS DevOps Engineer", "link": "https://aws.amazon.com/certification/certified-devops-engineer-professional/"}
        ],
        "internships": ["DevOps Intern", "Automation Engineer Intern", "CI/CD Intern"],
        "projects": {
            "Beginner": [
                {"title": "CI/CD Pipeline with GitHub Actions", "link": "https://docs.github.com/en/actions"},
                {"title": "Dockerized Flask App", "link": "https://docs.docker.com/get-started/"},
            ],
            "Intermediate": [
                {"title": "Kubernetes Deployment", "link": "https://kubernetes.io/docs/tutorials/"},
                {"title": "Monitoring with Prometheus and Grafana", "link": "https://prometheus.io/docs/introduction/overview/"},
            ],
            "Expert": [
                {"title": "Infrastructure as Code using Terraform", "link": "https://developer.hashicorp.com/terraform/docs"},
                {"title": "Jenkins CI/CD Pipeline Automation", "link": "https://www.jenkins.io/doc/book/pipeline/"},
            ],
        }
    }
}

# ----------- HTML TEMPLATE -----------
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Smart Internship & Project Recommender</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
  body {
    background: url('{{ bg }}') no-repeat center center fixed;
    background-size: cover;
    color: white;
    font-family: 'Poppins', sans-serif;
  }
  .overlay {
    background: rgba(0,0,0,0.75);
    min-height: 100vh;
    padding: 40px;
  }
  h1 {
    text-align: center;
    color: #ffb347;
    font-weight: bold;
    text-shadow: 0 0 10px #ffb347, 0 0 20px #ffcc70;
    animation: glow 2s infinite alternate;
  }
  @keyframes glow {
    from {text-shadow: 0 0 5px #ffcc70;}
    to {text-shadow: 0 0 20px #ffd700;}
  }
  .gif {
    display: block;
    margin: 20px auto;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(255,255,255,0.4);
  }
  a { color: #ffcc70; text-decoration: none; }
  a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="overlay container rounded">
  <h1>🚀 Smart Internship & Project Recommender</h1>
  <form method="POST" class="text-center mt-4">
    <label>Select Domain: </label>
    <select name="domain" class="form-select d-inline w-auto" required>
      <option value="">-- Choose Domain --</option>
      <option value="ai">AI & ML</option>
      <option value="cloud">Cloud Computing</option>
      <option value="cybersecurity">Cybersecurity</option>
      <option value="web">Web Development</option>
      <option value="devops">DevOps</option>
    </select>
    <button class="btn btn-warning ms-2" type="submit">Recommend</button>
  </form>

  {% if data %}
  <hr>
  <img src="{{ data.gif }}" width="400" class="gif">
  <h2 class="text-center mt-3">{{ domain.upper() }} Recommendations</h2>

  <h3>Languages & Tools:</h3>
  <ul>{% for lang in data.languages %}<li>{{ lang }}</li>{% endfor %}</ul>

  <h3>Internship Roles:</h3>
  <ul>{% for role in data.internships %}<li>{{ role }}</li>{% endfor %}</ul>

  <h3>Certifications:</h3>
  <ul>{% for cert in data.certifications %}<li><a href="{{ cert.link }}" target="_blank">{{ cert.name }}</a></li>{% endfor %}</ul>

  <h3>Projects by Level:</h3>
  {% for level, projects in data.projects.items() %}
    <h4>{{ level }} Level:</h4>
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
        if data:
            bg = data["bg"]
    return render_template_string(TEMPLATE, data=data, domain=domain, bg=bg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
