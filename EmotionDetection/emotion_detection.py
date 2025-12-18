'''
Emotion detection function using the Emotion Predict service of the Watson NLP Library.
'''
import json
import requests

# Define root service URL for the Watson NLP service
NLP_SERVICE = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService"

def emotion_detector(text_to_analyse ):
    '''
    Parameters:
      str: text_to_analyse  - Text to detect imotion for.
    Return:
      dict: emotion scores keyed by the emotion names: anger, disgust, fear, jo, sadness
            dominant_emotion gives the emotion with the highest score.
    '''
    # URL for the Emotion Predict service
    url = f"{NLP_SERVICE}/EmotionPredict"

    # Service request header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Service request payload 
    body = { "raw_document": { "text": text_to_analyse } }

    # Invoke service API
    response = requests.post(url, json = body, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Find dominant emotion by finding the key with the highest value in the dictionary
    dominant_emotion  = max(emotions, key = emotions.get)

    # Build the function result
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    # Return the function result
    return result