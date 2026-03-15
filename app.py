from flask import Flask , render_template , request
import string
import random

app = Flask(__name__)

def password_generator(length):

    characters = string.ascii_letters + string.digits + string.punctuation 

    password = ""

    for _ in range(length):
        password += random.choice(characters)
 
    return password
    
@app.route("/" , methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST" :
        length = int(request.form['length'])

        if length > 0 :
            password = password_generator(length)
        else:
            password = "Enter the valid Number"
     
    return render_template("index.html" , password=password)

if __name__ == "__main__":
    app.run(debug=True)
