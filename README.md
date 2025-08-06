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
   git clone https://github.com/yourusername/eliza-chatbot.git
   cd eliza-chatbot
   ```
   
2. **Install dependencies**

    ```bash
   pip install -r requirements.txt
    ```
   
3. **Run the app**

    ```bash
    streamlit run streamlit_app.py
    ```
   
## 🗂️ Project Structure

<pre lang="markdown">
📁 Eliza chatbot 
├── streamlit_app.py          # UI using Streamlit 
├── main.py	          # Logic engine 
├── comprehensive_rules.py    # Full ELIZA ruleset 
├── requirements.txt          # Dependencies 
└── README.md                 # You're reading it 
</pre>

## 📄 Requirements
    streamlit

## 📢 Notes

 - Memory is session-based only (resets on app reload).
 - Easy to expand: add more rules in comprehensive_rules.py for richer conversations.

## Autour
**Amit Eisen**






