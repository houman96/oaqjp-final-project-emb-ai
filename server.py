"""This module does Emotion Detection."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html template.
    This is the default route for the application.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detects emotion from the provided text input.
    Returns a formatted response with emotion scores.
    If the input is blank or invalid, an error message is returned.
    """
    # Get the text from the request
    text = request.form.get('text', '')

    # Get the emotion analysis result
    result = emotion_detector(text)

    # Check if the dominant emotion is None (due to blank input)
    if result['dominant_emotion'] is None:
        return jsonify({'response': 'Invalid text! Please try again.'}), 400

    # Format the response message for valid text
    response_message = (f"For the given statement, the system response is "
                        f"'anger': {result['anger']}, "
                        f"'disgust': {result['disgust']}, "
                        f"'fear': {result['fear']}, "
                        f"'joy': {result['joy']} and "
                        f"'sadness': {result['sadness']}. "
                        f"The dominant emotion is {result['dominant_emotion']}.")

    # Return the formatted response
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
