import pickle  # pip install pickle

from flask import Flask, render_template, request  # pip install flask
from requests import get

from movieRecommenderSystems import get_recommendations 

app = Flask(__name__)
file = open('model.pkl', 'rb')
svd = pickle.load(file)
file.close()


# def get_recommendations(title):
#     idx = indices[title]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:31]
#     movie_indices = [i[0] for i in sim_scores]
#     return titles.iloc[movie_indices]

# route


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        query = request.form['query']
        if(query == ""):
            return "Enter something!!"
        # a=get_recommendations('The Godfather').head(10)
        a = get_recommendations(query).head(10)
        # a = improved_recommendations(query).head(10)
        data = [i for i in a]
        print(data)
        return render_template('res.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
