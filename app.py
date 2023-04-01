from flask import Flask, render_template, redirect, request
import generate_amazon_link
import openai

file = open('APIKey.txt', 'r')
apikey = file.read().strip()
file.close()
openai.api_key = apikey
questions = ["What are the recipient's hobbies or interests?",
"Is there a specific occasion or event that the gift is for?",
"What is the recipient's age and gender?",
"What is the recipient's personal style or taste?",
"Is there a budget for the gift?"]

app = Flask(__name__) #create object of Flask class

@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template('home.html', questions = questions)
    else:
        # to get answers: request.form.getlist('nameofinput')
        answers = request.form.getlist("answer")
        messages = []
        message = f"with the questions and answers for the questions provided, give me 5 seperate perfect gifts: questions:{questions} and coressponding answers:{answers}. answer each gift idea in a new line and only give a single gift with no description."
        conversation = {'role':'user', 'content':message}
        messages.append(conversation)
        chat = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = messages)
        reply = chat.choices[0]
        # print(reply['message']['content'])
        home.perfectgift = reply['message']['content']
        home.gifts = home.perfectgift.split('\n')
        home.amazonlinks = []
        for gift in home.gifts:
            home.amazonlinks.append(generate_amazon_link.generate_amazon_link(gift))
        # print(gifts)

        return redirect('/results')

@app.route('/results', methods = ["GET","POST"])
def results():
    if request.method == "GET":
        return render_template("results.html", perfectgift=home.perfectgift, gifts = home.gifts, amazonlinks = home.amazonlinks)


if __name__ == '__main__': #checking if in actual application and running
    app.run(debug=True)

