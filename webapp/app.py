from flask import Flask, request, render_template, redirect, url_for
from plugins.aws_utils import AWSUtils
from plugins.math_utils import isPrimeNumber

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
        instances = awsutils.retrieve_instances(name)
        return render_template('display.html', instances=instances, name=name, number=number)
    elif submit == "Deploy":
        awsutils.create_instances(name, number)
        return render_template('create.html', name=name, number=number)
    elif submit == "Terminate":
        instances = awsutils.terminate_instances(name)
        return render_template('terminate.html', instances=instances, name=name, number=number)
    elif submit == "Is Prime Number":
        is_prime_number = isPrimeNumber(number)
        return render_template('prime.html', is_prime_number=is_prime_number[0], divisible_by=is_prime_number[1], name=name, number=number)

    return render_template('main.html')
