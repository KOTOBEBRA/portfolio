from flask import Flask, render_template

app = Flask(__name__)

contact_information = {
    'Имя': 'Андрей',
    'Фамилия': 'Иванов',
    'Возраст': 13,
    'КлASS': 7,
    }

path = 'static/bongocat.jpg' # путь до картинок


@app.route('/')
def index():
    return render_template(
        'index.html',
        name=contact_information['Имя'],
        data=contact_information,
        photo=path
    )


if __name__ == '__main__':
    app.run(debug=True)
    
