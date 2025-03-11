import React, { useState } from 'react';  // Importing React and the useState hook
import './App.css'; // Need to import the CSS for styling

// Main App component
function App() {
    const [result, setResult] = useState('');  // Stores the generated story

    // Function to send data to the Flask backend
    const handleDataSubmit = async (inputData) => {
        try {
            const response = await fetch('http://localhost:5000/generate-story', {  
                // Talking to my Python backend to generate the story
                method: 'POST',  // POST request since we're sending data
                headers: { 'Content-Type': 'application/json' }, // Telling the backend we're sending JSON
                body: JSON.stringify(inputData)  // Convert input data to JSON format
            });

            if (!response.ok) throw new Error('Failed to fetch story');  // Error check in case something breaks

            const data = await response.json();  // Convert response back to JSON
            setResult(data.story);  // Display the generated story
        } catch (error) {
            setResult(`Error: ${error.message}`);  // Show error if the request fails
        }
    };

    return (
        <div className="container">
            <h1>Madlib Story Generator</h1>
            <InputForm onSubmit={handleDataSubmit} />
            <ResultDisplay result={result} />
        </div>
    );
}

// Form for user inputs
function InputForm({ onSubmit }) {
    // Stores all the user inputs
    const [formData, setFormData] = useState({
        First_Noun: '',
        First_Adjective: '',
        First_Verb: '',
        Second_Noun: '',
        Second_Adjective: '',
        Second_Verb: ''
    });

    // Updates the corresponding value when a user types in an input
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    // When the user clicks 'Generate Story', this sends the data to the backend
    const handleSubmit = (e) => {
        e.preventDefault();  // Prevents the page from refreshing (important!)
        onSubmit(formData);  // Send data to the App component
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* Looping through the form fields to avoid repetitive code */}
            {Object.keys(formData).map((key) => (
                <div key={key}>
                    <label>{key.replace('_', ' ')}:</label> {/* Makes labels more readable */}
                    <input
                        type="text"
                        name={key}
                        value={formData[key]}
                        onChange={handleChange}
                    />
                </div>
            ))}
            <button type="submit">Generate Story</button>  {/* The magic button */}
        </form>
    );
}

// Displays the final story or an error message
function ResultDisplay({ result }) {
    return (
        <div classNmae="generated-story">
            <h3>Generated Story:</h3>
            <pre>{result || 'No story yet'}</pre>  {/* Displays story if one exists */}
        </div>
    );
}

export default App;  // Export the App component so it can be used in index.js
