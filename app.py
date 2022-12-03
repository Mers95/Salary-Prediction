import pickle
import requests

from flask import Flask, render_template,request,jsonify
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))


@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        experience =  float(request.form['exp'])
        test_score = float(request.form['t_score'])
        interview_score = float(request.form['i_score'])

    predict=model.predict([[experience,test_score,interview_score]])
    output=round(predict[0],2)
    if output<0:
        return render_template('index.html', predict_text - "sorry..")
    else:
        return render_template('index.html',predict_text="You Can  Offer {}".format(output))


if __name__=="__main__":
    app.run(debug=True)
