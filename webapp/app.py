from flask import Flask, request, render_template, redirect, url_for
from plugins.aws_utils import AWSUtils
from plugins.math_utils import isPrimeNumber
from plugins.validation_utils import isNumberValid, isNameValid

app = Flask(__name__)
awsutils = AWSUtils()

@app.route('/')
def my_form():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['name']
    number = request.form['number']
    submit = request.form['submit']

    if submit == "Display":
        render = validateName(name, number)
        if render is not None: return render

        instances = awsutils.retrieve_instances(name)
        return render_template('display.html', instances=instances, name=name, number=number)
    elif submit == "Deploy":
        render = validateNumber(name, number)
        if render is not None: return render

        render = validateName(name, number)
        if render is not None: return render

        awsutils.create_instances(name, number)
        return render_template('create.html', name=name, number=number)
    elif submit == "Terminate":
        render = validateName(name, number)
        if render is not None: return render

        instances = awsutils.terminate_instances(name)
        return render_template('terminate.html', instances=instances, name=name, number=number)
    elif submit == "Is Prime Number":
        render = validateNumber(name, number)
        if render is not None: return render

        is_prime_number = isPrimeNumber(number)
        return render_template('prime.html', is_prime_number=is_prime_number[0], divisible_by=is_prime_number[1], name=name, number=number)

    return render_template('main.html')

def validateNumber(name, number):
    isNumberInputValid = isNumberValid(number)
    if not isNumberInputValid:
        return render_template('error_number.html', name=name, number=number)

def validateName(name, number):
    isNameInputValid = isNameValid(name)
    if not isNameInputValid:
        return render_template('error_name.html', name=name, number=number)
