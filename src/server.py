import threading
import time
from flask import Flask
app = Flask(__name__)

def thread_function():
  while True:
    print(".")
    time.sleep(1)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
  x = threading.Thread(target=thread_function)
  x.start()
  app.run()
