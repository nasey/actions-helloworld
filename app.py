from flask import Flask
import atexit

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def exit_handler():
    print("Shutting down Flask app...")

if __name__ == '__main__':
    atexit.register(exit_handler)
    app.run()