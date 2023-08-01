import pickle
from flask import Flask,render_template,request
import pandas as pd
import numpy as np

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def get_movies(movie):    
    for i in movies['title']:
        if(movies['title'][i]==movie):
            index=i
            break
    distances = list(enumerate(similarity[index]))
    distances.sort(reverse=True,key=lambda x:x[1])
    l=distances[1:6]
    ans=[]
    for i in l:
        ans.append(movies['title'][i[0]])
        # print(movies['title'][i[0]])
    return ans
# get_movies('The Avengers')
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend',methods=['GET','POST'])
def recommend():
        m = request.args['movie']
        # return str(get_movies(m))
        return render_template('response.html',result=get_movies(m))

if __name__ == '__main__':
    app.run(debug=False)
