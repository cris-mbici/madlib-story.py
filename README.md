# Mad Libs Story Generator
[Watch the demo](https://github.com/cris-mbici/madlib-story.py/blob/main/madlib.mp4)
. This is a basic Mad Libs-style program where the user inputs nouns, adjectives, and verbs to create a short, fun story. The program begins by prompting the user to provide words, ensuring each input contributes to the final narrative.

Once all inputs are collected, the story is dynamically generated using the provided words. The result is a humorous dialogue between two characters who debate their habits before ultimately agreeing to continue doing what they love. The final story is printed, making for a fun and interactive experience.
This is also my first python program.

# Update!
This being my first python project, I also wanted it to be the first project where I implement an interactive React UI!

[Watch the updated demo](https://github.com/cris-mbici/madlib-story.py/raw/main/madlib_updated_demo.mp4). It still has the same functionality, but now has a bare minimum User Interface. 

## What I Learned

Throughout this project, I explored several new concepts and technologies. Here are some key things I learned:

## React (Frontend)

✅ Using useState() to manage form data and track the generated story result✅ Creating reusable components like InputForm for data entry and ResultDisplay to show the story✅ Sending data to the Flask backend using fetch() with a POST request✅ Handling errors gracefully by displaying error messages when the backend fails✅ Using .map() to dynamically render form fields instead of hardcoding them

## Flask (Backend)

✅ Creating a Flask app with app = Flask(__name__)✅ Using @app.route() to define an API endpoint called /generate-story✅ Handling JSON data with request.json to receive user input from React✅ Generating a dynamic story using Python’s f-strings✅ Using jsonify() to send the generated story back to the frontend✅ Adding CORS support to allow the React frontend to communicate with the Flask backend

## General Skills

✅ Structuring my project with clear folder separation for frontend and backend✅ Debugging issues like CORS errors, incorrect API URLs, and JSON format issues✅ Understanding the flow of data from user input → backend processing → React display

## How to Run the Project

Clone this repository

 git clone <repository-url>

Backend Setup

cd backend
pip install -r requirements.txt
python app.py

Frontend Setup

cd frontend
npm install
npm start

Open your browser and visit http://localhost:3000 to try out the Madlib Story Generator.

## What's Next?

Now that I’ve learned the basics, I'm excited to:
✅ Experiment with simple styling to improve the UI

This project taught me a lot about combining Python logic with React’s dynamic UI. It was scary at first because I felt like the syntax went so far from the python I'm familiar with, but I've succeeded and gained a lot of experience in the process.




