from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='Templates')


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/<string:page_name>')
def hello_world2(page_name):
    return render_template(page_name)


def write_to_txt(data):
    with open('database.txt', mode='a') as db:
        email = data["Email"]
        message = data["Message"]
        file = db.write(f'\n{email},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_txt(data)
        return redirect('/Thank.html')


if __name__ == "__main__":
    app.run(debug=True)
