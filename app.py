from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'







# 반드시 제일 아래에/ 마지막에 실행되도록 할 것
if __name__ == '__main__':
    app.run(debug=True)