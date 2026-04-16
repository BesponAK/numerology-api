from flask import Flask, request, jsonify

app = Flask(__name__)

def life_path_number(birthdate):
    digits = [int(d) for d in birthdate if d.isdigit()]
    total = sum(digits)

    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))

    return total


# 🧠 FULL READING ENGINE
def generate_reading(name, life_path):
    
    readings = {
        1: "You are built for leadership. Independence is your theme. You are here to start things others are afraid to.",
        2: "You are emotional intelligence. You read energy naturally and thrive in partnerships.",
        3: "You are expression. Creativity, communication, and visibility are your power.",
        4: "You are structure. Discipline, systems, and foundation building define your path.",
        5: "You are change. Freedom, movement, and unpredictability shape your life.",
        6: "You are responsibility. Love, family, and service are central to your journey.",
        7: "You are depth. Introspection, truth-seeking, and spiritual intelligence define you.",
        8: "You are power. Money, influence, and control of material systems are your domain.",
        9: "You are completion. You are here to let go, evolve, and uplift humanity.",
        11: "You are vision. Intuition and higher awareness guide you beyond logic.",
        22: "You are the builder. You turn vision into large-scale reality.",
        33: "You are the teacher. Healing, guidance, and service are your path."
    }

    core = readings.get(life_path, "Unknown energy pattern.")

    return f"""
{name}, here is your numerology reading:

CORE LIFE PATH:
{life_path}

ENERGY INTERPRETATION:
{core}

DIRECTION:
This number is not random — it reflects how you naturally move through life, make decisions, and attract experiences.
"""


@app.route("/")
def home():
    return "API is running"


@app.route("/reading", methods=["POST"])
def reading():
    data = request.json

    name = data["name"]
    birthdate = data["birthdate"]

    lp = life_path_number(birthdate)
    full_reading = generate_reading(name, lp)

    return jsonify({
        "name": name,
        "life_path": lp,
        "reading": full_reading
    })


if __name__ == "__main__":
    app.run()
