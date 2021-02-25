from flask import Flask, render_template, request, jsonify
from user_inputs import UserInputs, error_response
import requests, random

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky_nums'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "speakcatacean"



@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route("/api/get-lucky-num", methods=["POST"])
def lucky_num():
    """
    get data from our API 
    call numbers API using data 
    generate json response
    """
    random_number = random.randint(1, 100)

    name = request.json["name"]
    year = request.json["year"]
    email = request.json["email"]
    color = request.json["color"]

    inputs = UserInputs(name, year, email, color)

    err_obj = error_response(inputs)
    
    if len(err_obj["errors"]) != 0:
        response_object = err_obj
        res_json = jsonify(response_object)
        return res_json

    else:
        trivia_res = requests.get(f'http://numbersapi.com/{random_number}/trivia')
        year_res = requests.get(f'http://numbersapi.com/{year}/year')

        response_object = {"num" : {"fact" : trivia_res.text, "num" : random_number},
                           "year" : {"fact" : year_res.text, "year" : year }
                          }
        res_json = jsonify(response_object)
        return res_json

    
  
    
    