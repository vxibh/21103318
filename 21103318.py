from flask import Flask, request, jsonify
import time
import random
import requests

app = Flask(__name__)

window_size = 10
stored_numbers = []

def fetch_prime():
    url = "http://20.244.56.144/test/primes"
    headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzExNTM0MzMyLCJpYXQiOjE3MTE1MzQwMzIsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjI2YWE1NzNjLWQ1YWItNGZiYS04MDI5LTY1ODY1YjcxOThjZCIsInN1YiI6IjIxMTAzMzE4QG1haWwuamlpdC5hYy5pbiJ9LCJjb21wYW55TmFtZSI6ImdvTWFydCIsImNsaWVudElEIjoiMjZhYTU3M2MtZDVhYi00ZmJhLTgwMjktNjU4NjViNzE5OGNkIiwiY2xpZW50U2VjcmV0IjoiTlBsWUl0Y3FBSWt5WlZuWSIsIm93bmVyTmFtZSI6IlZhaWJoYXYgU2hhcm1hIiwib3duZXJFbWFpbCI6IjIxMTAzMzE4QG1haWwuamlpdC5hYy5pbiIsInJvbGxObyI6IjIxMTAzMzE4In0.iZbcwNxUY1C2M0rMHZ5xaUehEcUOdluoiVRzyCtcKoo"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["prime"]
    else:
        return None


@app.route('/numbers/<numberid>', methods=['POST'])
def add_number(numberid):
    global stored_numbers
    if numberid == 'p':
        num = fetch_prime()
    elif numberid == 'f':
        num = fetch_fibonacci()
    elif numberid == 'e':
        num = fetch_even()
    elif numberid == 'r':
        num = fetch_random()
    else:
        return jsonify({"error": "Invalid number ID"}), 400
    
    if num is not None and num not in stored_numbers:
        if len(stored_numbers) >= window_size:
            stored_numbers.pop(0)
        stored_numbers.append(num)
    
    average = sum(stored_numbers) / len(stored_numbers)
    response = {
        "windowPrevState": stored_numbers[:-1],
        "windowCurrState": stored_numbers,
        "numbers": stored_numbers, 
        "avg": round(average, 2)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=9876)