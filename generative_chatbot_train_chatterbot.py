# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:41:24 2021

@author: Hassaan
"""
from preprocessing import *
# ---------------- Importing Required Libraries ----------------
# Importing ChatBot Module from chatterbot library
from chatterbot import ChatBot  

# Importing ListTrainer from chatterbot.trainer
from chatterbot.trainers import ListTrainer

# --------------------------------------------------------------



# --------- Variables Declaration and Initialization -----------
chatbot_name = 'Jarvis'

# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome."
# ]

# providing path of files to get in preprocessing function
# Farhan's DataSet Path
path_1 = 'E:\Hassaan Bashir\Projects\Streamlit\streamlitapp\cornell_movie_dialogs_corpus\cornell movie-dialogs corpus\movie_conversations.txt'
path_2 = 'E:\Hassaan Bashir\Projects\Streamlit\streamlitapp\cornell_movie_dialogs_corpus\cornell movie-dialogs corpus\movie_lines.txt'

 
# Hassaan's DataSet Path
# path_1 = 'D:\Hassaan Bashir\Embedded C Course\FH Collaboration\cornell_movie_dialogs_corpus\cornell movie-dialogs corpus\movie_conversations.txt'
# path_2 = 'D:\Hassaan Bashir\Embedded C Course\FH Collaboration\cornell_movie_dialogs_corpus\cornell movie-dialogs corpus\movie_lines.txt'

conversation =  my_function(path_1,path_2)
# print (conversation)
# --------------------------------------------------------------



# ---------------- Initializing Library Instances --------------

# Intializing chatterbot ChatBot instance as chat_bot
chat_bot = ChatBot(
                    chatbot_name,
                    logic_adapters=[
                        {
                            "import_path": "chatterbot.logic.BestMatch",
                            'default_response': 'I am sorry, I do not understand what you are saying.',
                        }
                    ]
            )

# Initialize chatterbot Trainer instance as trainer_chat_bot
trainer_chat_bot = ListTrainer(chat_bot)

# --------------------------------------------------------------



# ------------------------- Train ChatBot ----------------------
for conv in conversation:
    print(f'Conv iteration: {conversation.index(conv)}')
    trainer_chat_bot.train(conv)
# --------------------------------------------------------------



# ------------------- Testing ChatBot Code ----------------------
while True:
    user_input = input("You: ")
    
    # Covering with in Try Except for Exception Handling
    try:
        # Check for User input if its  not Bye
        if (user_input.lower().find("bye") == -1):
            bot_response = chat_bot.get_response(user_input)
            print(f"Jarvis: {bot_response}")
            
        else:
            print("Jarvis: Bye. Nice talking to you :)")
            break

    except:
        print("User Exception from Keyboard")
        break
    # -------------------------------------------------

# --------------------------------------------------------------