from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionProvideLearningMaterial(Action):
    def name(self) -> str:
        return "action_provide_learning_material"

    def run(self, dispatcher, tracker, domain):
        subject = tracker.get_slot("subject")
        topic = tracker.get_slot("topic")
        
        # Fetch content from Beeceptor API
        content = self.get_course_content(subject, topic)
        
        dispatcher.utter_message(text=content["message"] if "message" in content else "Sorry, no content found.")
        return []

    def get_course_content(self, subject, topic):
        # Updated Beeceptor API URL
        lms_api_url = f"https://chatbot1.free.beeceptor.com/courses/{subject}/{topic}/content"
        
        try:
            # Sending a GET request to the Beeceptor API
            response = requests.get(lms_api_url, headers={'some-header': 'some-value'})
            
            if response.status_code == 200:
                # If API request is successful, return the data
                return response.json()  # Assumes API returns JSON data with a 'message' key
            else:
                # If there's an error, return a message indicating so
                return {"message": f"Sorry, there was an issue fetching content for {subject} - {topic}."}
        except Exception as e:
            # Handle exceptions such as network issues
            return {"message": f"Error fetching content: {str(e)}"}
