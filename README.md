# 🤖 AI Study Assistant

An AI-powered command-line study assistant built with Python and local AI.

It helps students study technical subjects through AI explanations, revision notes, questions, quizzes, progress tracking, achievements, and saved notes.

## 📸 Demo

![AI Study Assistant]( <img width="367" height="349" alt="Screenshot 2026-09-06 121617" src="https://github.com/user-attachments/assets/39a685f2-d9b5-4c0a-95cc-bc1aadf9be3c" />
)

---

## ✨ Features

- 🤖 **Ask AI** — Get simple explanations for difficult concepts
- 📝 **AI Notes Generator** — Generate concise, exam-friendly revision notes
- ❓ **AI Question Generator** — Generate practice questions
- 📚 **Key Points** — Quickly review important concepts
- 🧠 **AI Quiz Mode** — Test your understanding
- 📊 **Study Dashboard** — Track quiz performance
- 🏆 **Achievements** — Unlock badges as you study
- 📖 **Topic Progress** — See your strongest and weakest topics
- 💾 **Save Notes** — Store generated notes locally
- 🔒 **Local AI** — Uses Ollama, so AI runs locally on your computer

---

## 📚 Available Topics

The current version includes:

- Operating Systems
- Data Structures
- Python
- C++
- Java
- DBMS
- Computer Networks
- Algorithms

---

## 🧠 How the AI Works

The project uses **Ollama** to run the Llama 3.2 model locally.

Instead of sending study questions to a cloud API, the application communicates with the locally running AI model.

```text
User
  ↓
AI Study Assistant
  ↓
Python Application
  ↓
Ollama
  ↓
Llama 3.2
  ↓
AI Response

Absolutely. 🔥 Replace the entire contents of your current README.md with this:

# 🤖 AI Study Assistant

An AI-powered command-line study assistant built with Python and local AI.

It helps students study technical subjects through AI explanations, revision notes, questions, quizzes, progress tracking, achievements, and saved notes.

## 📸 Demo

![AI Study Assistant](screenshot.png)

---

## ✨ Features

- 🤖 **Ask AI** — Get simple explanations for difficult concepts
- 📝 **AI Notes Generator** — Generate concise, exam-friendly revision notes
- ❓ **AI Question Generator** — Generate practice questions
- 📚 **Key Points** — Quickly review important concepts
- 🧠 **AI Quiz Mode** — Test your understanding
- 📊 **Study Dashboard** — Track quiz performance
- 🏆 **Achievements** — Unlock badges as you study
- 📖 **Topic Progress** — See your strongest and weakest topics
- 💾 **Save Notes** — Store generated notes locally
- 🔒 **Local AI** — Uses Ollama, so AI runs locally on your computer

---

## 📚 Available Topics

The current version includes:

- Operating Systems
- Data Structures
- Python
- C++
- Java
- DBMS
- Computer Networks
- Algorithms

---

## 🧠 How the AI Works

The project uses **Ollama** to run the Llama 3.2 model locally.

Instead of sending study questions to a cloud API, the application communicates with the locally running AI model.

```text
User
  ↓
AI Study Assistant
  ↓
Python Application
  ↓
Ollama
  ↓
Llama 3.2
  ↓
AI Response
🛠️ Tech Stack
Technology	Purpose
Python	Application logic
Ollama	Local AI runtime
Llama 3.2	AI model
JSON	Progress storage
Git	Version control
GitHub	Source code hosting
📁 Project Structure
ai-study-assistant/
│
├── app.py
├── ai.py
├── study_data.py
├── progress.py
├── achievements.py
├── notes_manager.py
├── requirements.txt
├── screenshot.png
├── README.md
│
├── notes/
│
└── .gitignore
🚀 Installation
1. Clone the repository
git clone https://github.com/divyanshtomar2006-prog/ai-study-assistant.git
2. Open the project folder
cd ai-study-assistant
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
Windows
.venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
🤖 Set Up Local AI

Install Ollama and download the Llama 3.2 model.

Then run:

ollama run llama3.2

Keep Ollama running while using the AI features.

▶️ Run the Application

From the project directory:

python app.py

The application will display the available study topics.

Choose a topic and select the feature you want to use.

📊 Study Dashboard

The application tracks:

Total quizzes completed
Best score
Average score
Topic-wise performance
Strongest topic
Topic needing more practice

Progress is stored locally in:

progress.json

progress.json is ignored by Git so personal study progress isn't uploaded to the repository.

🏆 Achievements

The application currently includes achievements such as:

Achievement	Requirement
🥉 First Step	Complete your first quiz
🔥 Getting Serious	Complete 3 quizzes
🏆 Perfect Mind	Score 100%
📚 Knowledge Seeker	Study 5 different topics
💯 Century Club	Answer 100 questions
💾 Saved Notes

Generated AI notes can be saved locally.

Saved notes are stored inside:

notes/

Each topic gets its own text file for easy revision.

🎯 Project Goals

This project was created to combine:

Python programming
AI integration
Local AI models
File handling
JSON data storage
Git and GitHub
Basic software architecture

The goal is to continuously improve the application while learning AI and software development.

🔮 Future Improvements

Planned features include:

📅 AI Study Planner
🎯 Personalized study recommendations
📈 Better progress visualizations
🧪 More quiz question types
🔍 Search across study topics
🌐 Web-based interface
📱 Mobile-friendly version
🎤 Voice-based study assistant
📚 More academic subjects
📌 Current Status

Version: 1.0

The current version supports local AI-powered explanations, notes, questions, quizzes, progress tracking, achievements, and saved notes.

👨‍💻 Author

Divyansh Tomar

Built as a learning project while exploring:

Python • AI • Local LLMs • GitHub • Software Development

⭐ If you find this project interesting, consider giving the repository a star!
