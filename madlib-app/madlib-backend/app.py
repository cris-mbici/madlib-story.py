from flask import Flask, request, jsonify  # Importing Flask to build the web server
from flask_cors import CORS  # Importing CORS to let React connect to this backend

app = Flask(__name__)  # Creating the Flask app
CORS(app)  # Enables frontend-backend communication (important for React)

# Route to handle story generation (POST method because we're sending data)
@app.route('/generate-story', methods=['POST'])
def generate_story():
    # Grab the JSON data sent from the React app
    data = request.json  

    # Extract values from the incoming data (fallback to empty strings if keys are missing)
    first_noun = data.get('first_noun', '')
    first_adjective = data.get('first_adjective', '')
    first_verb = data.get('first_verb', '')
    second_noun = data.get('second_noun', '')
    second_adjective = data.get('second_adjective', '')
    second_verb = data.get('second_verb', '')

    # Build the Madlib story using f-strings (There's some recognizable python here, huge relief)
    story = f"""
    Once upon a time, there was a {first_adjective} {first_noun} who loved to {first_verb}.
    He loved {first_verb}ing so much that it annoyed {second_adjective} {second_noun} who loved {second_verb}ing.
    So they had a conversation to talk things through.
    {first_noun}: You call me {first_adjective} and say that I {first_verb} too much!
    {second_noun}: Get off that high horse! You call me {second_adjective} and say that I love {second_verb}ing too much!
    {first_noun}: Okay. I am {first_adjective} and you are {second_adjective}. Let's just do our own thing.
    {second_noun}: I'll keep {second_verb}ing and you keep {first_verb}ing.
    {first_noun}: Good
    Fin
    """

    # Send the generated story back to the React app as JSON
    return jsonify({"story": story})

# Run the Flask app only when this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Port 5000 so React can connect easily
