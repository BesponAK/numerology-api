from flask import Flask, request, jsonify

app = Flask(__name__)

def life_path_number(birthdate):
    digits = [int(d) for d in birthdate if d.isdigit()]
    total = sum(digits)
    
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    
    return total

@app.route("/")
def home():
    return "API is running"

@app.route("/reading", methods=["POST"])
def reading():
    data = request.json
    name = data["name"]
    birthdate = data["birthdate"]
    
    lp = life_path_number(birthdate)

    return jsonify({
        "name": name,
        "life_path": lp
    })

if __name__ == "__main__":
    app.run()
