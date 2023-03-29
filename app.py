from flask import Flask, render_template, redirect, request

app = Flask(__name__) #create object of Flask class

@app.route('/')
def home():
    if request.method == "GET":
        questions = ["What are the recipient's hobbies or interests?",
        "Is there a specific occasion or event that the gift is for?",
        "What is the recipient's age and gender?",
        "What is the recipient's personal style or taste?",
        "Is there a budget for the gift?"]
        return render_template('home.html', questions = questions)
    else:
        #to get answers: request.form.getlist('nameofinput')
        answers = request.form.getlist("answer")
        print(answers)
        return redirect('/')

if __name__ == '__main__': #checking if in actual application and running
    app.run(debug=True)

