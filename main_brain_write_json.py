import os
from pandas import read_excel
import json


def main():
    print("Extract Knowledge from WingBank FAQs...")

    print("Trying get Question and Answer from Excel file...")
    dataframe = read_excel(os.path.join('data/brain.xlsx'))

    for i in range(len(dataframe)):
        iq_km: str = dataframe.loc[i, 'Question KM']
        ir_en: str = dataframe.loc[i, 'Response EN']
        ia_km: str = dataframe.loc[i, 'Answer KM']

        data = {
            "id": "",
            "name": ir_en[:99],
            "auto": True,
            "contexts": [],
            "responses": [
                {
                    "resetContexts": False,
                    "action": "",
                    "affectedContexts": [],
                    "parameters": [],
                    "messages": [
                        {
                            "type": "0",
                            "title": "",
                            "textToSpeech": "",
                            "lang": "km",
                            "speech": [
                                ia_km
                            ],
                            "condition": ""
                        }
                    ],
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": False,
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
        data_usersays = [
          {
            "id": "",
            "data": [
              {
                "text": iq_km,
                "userDefined": False
              }
            ],
            "isTemplate": False,
            "count": 0,
            "lang": "km",
            "updated": 0
          }
        ]
        with open("intents/{}.json".format(ir_en[:99]), 'w') as file:
            json.dump(data, file, indent=2)
        with open("intents/{}_usersays_km.json".format(ir_en[:99]), 'w') as says_file:
            json.dump(data_usersays, says_file, indent=2)

    print("Done Extracting Knowledge from WingBank FAQs.")


if __name__ == '__main__':
    try:
        main()
    except EOFError or KeyboardInterrupt:
        print("Main Error or Interrupted.")
