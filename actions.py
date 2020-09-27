from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUttered, FollowupAction

data = {
    "RoyInc": {
        "product1" : 1234,
        "product2" : 4567,
        "product3" : 5000,
        "product4" : 677,
    },
    "SharesInc": {
        "Mutiny" : 5000,
        "Masclow" : 9000,
        "Fiasco" : 3400,
        "Pluma" : 50000,
    }  
}

class ActionGetPrice(Action):

    def name(self) -> Text:
        return "action_get_price"

    def apply_to(self, tracker):
        tracker.trigger_follow_up_action(self.ActionEmployeeCodeInput)


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]
        print (entities)
        new_entities = {}
        for entity in entities:
            new_entities[entity["entity"]] = entity["value"]

        print (new_entities)
        try:
            dispatcher.utter_message(text=f"The price of product {new_entities['product']} is {data[new_entities['company']][new_entities['product']]}")
        except KeyError as e:
            print (e)
            dispatcher.utter_message(text="Product not found")
        return []

class ActionGetProduct(Action):

    def name(self) -> Text:
        return "action_get_product"

    def apply_to(self, tracker):
        tracker.trigger_follow_up_action(self.ActionEmployeeCodeInput)


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print (domain, tracker, dispatcher)
        dispatcher.utter_message(text="{product} is great")

        return []