import random

def get_animated_text():
    animations = [
        "HELLO, YOU",
        "HI THERE!",
        "GREETINGS!",
        "WELCOME!",
        "HEY!"
    ]
    return random.choice(animations)

animated_text = get_animated_text()

readme_template = """
# {animated_text}
## I'm OSISEHH 👋

Welcome to my GitHub profile! I'm passionate about Artificial Intelligence and Machine Learning. Below, you'll find more information about me and my work.

## 🔭 What I'm Currently Working On
- **[Email Classifier](https://github.com/Osisehh/Email-Classifier)**: About
A machine learning project designed to classify emails as spam or non-spam based on their content.

## 🌱 What I'm Learning
- Currently diving into **[Artificial Intelligence ]**
- Exploring **[YOLO]**

## 📫 How to Reach Me
- Email: [osisehirudunoghena@gmail.com](mailto:osisehirudunoghena@gmail.com)
- LinkedIn: [Irudunoghena Osiseh](www.linkedin.com/in/osiseh-irudunoghena)

## 🛠️ Languages and Tools
- **Languages**: Python, R, SQL, HTML, CSS
- **Tools**: Git, TensorFlow, Keras, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Selenium, Git Docker, NLP

## 📈 GitHub Stats
![Osisehh's GitHub stats](https://github-readme-stats.vercel.app/api?username=Osisehh&show_icons=true&theme=radical)

## 🏆 Achievements
- **[Bronze Medal on KaggleNotebook]**

## 💡 Fun Facts
- I love **[Music and Cooking]**
- I'm a **[Fast Learner. I don't slow down]**

## 🤝 Let's Connect
Feel free to reach out if you want to collaborate on a project, ask questions, or just say hi!

"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_template.format(animated_text=animated_text))
