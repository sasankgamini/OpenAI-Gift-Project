import openai
messages = []
file = open('APIKey.txt', 'r')
apikey = file.read().strip()
file.close()
openai.api_key = apikey

while True:
    print('enter something')
    message = input()
    conversation = {'role':'user', 'content':message}
    messages.append(conversation)
    chat = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = messages)
    reply = chat.choices[0]
    print(reply['message']['content'])
