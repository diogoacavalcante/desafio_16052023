from flask import Flask
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def get_random_number():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_number = random.randint(1, 100)
    return f"Current Time: {current_time}\nRandom Number: {random_number}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0')