import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.latest_message['text']

        print(f"City: {city}")

        response = f"The weather in {city} is 30°C."

        dispatcher.utter_message(text=response)
        return []

class ActionGetQA(Action):
    def name(self) -> Text:
        return "action_immigration_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        question = tracker.latest_message['text']

        response = self.get_immigration_qs(question)

        dispatcher.utter_message(text=response)
        return []

    @staticmethod
    def get_immigration_qs(question: str) -> str:

        base_url = "http://127.0.0.1:8000/api/v1/qa"
        params = {
            "prompt": question
        }

        try:
            print(f"API Request URL: {base_url}?{params}")
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            api_response = response.json()
            print(f"API Response: {api_response}")
            return api_response
        except requests.exceptions.RequestException as e:
            print(f"API Request Error: {e}")
            return None  # Return {} in case of exception