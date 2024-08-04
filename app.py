from flask import Flask, render_template, request, jsonify
from cpp import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template('index.html')


@app.route("/answer", methods=["GET", "POST"])
def answers():
    question = request.get_json()["message"]
        
    print(question)
    
    answer = get_response(question)
    answer = answer.split(question)[-1]

    return jsonify({'answer': answer})
    
    
if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=5000, debug=True)