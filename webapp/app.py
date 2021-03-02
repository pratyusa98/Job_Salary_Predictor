from flask import Flask, render_template,request
import pickle
from joblib import load

app = Flask(__name__)


#Load the vectorizer and model here

labels=['Below $50,000','$50,000-$70,000','$70,000-$90,000','$90,000-$120,000','$120,000-$150,000','$150,000 and Above']
model = load('sgdclassifier.joblib')
tfidf_vectorizer = pickle.load(open('fitted_vectorizer.pickle','rb'))

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def salary_predictor():
    description = request.form.get('description')
    result = model.predict(tfidf_vectorizer.transform([description]))

    return render_template('index.html', salaryRange=labels[result[0]],
                           salary_prediction_text="The salary range of this job:")


if __name__ == '__main__':
    app.run(debug=True)












