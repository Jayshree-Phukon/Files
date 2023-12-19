from flask import Flask, render_template, request

app = Flask(__name__)

# Function to predict heart disease based on conditions
def predict_heart_disease(age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,slope,ca,thal):
    risk_age = age > 45
    risk_cp = cp != 0
    risk_trestbps = trestbps > 130
    risk_chol = chol > 200
    risk_fbs = fbs == 1
    risk_restecg = restecg != 0
    risk_thalach = thalach < 150
    risk_exang = exang == 1
    risk_oldpeak = oldpeak > 2.0
    risk_slope = slope == 2
    risk_ca = ca>=1
    risk_thal = thal == 3

    # Define conditions for heart disease prediction
    if risk_age and risk_cp and risk_trestbps and risk_chol and risk_fbs and risk_restecg and risk_thalach and risk_exang and risk_oldpeak and risk_slope and risk_ca and risk_thal:
        return "High risk of heart disease"
    else:
        return "Low risk of heart disease"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        result = predict_heart_disease(age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,slope,ca,thal)
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)