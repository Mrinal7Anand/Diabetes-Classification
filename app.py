from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def func():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def pred():
    while True:
        try:
            if request.method == 'POST':
                Glucoselevel = int(request.form['Glucose level'])
                BMI = float(request.form['BMI'])
                Age = int(request.form['Age'])
                DPF = float(request.form['Diabetes Pedigree Function'])
                BloodPressure = int(request.form['Blood Pressure'])

                result = model.predict([[Glucoselevel, BMI, Age, DPF, BloodPressure]])

                if result == 0:
                    res = "Not Diabetic"
                    return render_template("index.html", your_res = res)

                elif result == 1:
                    res = "Diabetic"
                    return render_template("index.html", your_res = res)

            break

        except ValueError:
            res = "Please Enter valid values"
            return render_template("index.html", your_res = res)

if __name__ =='__main__':
    app.static_folder = 'static'
    app.run(debug = True)
