import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# URL API
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    result = None
    
    if query:
        # درخواست به API برای دریافت معنی کلمه
        response = requests.get(f"{API_URL}/{query}")
        
        if response.status_code == 200:
            result = response.json()
        else:
            result = None
    
    return render_template('search.html', query=query, result=result)

if __name__ == '__main__':
    app.run(debug=True)
