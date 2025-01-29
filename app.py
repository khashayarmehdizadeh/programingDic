from flask import Flask, render_template, request
app = Flask(__name__)

# یک دیکشنری ساده به عنوان دیتابیس
dictionary = {
    "python": {
        "description": "Python is a high-level programming language.",
        "example_code": "print('Hello, World!')"
    },
    "java": {
        "description": "Java is a class-based, object-oriented programming language.",
        "example_code": "System.out.println('Hello, World!');"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    results = []
    
    # جستجو در دیکشنری
    if query:
        for word, details in dictionary.items():
            if query.lower() in word.lower():
                results.append({"id": word, "name": word, "description": details["description"]})
    
    return render_template('search.html', query=query, results=results)

@app.route('/word/<word>')
def word_detail(word):
    word_data = dictionary.get(word)
    if word_data:
        return render_template('word_detail.html', word=word_data)
    return "کلمه یافت نشد."

if __name__ == '__main__':
    app.run(debug=True)
