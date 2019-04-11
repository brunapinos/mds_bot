from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import logging
import datetime
from datetime import date

logger = logging.getLogger(__name__)

class ActionTest(Action):
    def name(self):
        return "action_integrante_horario"

    def run(self, dispatcher, tracker, domain):        
        dispatcher.utter_message("Eai to funcionando aqui")
        # name = tracker.get_slot('nome')
        # dispatcher.utter_message(name)
        # x = tracker.current_slot_values()['nome']
        # dispatcher.utter_message(x)