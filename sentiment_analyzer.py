from flask import Flask, request,jsonify,render_template
import joblib
import pickle


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        content = request.form['review']
        r = []
        r.append(content)
        # r = pd.Series(content)
        vectorizer = joblib.load('vectorizer/vectorizer1.pkl')
        review = vectorizer.transform(r)
        classifier = joblib.load('model/model_2.pkl')
        prediction = classifier.predict(review)
        if prediction == 1.0:
            sentiment = 'Positive'
            return render_template('index.html',message = "Positive😁😁")
        elif prediction == -1.0:
            sentiment = 'negative'
            return render_template('index.html',message = "Negative😡😡")
        else:
            sentiment = 'Neutral'
            return render_template('index.html',message = "Neutral🙂🙂")
    return render_template('index.html')



app.run(debug=True)



# def predict():
#     if request.method == 'POST':
#         content = request.form['review']
#         sid = SentimentIntensityAnalyzer()
#         score = sid.polarity_scores(content)
#         if (score['compound'] >= 0.0):
#             render_template('index.html',message = "Positive😁😁")
#         else:
#             render_template('index.html', message="Negative😡😡")
#
#     return render_template('index.html')

