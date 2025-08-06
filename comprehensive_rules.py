# comprehensive_rules.py
# Comprehensive ELIZA Rules Set
# Complete rules for ELIZA bot with diverse responses and flowing conversation

rules = {
    # High priority rules - emotions and mental states
    "depressed": {
        "rank": 10,
        "decompositions": [
            {
                "pattern": r"i.*depressed",
                "reassembly": [
                    "I'm sorry to hear you're feeling depressed. Can you tell me more about it?",
                    "Depression can be very difficult. What makes you feel this way?",
                    "When did you first start feeling depressed?",
                    "What do you think is causing your depression?"
                ]
            }
        ]
    },

    "sad": {
        "rank": 9,
        "decompositions": [
            {
                "pattern": r"i.*sad",
                "reassembly": [
                    "What is making you feel sad?",
                    "Tell me more about your sadness.",
                    "How long have you been feeling this way?",
                    "Is there something specific that triggered this sadness?"
                ]
            }
        ]
    },

    "angry": {
        "rank": 9,
        "decompositions": [
            {
                "pattern": r"i.*angry|i.*mad|i.*furious",
                "reassembly": [
                    "What made you angry?",
                    "Tell me about your anger.",
                    "How do you usually handle your anger?",
                    "What triggers your anger most often?"
                ]
            }
        ]
    },

    "anxious": {
        "rank": 9,
        "decompositions": [
            {
                "pattern": r"i.*anxious|i.*worried|i.*nervous",
                "reassembly": [
                    "What are you anxious about?",
                    "Tell me more about your worries.",
                    "When do you feel most anxious?",
                    "What helps you when you're feeling this way?"
                ]
            }
        ]
    },

    "happy": {
        "rank": 8,
        "decompositions": [
            {
                "pattern": r"i.*happy|i.*glad|i.*joyful",
                "reassembly": [
                    "That's wonderful! What makes you happy?",
                    "I'm glad to hear you're feeling good. Tell me more.",
                    "What brings you the most joy?",
                    "It's great that you're feeling positive."
                ]
            }
        ]
    },

    # Family rules
    "mother": {
        "rank": 8,
        "decompositions": [
            {
                "pattern": r"my mother (.*)",
                "reassembly": [
                    "Tell me more about your mother and {0}.",
                    "What is your relationship with your mother like?",
                    "How do you feel about your mother {0}?",
                    "Does your mother's {0} affect you?"
                ]
            },
            {
                "pattern": r"mother",
                "reassembly": [
                    "Tell me about your mother.",
                    "What was your mother like?",
                    "How is your relationship with your mother?",
                    "What role does your mother play in your life?"
                ]
            }
        ]
    },

    "father": {
        "rank": 8,
        "decompositions": [
            {
                "pattern": r"my father (.*)",
                "reassembly": [
                    "What about your father and {0}?",
                    "How does your father's {0} make you feel?",
                    "Tell me more about your father {0}.",
                    "What is your relationship with your father like?"
                ]
            },
            {
                "pattern": r"father",
                "reassembly": [
                    "Tell me about your father.",
                    "What was your father like?",
                    "How do you feel about your father?",
                    "What role did your father play in your life?"
                ]
            }
        ]
    },

    "family": {
        "rank": 7,
        "decompositions": [
            {
                "pattern": r"my family (.*)",
                "reassembly": [
                    "Tell me more about your family and {0}.",
                    "How does your family {0} affect you?",
                    "What is your family like when they {0}?"
                ]
            },
            {
                "pattern": r"family",
                "reassembly": [
                    "Tell me about your family.",
                    "What is your family like?",
                    "How do you get along with your family?",
                    "Family relationships can be complex. How are yours?"
                ]
            }
        ]
    },

    # Relationship rules
    "relationship": {
        "rank": 7,
        "decompositions": [
            {
                "pattern": r"my relationship (.*)",
                "reassembly": [
                    "What about your relationship {0}?",
                    "How do you feel about your relationship {0}?",
                    "Tell me more about this relationship issue."
                ]
            },
            {
                "pattern": r"relationship",
                "reassembly": [
                    "What kind of relationship are you thinking about?",
                    "Tell me about your relationships.",
                    "How are your relationships going?",
                    "What makes a good relationship for you?"
                ]
            }
        ]
    },

    "friend": {
        "rank": 6,
        "decompositions": [
            {
                "pattern": r"my friend (.*)",
                "reassembly": [
                    "Tell me about your friend and {0}.",
                    "How do you feel about your friend {0}?",
                    "What kind of friend {0}?"
                ]
            },
            {
                "pattern": r"friend",
                "reassembly": [
                    "Tell me about your friends.",
                    "What do you value in a friend?",
                    "How are things with your friends?",
                    "Friendship is important. How are yours?"
                ]
            }
        ]
    },

    # Work and study rules
    "work": {
        "rank": 6,
        "decompositions": [
            {
                "pattern": r"my work (.*)",
                "reassembly": [
                    "How do you feel about your work {0}?",
                    "Tell me more about work and {0}.",
                    "What about your work {0} bothers you?"
                ]
            },
            {
                "pattern": r"work",
                "reassembly": [
                    "How do you feel about your work?",
                    "Tell me about your work situation.",
                    "What's your work like?",
                    "Are you satisfied with your work?"
                ]
            }
        ]
    },

    "school": {
        "rank": 6,
        "decompositions": [
            {
                "pattern": r"school (.*)",
                "reassembly": [
                    "What about school and {0}?",
                    "How do you feel about school {0}?",
                    "Tell me more about your school experience."
                ]
            },
            {
                "pattern": r"school",
                "reassembly": [
                    "How are things at school?",
                    "Tell me about school.",
                    "What's school like for you?",
                    "How do you feel about your studies?"
                ]
            }
        ]
    },

    # Basic "I" rules
    "i": {
        "rank": 5,
        "decompositions": [
            {
                "pattern": r"i feel (.*)",
                "reassembly": [
                    "Tell me more about feeling {0}.",
                    "Do you often feel {0}?",
                    "Why do you feel {0}?",
                    "When did you start feeling {0}?",
                    "What makes you feel {0}?"
                ]
            },
            {
                "pattern": r"i am (.*)",
                "reassembly": [
                    "How long have you been {0}?",
                    "Why do you think you are {0}?",
                    "Do you like being {0}?",
                    "What does it mean to you to be {0}?"
                ]
            },
            {
                "pattern": r"i have (.*)",
                "reassembly": [
                    "How do you feel about having {0}?",
                    "What does having {0} mean to you?",
                    "Tell me more about your {0}.",
                    "How long have you had {0}?"
                ]
            },
            {
                "pattern": r"i want (.*)",
                "reassembly": [
                    "Why do you want {0}?",
                    "What would it mean to you to have {0}?",
                    "What if you got {0}?",
                    "How badly do you want {0}?"
                ]
            },
            {
                "pattern": r"i need (.*)",
                "reassembly": [
                    "Why do you need {0}?",
                    "What makes you think you need {0}?",
                    "How would {0} help you?",
                    "What would happen if you didn't get {0}?"
                ]
            },
            {
                "pattern": r"i think (.*)",
                "reassembly": [
                    "Why do you think {0}?",
                    "Tell me more about thinking {0}.",
                    "What makes you believe {0}?",
                    "Are you sure you think {0}?"
                ]
            },
            {
                "pattern": r"i believe (.*)",
                "reassembly": [
                    "What makes you believe {0}?",
                    "How strong is your belief that {0}?",
                    "Why is it important to believe {0}?"
                ]
            },
            {
                "pattern": r"i can't (.*)",
                "reassembly": [
                    "Why can't you {0}?",
                    "What stops you from {0}?",
                    "Have you tried to {0}?",
                    "What would help you {0}?"
                ]
            },
            {
                "pattern": r"i don't (.*)",
                "reassembly": [
                    "Why don't you {0}?",
                    "What would happen if you did {0}?",
                    "Do you want to {0}?",
                    "What stops you from {0}?"
                ]
            }
        ]
    },

    # "You" rules (about the therapist)
    "you": {
        "rank": 4,
        "decompositions": [
            {
                "pattern": r"you are (.*)",
                "reassembly": [
                    "What makes you think I am {0}?",
                    "Do you believe I am {0}?",
                    "Does it matter whether I am {0}?",
                    "Why is it important if I am {0}?"
                ]
            },
            {
                "pattern": r"you (.*)",
                "reassembly": [
                    "Why do you think I {0}?",
                    "We're here to talk about you, not me.",
                    "What makes you think about me {0}?",
                    "Let's focus on you instead."
                ]
            }
        ]
    },

    # Common problems rules
    "problem": {
        "rank": 6,
        "decompositions": [
            {
                "pattern": r"my problem (.*)",
                "reassembly": [
                    "Tell me more about your problem with {0}.",
                    "How long has this problem with {0} been bothering you?",
                    "What do you think causes this problem?"
                ]
            },
            {
                "pattern": r"problem",
                "reassembly": [
                    "What kind of problem are you having?",
                    "Tell me about your problem.",
                    "How long have you had this problem?",
                    "What do you think is the root of the problem?"
                ]
            }
        ]
    },

    "stress": {
        "rank": 7,
        "decompositions": [
            {
                "pattern": r"stressed|stress",
                "reassembly": [
                    "What is causing you stress?",
                    "How do you usually handle stress?",
                    "Tell me about your stress.",
                    "When do you feel most stressed?",
                    "What would help reduce your stress?"
                ]
            }
        ]
    },

    # Memory and experience rules
    "remember": {
        "rank": 5,
        "decompositions": [
            {
                "pattern": r"i remember (.*)",
                "reassembly": [
                    "What else do you remember about {0}?",
                    "Why do you think you remember {0} now?",
                    "How does remembering {0} make you feel?",
                    "What is significant about {0}?"
                ]
            }
        ]
    },

    "dream": {
        "rank": 6,
        "decompositions": [
            {
                "pattern": r"i dream.*about (.*)",
                "reassembly": [
                    "What do you think dreaming about {0} means?",
                    "How do you feel about these dreams of {0}?",
                    "Tell me more about your dreams."
                ]
            },
            {
                "pattern": r"dream",
                "reassembly": [
                    "What was in your dream?",
                    "Tell me about your dreams.",
                    "How do your dreams make you feel?",
                    "Do you often remember your dreams?"
                ]
            }
        ]
    },

    # Social behavior rules
    "lonely": {
        "rank": 8,
        "decompositions": [
            {
                "pattern": r"lonely",
                "reassembly": [
                    "Tell me about your loneliness.",
                    "When do you feel most lonely?",
                    "What makes you feel less lonely?",
                    "How long have you been feeling lonely?"
                ]
            }
        ]
    },

    "afraid": {
        "rank": 8,
        "decompositions": [
            {
                "pattern": r"i.*afraid|i.*scared|i.*fear",
                "reassembly": [
                    "What are you afraid of?",
                    "Tell me more about your fear.",
                    "When did this fear start?",
                    "How does this fear affect your life?"
                ]
            }
        ]
    },

    # Special rules
    "sorry": {
        "rank": 3,
        "decompositions": [
            {
                "pattern": r"sorry",
                "reassembly": [
                    "Please don't apologize.",
                    "Apologies are not necessary.",
                    "Why do you feel you need to apologize?",
                    "There's no need to be sorry."
                ]
            }
        ]
    },

    "hello": {
        "rank": 2,
        "decompositions": [
            {
                "pattern": r"hello|hi|hey",
                "reassembly": [
                    "Hello. How are you feeling today?",
                    "Hi there. What's on your mind?",
                    "Hello. What would you like to talk about?",
                    "Hi. Tell me about yourself."
                ]
            }
        ]
    },

    "goodbye": {
        "rank": 2,
        "decompositions": [
            {
                "pattern": r"goodbye|bye|farewell",
                "reassembly": [
                    "Goodbye. I hope our conversation was helpful.",
                    "Thank you for talking with me.",
                    "Goodbye. Take care of yourself.",
                    "I hope to speak with you again soon."
                ]
            }
        ]
    },

    "yes": {
        "rank": 1,
        "decompositions": [
            {
                "pattern": r"yes",
                "reassembly": [
                    "You seem quite sure.",
                    "I see. Can you tell me more?",
                    "Why do you think so?",
                    "What makes you so certain?"
                ]
            }
        ]
    },

    "no": {
        "rank": 1,
        "decompositions": [
            {
                "pattern": r"no",
                "reassembly": [
                    "Why not?",
                    "Are you sure?",
                    "Can you tell me more about that?",
                    "What makes you say no?"
                ]
            }
        ]
    },

    # Default general rules - low priority
    "always": {
        "rank": 1,
        "decompositions": [
            {
                "pattern": r"always (.*)",
                "reassembly": [
                    "Can you think of a time when you didn't {0}?",
                    "Really, always?",
                    "What makes you think you always {0}?"
                ]
            }
        ]
    },

    "never": {
        "rank": 1,
        "decompositions": [
            {
                "pattern": r"never (.*)",
                "reassembly": [
                    "Never? That seems absolute.",
                    "Can you think of a time when you did {0}?",
                    "What would it mean if you did {0}?"
                ]
            }
        ]
    }
}

# Default responses when no pattern matches
default_responses = [
    "Please go on.",
    "Tell me more about that.",
    "I see. Can you elaborate?",
    "That's interesting. Continue.",
    "How does that make you feel?",
    "What comes to mind when you think about that?",
    "Can you give me more details?",
    "I'm listening. Please continue.",
    "What else would you like to discuss?",
    "How long have you felt this way?",
    "What do you think about that?",
    "Can you tell me more?"
]

# Context-aware responses - responses that refer to previous conversation
context_responses = [
    "Earlier you mentioned {topic}. How does that relate to what you're saying now?",
    "This reminds me of when you talked about {topic}. Is there a connection?",
    "You seem to return to the theme of {topic}. Why is that important to you?",
    "I notice you've mentioned {topic} before. Tell me more about that.",
]