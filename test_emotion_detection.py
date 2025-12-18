'''
Tests for emotion_detection.py module
'''
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        '''
        Test function emotion_detector() dominant emotions.
        '''
        # Test1: Test dominant is joy
        test1_response = emotion_detector("I am glad this happened")
        self.assertEqual(test1_response['dominant_emotion'], 'joy')
    
        # Test2: Test dominant is anger
        test2_response = emotion_detector("I am really mad about this")
        self.assertEqual(test2_response['dominant_emotion'], 'anger')

        # Test3: Test dominant is disgust
        test3_response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test3_response['dominant_emotion'], 'disgust')

        # Test4: Test dominant is sadness
        test4_response = emotion_detector("I am so sad about this")
        self.assertEqual(test4_response['dominant_emotion'], 'sadness')

        # Test5: Test dominant is fear
        test5_response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test5_response['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()