from flask import  Flask, render_template, request
import sklearn
import joblib

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    form_data = {'test_string': ''}
    prediction = ""
    model=joblib.load("best_models/logistic_regression.pkl")

    if request.method=="POST":
        test_string=request.form.get("test_string")
        prediction = model.predict([test_string])
        return  render_template("home.html",form_data={'test_string': test_string}, prediction = prediction)
    else:
        return render_template("home.html", form_data=form_data, prediction = prediction) 


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0") # running the app and adding a broadcasting IP