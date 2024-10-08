from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'yghnsd%^&%^^(*(yfgyr9'
@app.route('/home/', methods=['GET', 'POST'])
def check_temperature():
    message = ""
    if request.method == 'POST':
        try:
            temperature = float(request.form.get('temperature'))
            if temperature <= 0:
                flash("A cold, isn’t it?", "warning")
            elif 0 < temperature < 10:
                message = "Cool."
            else:
                message = "Nice weather we’re having."
        except:
            message = "Please enter a valid number."

    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)


