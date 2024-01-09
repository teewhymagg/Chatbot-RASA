from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
import requests


# Action to reset certain slots in the conversation
class ActionResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[Dict]:

        return [SlotSet("nature_slot", None)]
        
# Action to handle city information.
class ActionChooseCity(Action):

    def name(self) -> Text:
        return "action_choose_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Retrieves the city name from the user's slot and takes the info from Wikipedia
        city = tracker.get_slot('city')
        weather_api_key = "7940f21fb567065f948386c9c9ca7971"
        weather_info = self.get_weather(city, weather_api_key) if city else ""
        wikipedia_info = self.get_wikipedia_info(city) if city else ""

        if city:
            dispatcher.utter_message(text=f"{wikipedia_info} {weather_info} \n You can book an accommodation here: https://www.booking.com/city/de/{city}.html?aid=1610684")
        else:
            dispatcher.utter_message(text="Please specify a city to get information.")

        return []
    
    # Searches weather information for the specified city 
    def get_weather(self, title, api_key):
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={title}&units=metric&appid={api_key}"
            )
            if response.status_code == 200:
                data = response.json()
                weather = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                return f"||| The current weather in {title} is {weather} with a temperature of {temperature}°C."
            else:
                return "Weather information is currently unavailable."
        except Exception as e:
            return f"An error occurred while retrieving weather data: {e}"
        
    # Searches information from Wikipedia for a given title
    def get_wikipedia_info(self, title):
        base_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "redirects": 1
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            pages = data["query"]["pages"]
            extract = next(iter(pages.values())).get("extract", "")

            # Split extract into sentences and take the first 2-3 sentences
            sentences = extract.split('. ')
            short_summary = '. '.join(sentences[:3])

            return short_summary if short_summary else f"Information about {title} is not available on Wikipedia."
        return "Failed to retrieve information from Wikipedia."

# Action to handle specific nature-related user queries
class ActionChooseSpecificNature(Action):

    def name(self) -> Text:
        return "action_choose_specific_nature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        specific_nature = tracker.get_slot('specific_nature')
        wikipedia_info = self.get_wikipedia_info(specific_nature) if specific_nature else ""

        if specific_nature:
            dispatcher.utter_message(text=f"{wikipedia_info} | You can buy Bavarian Ticket here: https://www.bahn.de/angebot/regio/laender-tickets/bayern-ticket  \nWant to get info about something else? Just type 'nature' or 'cities'.")
        else:
            dispatcher.utter_message(text="Please specify a natural feature to get information.")

        return []

    # The same as in Choose city class
    def get_wikipedia_info(self, title):
        base_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "redirects": 1
        }
        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                pages = data["query"]["pages"]
                extract = next(iter(pages.values())).get("extract", "")

                # Split extract into sentences and take the first 2-3 sentences
                sentences = extract.split('. ')
                short_summary = '. '.join(sentences[:3])

                return short_summary if short_summary else f"Information about {title} is not available on Wikipedia."
            else:
                return f"Failed to retrieve information about {title} from Wikipedia."
        except Exception as e:
            return f"An error occurred while retrieving information from Wikipedia: {e}"
        
# Action to process category choice (nature or city)
class ActionProcessCategoryChoice(Action):

    def name(self) -> Text:
        return "action_process_category_choice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category = tracker.get_slot('category')

        if category == 'nature':
            dispatcher.utter_message(text="You've chosen to explore nature. Would you like mountains, forests, or lakes?")
            
        elif category == 'cities':
            dispatcher.utter_message(text="Interested in cities? Choose a city in Bavaria.")
            
        else:
            dispatcher.utter_message(text="I'm not sure what you're interested in. Could you please specify if you're interested in nature or city?")
            return []
        
# Action to handle nature-related user queries based on the nature slot
class ActionChooseNature(Action):

    def name(self) -> Text:
        return "action_choose_nature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nature_slot = tracker.get_slot('nature_slot')

        if nature_slot == 'mountains':
            dispatcher.utter_message(text="Great choice! In Bavaria, you can visit the Zugspitze, Watzmann, or Tegelberg. Which one interests you?")
        elif nature_slot == 'forests':
            dispatcher.utter_message(text="Bavarian forests are beautiful! Would you like to know more about Spessart, Steigerwald, or Bayerischer Wald?")
        elif nature_slot == 'lakes':
            dispatcher.utter_message(text="Bavaria's lakes are stunning. Would you like to hear about Chiemsee, Starnberger See, or Ammersee?")
        else:
            dispatcher.utter_message(text="I didn't get that. Could you please specify if you're interested in mountains, forests, or lakes in Bavaria?")

        return []
    

