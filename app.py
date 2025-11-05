from flask import Flask, render_template_string, request

app = Flask(__name__)

# ----------- DATA: INTERNSHIP, PROJECTS, LANGUAGES & CERTIFICATIONS -----------
recommendations = {
    "web": {
        "bg": "https://static.vecteezy.com/system/resources/previews/000/523/309/original/web-development-and-programming-coding-concept-seo-optimization-modern-web-design-on-laptop-screen-vector.jpg",
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
    },
    "robotics": {
        "bg": "https://tse4.mm.bing.net/th/id/OIP.CgeybFxfhad-Jo8HU0HpfwHaD5?pid=Api&P=0&h=180",
        "languages": ["C++", "Python", "Arduino", "ROS"],
        "certifications": [
            {"name": "ROS Robotics Certification", "link": "https://www.coursera.org/learn/robotics"},
            {"name": "Arduino Fundamentals", "link": "https://www.arduino.cc/en/Tutorial/HomePage"}
        ],
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

# ----------- HTML TEMPLATE -----------
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Smart Internship & Project Recommender</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.5/lottie.min.js"></script>
  <style>
    body {
      background-image: url('{{ bg }}');
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
      color: white;
      font-family: 'Poppins', sans-serif;
    }
    .overlay {
      background-color: rgba(0,0,0,0.6);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
    }
    .card {
      background-color: rgba(0,0,0,0.7);
      border-radius: 20px;
      padding: 2rem;
      width: 90%;
      max-width: 800px;
      margin-top: 2rem;
    }
    .btn {
      background-color: #ffb347;
      color: black;
      border: none;
      font-weight: 600;
    }
    a { color: #ffcc70; text-decoration: none; }
    a:hover { text-decoration: underline; }
    #lottie {
      width: 300px;
      height: 300px;
      margin: auto;
    }
  </style>
</head>
<body>
  <div class="overlay">
    {% if not data %}
    <!-- Front page Lottie Animation -->
    <div id="lottie"></div>
    <h1 class="fw-bold mt-3">🚀 Smart Internship & Project Recommender</h1>
    <p class="text-light">Explore internships, projects, and certifications tailored to your domain of interest.</p>
    {% endif %}

    <div class="card">
      <form method="POST">
        <label>Select Your Domain:</label><br>
        <select name="domain" class="form-select mt-2 mb-3" required>
          <option value="">-- Choose Domain --</option>
          <option value="ai">AI & ML</option>
          <option value="cloud">Cloud Computing</option>
          <option value="cybersecurity">Cybersecurity</option>
          <option value="web">Web Development</option>
          <option value="devops">DevOps</option>
          <option value="robotics">Robotics</option>
        </select>
        <button class="btn btn-warning" type="submit">Recommend</button>
      </form>
    </div>

    {% if data %}
    <div class="card mt-4 text-start">
      <h2>{{ domain.upper() }} Recommendations</h2>

      <h3>Languages & Tools:</h3>
      <ul>{% for lang in data.languages %}<li>{{ lang }}</li>{% endfor %}</ul>

      <h3>Internships:</h3>
      <ul>{% for role in data.internships %}<li>{{ role }}</li>{% endfor %}</ul>

      <h3>Certifications:</h3>
      <ul>{% for cert in data.certifications %}
        <li><a href="{{ cert.link }}" target="_blank">{{ cert.name }}</a></li>
      {% endfor %}</ul>

      <h3>Project Ideas:</h3>
      {% for level, projects in data.projects.items() %}
        <h5>{{ level }} Level</h5>
        <ul>
          {% for project in projects %}
            <li><a href="{{ project.link }}" target="_blank">{{ project.title }}</a></li>
          {% endfor %}
        </ul>
      {% endfor %}
    </div>
    {% endif %}
  </div>

  {% if not data %}
  <script>
    // Front page Lottie Animation
    var animation = lottie.loadAnimation({
      container: document.getElementById('lottie'),
      path: 'https://lottie.host/eBolNfIgIj/creative-team.json', // replace with your Lottie JSON link
      renderer: 'svg',
      loop: true,
      autoplay: true
    });
  </script>
  {% endif %}
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
