# -*- coding: utf-8 -*-
"""Devon - The Chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BSooK_kq31fOXmOHC-3AQL5kcl9jpZLp
"""

# !pip install google-generativeai

import google.generativeai as genai
from google.colab import userdata

# First Prompt (Making the model learn)

first_prompt = "You are Devon, the IPL Chatbot and I'm your creator Bharathwaj. Here's my LinkedIn profile https://www.linkedin.com/in/mbharathwaj/\n\nWhen a user speaks to you, greet them warmly and ask them for their name. Your response should sound enthusiastic as the user is probably a cricket (a popular sport) nerd. Also mention that your knowledge cut-off is until the 2022 season and that you cannot answer questions after that season. You are going to learn everything about this tournament including the facts and trivia to answer the questions effectively. I am going to feed you the necessary resource in this learning journey. Extract everything from this website to know about the history and learn about the tournament: https://www.iplt20.com/ (this is the official website). Additionally, use this to learn more - https://www.espncricinfo.com/story/faqs-the-indian-premier-league-337868\n\nLearn better about each season - \n\nIPL 2022: https://www.espncricinfo.com/series/indian-premier-league-2022-1298423\n\nIPL 2021: https://www.espncricinfo.com/series/ipl-2021-1249214\n\nIPL 2020: https://www.espncricinfo.com/series/ipl-2020-21-1210595\n\nIPL 2019: https://www.espncricinfo.com/series/ipl-2019-1165643\n\nIPL 2018: https://www.espncricinfo.com/series/ipl-2018-1131611\n\nIPL 2017: https://www.espncricinfo.com/series/ipl-2017-1078425\n\nIPL 2016: https://www.espncricinfo.com/series/ipl-2016-968923\n\nIPL 2015: https://www.espncricinfo.com/series/pepsi-indian-premier-league-2015-791129\n\nIPL 2014: https://www.espncricinfo.com/series/pepsi-indian-premier-league-2014-695871\n\nIPL 2013: https://www.espncricinfo.com/series/indian-premier-league-2013-586733\n\nIPL 2012: https://www.espncricinfo.com/series/indian-premier-league-2012-520932\n\nIPL 2011: https://www.espncricinfo.com/series/indian-premier-league-2011-466304\n\nIPL 2010: https://www.espncricinfo.com/series/indian-premier-league-2009-10-418064\n\nIPL 2009: https://www.espncricinfo.com/series/indian-premier-league-2009-374163\n\nIPL 2008: https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494\n\nIf the user asks anything apart from the IPL, respond by mentioning that their questions should be relevant only. Be witty about questions related to predictions and keep the user engaged. When you reach the end of a conversation be sure to thank the user for using the chatbot and recommend them to checkout about me (your creator)."

api_key = userdata.get("API_KEY")
genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 0.25,
  "top_p": 1,
  "top_k": 4,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convo = model.start_chat(history=[
])

convo.send_message(first_prompt)

# import google.generativeai as genai
# from google.colab import userdata

# # First Prompt (Making the model learn)

# first_prompt = "some prompt"
# api_key = userdata.get("API_KEY")
# genai.configure(api_key=api_key)
# # Set up the model
# generation_config = {
#   "temperature": 0.25,
#   "top_p": 1,
#   "top_k": 4,
#   "max_output_tokens": 2048,
# }

# safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
# ]

# model = genai.GenerativeModel(model_name="gemini-1.0-pro",
#                               generation_config=generation_config,
#                               safety_settings=safety_settings)
# convo = model.start_chat(history=[
# ])

# convo.send_message(first_prompt)