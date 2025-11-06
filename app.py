from flask import Flask, render_template_string, request

app = Flask(__name__)

# Domain data
domains = {
    "ai": {
        "bg": "https://en.sepoin.com/wp-content/uploads/2020/01/AI-ML-4.jpg",
        "color": "#ffff99",
        "ideas": ["AI Chatbot", "Image Recognition", "AI Resume Screener"],
        "languages": ["Python", "TensorFlow", "PyTorch"],
        "learn_link": "https://www.coursera.org/specializations/machine-learning-introduction"
    },
    "web": {
        "bg": "https://static.vecteezy.com/system/resources/previews/000/523/309/original/web-development-and-programming-coding-concept-seo-optimization-modern-web-design-on-laptop-screen-vector.jpg",
        "color": "#00bfff",
        "ideas": ["Portfolio Website", "Blog CMS", "E-Commerce App"],
        "languages": ["HTML", "CSS", "JavaScript", "Flask/Django"],
        "learn_link": "https://www.udemy.com/course/the-complete-web-development-bootcamp/"
    },
    "cloud": {
        "bg": "https://cdn.pixabay.com/photo/2024/01/26/08/07/ai-generated-8533603_1280.jpg",
        "color": "#00ffff",
        "ideas": ["Cloud File Uploader", "Serverless Function App", "Cloud Monitoring Dashboard"],
        "languages": ["Python", "AWS CLI", "Docker"],
        "learn_link": "https://www.coursera.org/specializations/aws-fundamentals"
    },
    "cybersecurity": {
        "bg": "https://images.wallpapersden.com/image/download/cybersecurity-core_bmdrZ2mUmZqaraWkpJRmbmdsrWZlbWU.jpg",
        "color": "#ff6347",
        "ideas": ["Password Strength Checker", "Phishing Detection", "Network Scanner"],
        "languages": ["Python", "Wireshark", "Kali Linux"],
        "learn_link": "https://www.udemy.com/course/the-complete-cyber-security-course-hackers-exposed/"
    },
    "devops": {
        "bg": "https://www.tekcent.com/media/yncjty2t/devops-1600x900-1423173157.jpg",
        "color": "#7CFC00",
        "ideas": ["CI/CD Pipeline", "Dockerized App", "Kubernetes Monitor"],
        "languages": ["Python", "Docker", "Jenkins", "Kubernetes"],
        "learn_link": "https://www.coursera.org/specializations/devops"
    },
    "robotics": {
        "bg": "https://tse4.mm.bing.net/th/id/OIP.CgeybFxfhad-Jo8HU0HpfwHaD5?pid=Api&P=0&h=180",
        "color": "#ff69b4",
        "ideas": ["Line Follower Robot", "Object Avoidance Bot", "Robotic Arm Controller"],
        "languages": ["Python", "ROS", "Arduino"],
        "learn_link": "https://www.coursera.org/specializations/robotics"
    }
}

# HTML template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Smart Internship & Project Recommender</title>
  <style>
    body {
      background-image: url('{{ bg }}');
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
      font-family: 'Poppins', sans-serif;
      color: white;
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
      color: #ffffff;
    }
    h1, h2, h3, h4, h5 {
      color: #ffffff;
    }
    a { 
      color: {{ color }};
      text-decoration: none; 
      font-weight: 600;
    }
    a:hover { text-decoration: underline; }
    input {
      padding: 10px;
      width: 70%;
      border-radius: 8px;
      border: none;
      margin-top: 10px;
      text-align: center;
    }
    button {
      margin-top: 15px;
      padding: 10px 20px;
      border: none;
      border-radius: 8px;
      background-color: #ffb347;
      color: black;
      font-weight: 600;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="overlay">
    <h1>Smart Internship & Project Recommender</h1>
    <form method="post">
      <input type="text" name="domain" placeholder="Enter your interest (e.g. AI, Web, Cloud, etc.)" required>
      <br>
      <button type="submit">Recommend</button>
    </form>

    {% if domain %}
    <div class="card">
      <h2>{{ domain.upper() }} Recommendations</h2>
      <h3>💡 Project Ideas</h3>
      <ul>
        {% for idea in ideas %}
        <li>{{ idea }}</li>
        {% endfor %}
      </ul>
      <h3>🧠 Languages to Learn</h3>
      <p>{{ ', '.join(languages) }}</p>
      <h3>📚 Learn More</h3>
      <a href="{{ learn_link }}" target="_blank">Click here to start learning →</a>
    </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        domain = request.form["domain"].strip().lower()
        data = domains.get(domain)
        if data:
            return render_template_string(template, domain=domain, **data)
        else:
            return render_template_string(template, domain=None, bg="https://images.unsplash.com/photo-1498050108023-c5249f4df085")
    return render_template_string(template, domain=None, bg="https://images.unsplash.com/photo-1498050108023-c5249f4df085")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
