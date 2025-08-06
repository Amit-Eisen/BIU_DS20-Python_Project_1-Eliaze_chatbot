# 🧠 ELIZA Chatbot Project

This project is a modern Python remake of the classic 1960s ELIZA chatbot — a simple *rule-based psychotherapist bot*.  
It simulates human-like conversation using pattern-matching and keyword decomposition.

---

## 🚀 Features

- ✅ Rule-based response engine (Layer 3 logic)
- ✅ Comprehensive rule set (~200+ patterns)
- ✅ Temporary session-based memory
- ✅ Clean Streamlit UI with WhatsApp-style chat bubbles
- ✅ Default fallback responses for open-ended prompts

---

## 🧠 How It Works

1. User input is matched against ranked keyword rules.
2. If a rule is matched, a reassembly pattern is selected and filled with substitutions.
3. If no match is found, a default response is returned.
4. The bot uses simple pronoun reflection (I → you, me → you, etc.).

---

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/Amit-Eisen/BIU_DS20-Python_Project_1-Eliaze_chatbot.git
   cd BIU_DS20-Python_Project_1-Eliaze_chatbot
   ```
   
2. **Install Poetry**

    ```bash
   pip install poetry
    ```
   
3. **Install environment & dependencies:**

    ```bash
    poetry install
    ```
4. **Run the app with Poetry:
   
   ```bash
   poetry run streamlit run main.py
   ```


## 🗂️ Project Structure

<pre lang="markdown">
📁 Eliza chatbot 
├── main.py                   # UI using Streamlit 
├── eliza_engine.py	          # Logic engine 
├── comprehensive_rules.py    # Full ELIZA ruleset 
├── poetry.lock               # Poetry project file 
├── poetry.lock               # Poetry lock file
└── README.md                 # You're reading it 
</pre>

## 📢 Notes

 - Memory is session-based only (resets on app reload).
 - Easy to expand: add more rules in comprehensive_rules.py for richer conversations.

## Autour
**Amit Eisen**






