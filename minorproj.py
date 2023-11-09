import datetime
import hashlib
from bson.objectid import ObjectId
from flask import *
from mongo import MongoDBHelper


web_app = Flask("Codejunction")


@web_app.route("/")
def index():
    return render_template('login.html')

@web_app.route("/register")
def register():
    return render_template('register.html')

@web_app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@web_app.route("/courses")
def courses():
    return render_template('courses.html')

@web_app.route("/home")
def home():
    return render_template('home.html')

@web_app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@web_app.route("/register-person", methods=['POST'])
def register_person():
    person_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
        'createdon': datetime.datetime.today()
    }
    print(person_data)
    db = MongoDBHelper(collection="codejunction")
    # Update MongoDB Helper insert function, to return result here
    result = db.insert(person_data)

    # Test the same
    person_id = result.inserted_id
    session['person_id'] = str(person_id)
    session['person_name'] = person_data['name']
    session['person_email'] = person_data['email']
    return render_template('login.html')

@web_app.route("/login-person", methods=['POST'])
def login_person():
    person_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
    }
    print(login_person)
    db = MongoDBHelper(collection="codejunction")
    documents = db.fetch(person_data)
    print(documents, type(documents))

    if len(documents) == 1:
        session['person_id'] = str(documents[0]['_id'])
        session['person_email'] = documents[0]['email']
        session['person_name'] = documents[0]['name']
        print(vars(session))
        return render_template('Home.html', email=session['person_email'], name=session['person_name'])
    else:
        return render_template('errors.html', message="Invalid Login!!! Login Again??")

#HTML Questions Start---
html_questions = [
    {
        'question_number': 1,
        'q1': 'HTML stands for -',
        'options': ['HighText Machine Language', 'HyperText and links Markup Language', 'HyperText Markup Language', 'None of these'],
        'correct_answer': 'HyperText Markup Language'
    },
    {
        'question_number': 2,
        'q1': 'The correct sequence of HTML tags for starting a webpage is -',
        'options': ['Head, Title, HTML, body', 'HTML, Body, Title, Head', 'HTML, Head, Title, Body', 'HTML, Head, Title, Body'],
        'correct_answer': 'HTML, Head, Title, Body'
    },
    {

        'question_number': 3,
        'q1': 'Which of the following element is responsible for making the text bold in HTML?',
        'options': ['<pre>', '<a>', '<b>', '<br>'],
        'correct_answer': '<b>'
    },
    {
        'question_number': 4,
        'q1': 'Which of the following tag is used for inserting the largest heading in HTML?',
        'options': ['<h3>', '<h1>', '<h5>', '<h6>'],
        'correct_answer': '<h1>'
    },
    {
        'question_number': 5,
        'q1': 'Which of the following tag is used to insert a line-break in HTML?',
        'options': ['<br>', '<a>', '<pre>', '<b>'],
        'correct_answer': '<br>'
    },
    {
        'question_number': 6,
        'q1': 'How to create an unordered list (a list with the list items in bullets) in HTML?',
        'options': ['<ul>', '<ol>', '<li>', '<i>'],
        'correct_answer': '<ul>'
    },
    {
        'question_number': 7,
        'q1': 'Which of the following element is responsible for making the text italic in HTML?',
        'options': ['<i>', '<italic>', '<it>', '<pre>'],
        'correct_answer': '<i>'
    },
    {
        'question_number':8,
        'q1': ' How to add a background color in HTML?',
        'options': ['<marquee bg color: "red">', '<marquee bg-color = "red">', '<marquee bgcolor = "red">', '<marquee color = "red">'],
        'correct_answer': '<marquee bgcolor = "red">'
    },
{
        'question_number': 9,
        'q1': '<input> is -',
        'options': ['a format tag.', 'an empty tag.', 'All of the above', 'None of the above'],
        'correct_answer': 'an empty tag.'
    },
{
        'question_number': 10,
        'q1': 'Which of the following tag is used to make the underlined text?',
        'options': ['<i>', '<ul>', '<u>', '<pre>'],
        'correct_answer': '<u>'
    },
    # Add more questions here
]

@web_app.route("/html-ques")
def htmlquiz():
    return render_template('html-ques.html', html_questions=html_questions)

@web_app.route("/htmlsubmit", methods=['POST'])
def htmlsubmit():
    score = 0
    for q1 in html_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('htmlresult.html', score=score, total=len(html_questions), html_questions=html_questions)

#HTML Questions End---

