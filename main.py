import re
import random
import streamlit as st
from collections import Counter, defaultdict

from comprehensive_rules import rules, default_responses, context_responses

# Substitution map to reflect user input
substitutions = {
    "i": "you",
    "you": "I",
    "me": "you",
    "my": "your",
    "your": "my",
    "am": "are",
    "are": "am",
    "myself": "yourself",
    "yourself": "myself"
}

def apply_substitutions(text: str) -> str:
    # Swap common pronouns to mimic conversation
    words = re.findall(r"\b\w+\b", text.lower())
    return " ".join([substitutions.get(word, word) for word in words])

def extract_topics_from_history():
    # Get important topics from what the user said
    if "conversation_history" not in st.session_state:
        return []

    topics = []
    important_keywords = ['mother', 'father', 'family', 'work', 'school', 'friend',
                          'sad', 'happy', 'angry', 'depressed', 'anxious', 'problem', 'stress']

    for sender, message in st.session_state.conversation_history:
        if sender == "user":
            msg = message.lower()
            for keyword in important_keywords:
                if keyword in msg:
                    topics.append(keyword)

    counts = Counter(topics)
    return [topic for topic, count in counts.most_common(3)]

def should_use_context_response():
    # Decide randomly (sometimes) to respond based on topic
    if "conversation_history" not in st.session_state:
        return False
    return len(st.session_state.conversation_history) > 8 and random.random() < 0.2

def get_context_response():
    # Return a response based on previously mentioned topic
    topics = extract_topics_from_history()
    if topics:
        topic = random.choice(topics)
        template = random.choice(context_responses)
        return template.format(topic=topic)
    return None

def get_response(user_input: str) -> str:
    user_input_clean = user_input.lower().strip()

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []
    if "used_responses" not in st.session_state:
        st.session_state.used_responses = defaultdict(int)

    # Occasionally use context-aware response
    if should_use_context_response():
        context_resp = get_context_response()
        if context_resp:
            return context_resp

    sorted_keywords = sorted(rules.items(), key=lambda x: -x[1]["rank"])

    for keyword, data in sorted_keywords:
        if keyword in user_input_clean:
            for rule in data["decompositions"]:
                match = re.search(rule["pattern"], user_input_clean)
                if match:
                    fragments = match.groups()
                    substituted = [apply_substitutions(f) for f in fragments]

                    # Try to avoid repeating the same responses
                    options = rule["reassembly"]
                    weights = []

                    for template in options:
                        count = st.session_state.used_responses[template]
                        weights.append(max(1, 5 - count))

                    template = random.choices(options, weights=weights)[0]

                    try:
                        response = template.format(*substituted)
                        st.session_state.used_responses[template] += 1

                        # Occasionally reset memory so answers can be reused
                        if len(st.session_state.used_responses) > 50:
                            for key in list(st.session_state.used_responses.keys()):
                                st.session_state.used_responses[key] = max(0, st.session_state.used_responses[key] - 1)

                        st.session_state.conversation_history.append(("user", user_input))
                        st.session_state.conversation_history.append(("eliza", response))
                        return response
                    except Exception:
                        continue

    # No match – fallback
    defaults = default_responses
    weights = []
    for resp in defaults:
        count = st.session_state.used_responses[resp]
        weights.append(max(1, 5 - count))

    fallback = random.choices(defaults, weights=weights)[0]
    st.session_state.used_responses[fallback] += 1

    st.session_state.conversation_history.append(("user", user_input))
    st.session_state.conversation_history.append(("eliza", fallback))
    return fallback

def get_conversation_stats():
    # Just count how many turns and what topics came up
    if "conversation_history" not in st.session_state:
        return {"total_exchanges": 0, "topics": []}

    total = len([msg for sender, msg in st.session_state.conversation_history if sender == "user"])
    topics = extract_topics_from_history()

    return {
        "total_exchanges": total,
        "topics": topics
    }
