import nltk
from nltk.chat.util import Chat, reflections
set_pairs=[
         [  r"my name is (.*)",
           ["Hello %1,How are you today?",]
         ],
      [ r"hi|hello|hey",
       ["Hello!","Hey there!",]
      ], 
     [ r"what is your name?",
        ["My name is Savy. How can I help you?"]
    ],
    [
        r"what can you do?",
        ["I can help you with a variety of tasks such as finding information, providing recommendations, or just having a casual conversation."]
    ],
    [
        r"what do you like?",
        ["I like helping people and learning new things."]
    ],
    [
        r"how old are you?",
        ["I am an artificial intelligence, so I don't have an age in the traditional sense."]
    ],
    [
        r"thanks|thank you",
        ["You're welcome! Is there anything else you need help with?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!"]
    ]
]
def chatbot():
    print("Hey I am a rule-based chatbot.How can I help you?!")
chatbot()
chat=Chat(set_pairs,reflections)
chat.converse()
if __name__=="__main__":
       chatbot()