import openai
messages = []
file = open('APIKey.txt', 'r')
apikey = file.read().strip()
file.close()
openai.api_key = apikey


# while True:
#     # print('enter something')
#     message = input()
#     conversation = {'role':'user', 'content':message}
#     messages.append(conversation)
#     chat = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = messages)
#     reply = chat.choices[0]
#     print(reply['message']['content'])



questions = ["What are the recipient's hobbies or interests?",
    "Is there a specific occasion or event that the gift is for?",
    "What is the recipient's age and gender?",
    "What is the recipient's personal style or taste?",
    "Is there a budget for the gift?"]
answers = ['likes to run and make music', "birthday", "18 male", "not sure", "$200"]

message = f"with the questions and answers for the questions provided, find the perfect gift: questions:{questions} and coressponding answers:{answers}"
conversation = {'role':'user', 'content':message}
messages.append(conversation)
chat = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = messages)
reply = chat.choices[0]
print(reply['message']['content'])
