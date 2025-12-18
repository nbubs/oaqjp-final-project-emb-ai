'''
Webapp to test emotion detection in user supplied text.
Implmented using the Python flask framework.
'''

# Imports from flask framework
from flask import Flask, render_template, request

# Import from the NLP EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector

# Intantiate the application
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    '''
    This function handles the web request to perform the emotion detection.
    The text to analyse is given in the query parameter 'textToAnalyze'
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Invoke the emotion detection
    response = emotion_detector(text_to_analyze)

    result = (
        "For the given statement, the system response is"
        f" 'anger': {response['anger']},"
        f" 'disgust': {response['disgust']},"
        f" 'fear': {response['fear']},"
        f" 'joy': {response['joy']},"
        f" and 'sadness': {response['sadness']}."
        f" The dominant emotion is {response['dominant_emotion']}."
    )
    return result


@app.route("/")
def index_page():
    ''' This function initiates the rendering of the main application
        page.
    '''
    return render_template("index.html")


# Run the application on local host, port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