#CSS Questions Start---
css_questions = [
    {
        'question_number': 1,
        'q1': 'CSS stands for -',
        'options': ['Cascade style sheets', 'Color and style sheets', 'Cascading style sheets', 'None of these'],
        'correct_answer': 'Cascading style sheets'
    },
    {
        'question_number': 2,
        'q1': 'Which of the following is the correct syntax for referring the external style sheet?',
        'options': ['<style src = example.css>', '<style src = "example.css" >', '<stylesheet> example.css </stylesheet>', '<link rel="stylesheet" type="text/css" href="example.css">'],
        'correct_answer': '<link rel="stylesheet" type="text/css" href="example.css">'
    },
    {

        'question_number': 3,
        'q1': ' The property in CSS used to change the background color of an element is -',
        'options': ['bgcolor', 'color', 'background-color', 'All of the above'],
        'correct_answer': 'background-color'
    },
    {
        'question_number': 4,
        'q1': ' The CSS property used to control the elements font-size is -',
        'options': ['text-style', 'text-size', 'font-size', 'None of the above'],
        'correct_answer': 'font-size'
    },
    {
        'question_number': 5,
        'q1': 'The HTML attribute used to define the inline styles is -',
        'options': ['style', 'styles', 'class', 'None of the above'],
        'correct_answer': 'style'
    },
    {
        'question_number': 6,
        'q1': 'The HTML attribute used to define the internal stylesheet is -',
        'options': ['<style>', 'style', '<link>', '<script>'],
        'correct_answer': '<style>'
    },
    {
        'question_number': 7,
        'q1': ' Which of the following CSS property is used to set the background image of an element?',
        'options': ['background-attachment', 'background-image', 'background-color', 'None of the above'],
        'correct_answer': 'background-image'
    },
    {
        'question_number':8,
        'q1': 'Which of the following property is used as the shorthand property for the padding properties?',
        'options': ['padding-left', 'padding-right', 'padding', 'All of the above'],
        'correct_answer': 'padding'
    },
{
        'question_number': 9,
        'q1': ' The CSS property used to make the text bold is -',
        'options': ['font-weight : bold', 'weight: bold', 'font: bold', 'style: bold'],
        'correct_answer': 'font-weight : bold'
    },
{
        'question_number': 10,
        'q1': 'Which of the following property is used as the shorthand property of margin properties?',
        'options': ['margin-left', 'margin-right', 'margin', 'None of the above'
                                                             ''],
        'correct_answer': 'margin'
    },
    # Add more questions here
]

@web_app.route("/css-ques")
def cssquiz():
    return render_template('css-ques.html', css_questions=css_questions)

@web_app.route("/csssubmit", methods=['POST'])
def csssubmit():
    score = 0
    for q1 in css_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('cssresult.html', score=score, total=len(css_questions), css_questions=css_questions)

#CSS Questions End---

#JAVASCRIPT Questions Start---
js_questions = [
    {
        'question_number': 1,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 2,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {

        'question_number': 3,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 4,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 5,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 6,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 7,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number':8,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 9,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 10,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    # Add more questions here
]

@web_app.route("/js-ques")
def jsquiz():
    return render_template('js-ques.html', js_questions=js_questions)

@web_app.route("/jssubmit", methods=['POST'])
def jssubmit():
    score = 0
    for q1 in js_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('jsresult.html', score=score, total=len(js_questions), js_questions=js_questions)

#JAVASCRIPT Questions End---

#JAVA Questions Start---
j_questions = [
    {
        'question_number': 1,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 2,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {

        'question_number': 3,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 4,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 5,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 6,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 7,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number':8,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 9,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 10,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    # Add more questions here
]

@web_app.route("/j-ques")
def jquiz():
    return render_template('j-ques.html', j_questions=j_questions)

@web_app.route("/jsubmit", methods=['POST'])
def jsubmit():
    score = 0
    for q1 in j_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('jresult.html', score=score, total=len(j_questions), j_questions=j_questions)

#JAVA Questions End---

#C++ Questions Start---
c_questions = [
    {
        'question_number': 1,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 2,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {

        'question_number': 3,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 4,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 5,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 6,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 7,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number':8,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 9,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 10,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    # Add more questions here
]

@web_app.route("/c-ques")
def cquiz():
    return render_template('c-ques.html', c_questions=c_questions)

@web_app.route("/csubmit", methods=['POST'])
def csubmit():
    score = 0
    for q1 in c_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('cresult.html', score=score, total=len(c_questions), c_questions=c_questions)

#C++ Questions End---

#REACT Questions Start---
react_questions = [
    {
        'question_number': 1,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 2,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {

        'question_number': 3,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 4,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 5,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 6,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 7,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number':8,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 9,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 10,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    # Add more questions here
]

@web_app.route("/react-ques")
def reactquiz():
    return render_template('react-ques.html', react_questions=react_questions)

@web_app.route("/reactsubmit", methods=['POST'])
def reactsubmit():
    score = 0
    for q1 in react_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('reactresult.html', score=score, total=len(react_questions), react_questions=react_questions)

#REACT Questions End---

#PYTHON Questions Start---
python_questions = [
    {
        'question_number': 1,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 2,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {

        'question_number': 3,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 4,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 5,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 6,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 7,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number':8,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 9,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 10,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    # Add more questions here
]

@web_app.route("/python-ques")
def pythonquiz():
    return render_template('python-ques.html', python_questions=python_questions)

@web_app.route("/pythonsubmit", methods=['POST'])
def pythonsubmit():
    score = 0
    for q1 in python_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('pythonresult.html', score=score, total=len(python_questions), python_questions=python_questions)

#PYTHON Questions End---

#PHP Questions Start---
php_questions = [
    {
        'question_number': 1,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 2,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {

        'question_number': 3,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 4,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 5,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 6,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number': 7,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    {
        'question_number':8,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 9,
        'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
{
        'question_number': 10,
         'q1': 'for-',
        'options': ['Cascade', 'Color', 'Cascading', 'These'],
        'correct_answer': 'Cascading'
    },
    # Add more questions here
]

@web_app.route("/php-ques")
def phpquiz():
    return render_template('php-ques.html', php_questions=php_questions)

@web_app.route("/phpsubmit", methods=['POST'])
def phpsubmit():
    score = 0
    for q1 in php_questions:
        selected_answer = request.form.get(q1['q1'])
        if selected_answer == q1['correct_answer']:
            score += 1

    return render_template('phpresult.html', score=score, total=len(php_questions), php_questions=php_questions)

#PHP Questions End---


def main():
    # In order to use session object in flask, we need to set some key as secret_key in app
    web_app.secret_key = 'Codejunction-key-1'
    web_app.run(port=5026)

if __name__ == "__main__":
    main()
