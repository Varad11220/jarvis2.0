# 💡 Jarvis (Voice-Controlled Desktop Assistant)  
🚀 *Your Personal Voice-Activated Desktop Sidekick*  
This **Python-based desktop automation project** acts like a mini **Jarvis** from Iron Man. With a simple press of the **`H` key**, users can activate voice commands to automate common tasks like opening apps, searching the web, sending messages, checking system stats, and much more — all from a unified dashboard interface.

---

## 🔧 Features
- 🗣️ **Voice Command Trigger** — Press `H` to start listening for voice commands  
- 🧠 **Smart Task Execution** — Based on voice, perform tasks like:  
  - 🖥️ Open any installed desktop application  
  - 🌐 Search anything on Google  
  - 📺 Play a video directly on YouTube  
  - 📥 Download YouTube video from clipboard link  
  - 🎮 Play browser-based games  
  - 💬 Add a contact and send a message via WhatsApp (Web/App)  
- 📊 **System Dashboard** — Displays:  
  - ⏰ Current time and date  
  - ⚙️ CPU speed  
  - 🔥 GPU speed  
  - 📈 Running processes  

---

## 🛠️ Tech Stack
- 🐍 **Python** — Core programming language  
- 🎙️ **SpeechRecognition** — For capturing and processing voice input  
- 🧠 **Pyttsx3** — Text-to-speech for voice feedback  
- 🌍 **pywhatkit** — For online search and actions  
- 🖼️ **PyQt** — GUI for the dashboard  
- 💻 **psutil** — To monitor system performance  
- 📋 **pyperclip** — To read YouTube links from clipboard  
- 🖱️ **keyboard** — For hotkey-based trigger (`H` key)

---

## 👥 Collaborators
- [Varad Khandare](https://github.com/Varad11220)  
- [Yash Dhavde](https://github.com/YashD15)  

---

## 📦 Installation
```bash
git clone https://github.com/Varad11220/jarvis2.0.git
cd jarvis2.0
pip install -r requirements.txt
python main.py
