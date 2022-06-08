from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return render_template ('fizzbuzz.html')

@app.route("/fizzbuzz/<int:count_to")
def fizzbuzz(count_to):
    l = []
    for i in range(0,count_to):
        if (i % 3 == 0) and (i % 5 == 0):
          l.append('Fizzbuzz')
        elif i % 3 == 0:
            l.append('Fizz')
        elif i % 5 == 0:
            l.append('Buzz')
        else:
            l.append(i)

    return render_template ('fizzbuzz.html')