# On terminal:
# export FLASK_APP=portfolio.py
# export FLASK_ENV=development
# flask run

from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_txt(data):
    with open("data.txt", mode="a+") as text_file:
        text_file.write(f'Subject: {data["subject"]}\n Email: {data["email"]}\n Message: {data["message"]}\n\n')
    text_file.close()

def write_to_csv(data):
    with open("database.csv", newline='', mode="a+") as database:
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data["email"], data["subject"], data["message"]])
    database.close()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # f'Subject: {request.form["subject"]}\n Email: {request.form["email"]}\n Message: {request.form["message"]}\n\n'
            write_to_txt(data)
            write_to_csv(data)
            return redirect('/thanksyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
