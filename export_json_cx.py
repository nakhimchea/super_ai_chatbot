from models import StructuredFAQ
import uuid
import json


class Export:
    intents = []
    transition_events = []

    def __init__(self, structured_faqs: list[StructuredFAQ]):
        self.structured_faqs = structured_faqs

    def __repr__(self):
        return repr(self.structured_faqs)

    def json_append(self):
        print("---- Appending JSON List for Dialogflow CX ----")
        for i in range(0, len(self.structured_faqs)):
            intent_id = str(uuid.uuid4())
            etag = "64f97{0}".format(intent_id[2:5])
            etags = []
            for index in range(0, len(self.intents)):
                etags.append(self.intents[index]['meta']['etag'])
            while etag in etags:
                etag = "64f97{0}".format(str(uuid.uuid4())[:3])

            intent = {
                "meta": {
                    "id": intent_id,
                    "displayName": self.structured_faqs[i].q_en,
                    "priority": 500000,
                    "etag": etag
                },
                "trainingPhrases": [{
                    "type": "EXAMPLE",
                    "parts": [{
                        "text": self.structured_faqs[i].q_en,
                        "userDefined": True
                    }],
                    "timesAddedCount": 1,
                    "lang": "en"
                }, {
                    "type": "EXAMPLE",
                    "parts": [{
                        "text": self.structured_faqs[i].q_km
                    }],
                    "timesAddedCount": 1,
                    "lang": "km"
                }]
            }
            transition_event = {
                "triggerIntentId": intent_id,
                "transitionEventHandler": {
                    "beforeTransition": {
                        "staticUserResponse": {
                            "candidates": [
                                {
                                    "selector": {
                                        "platform": ["PLATFORM_UNSPECIFIED"],
                                        "lang": "en"
                                    },
                                    "responses": [{
                                        "text": {
                                            "variants": [{
                                                "text": json.dumps(self.structured_faqs[i].a_en)
                                            }]
                                        }
                                    }]
                                },
                                {
                                    "selector": {
                                        "platform": ["PLATFORM_UNSPECIFIED"],
                                        "lang": "km"
                                    },
                                    "responses": [{
                                        "text": {
                                            "variants": [{
                                                "text": json.dumps(self.structured_faqs[i].a_km)
                                            }]
                                        }
                                    }]
                                }]
                        }
                    }
                },
                "name": str(uuid.uuid4())
            }
            self.intents.append(intent)
            self.transition_events.append(transition_event)

        print("++++ Done Appending JSON List for Dialogflow CX ++++")

    def json_export(self):
        print("---- Exporting JSON List for Dialogflow CX ----")
        with open('intents.json', 'w') as file:
            json.dump(self.intents, file, indent=2)
        with open('transitionEvents.json', 'w') as file:
            json.dump(self.transition_events, file, indent=2)
        print("++++ Done Exporting JSON List for Dialogflow CX ++++")
