from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        message = data ["message"]
        file = database.write(f'\n{name}, {email}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as database2:
        name = data["name"]
        email = data["email"]
        message = data ["message"]
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='"', quoting =csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return "Thank you!! You are Awesome"
        except:
            return 'ooooopppppps you did it again. Not saved to database'
    else:
        return 'you fucked up'