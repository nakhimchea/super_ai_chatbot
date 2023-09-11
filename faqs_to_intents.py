import os
from pandas import read_excel
import re
import numpy
import json


def main():
    print("Extract Knowledge from WingBank FAQs...")

    print("Trying get Question and Answer from Excel file...")
    general = read_excel(os.path.join('data/brain.xlsx'))
    dataframe = read_excel(os.path.join('data/Final_FAQ_Chatbot_Masterlist.xlsx'), sheet_name='Products&services 1')
    dataframe1 = read_excel(os.path.join('data/Final_FAQ_Chatbot_Masterlist.xlsx'), sheet_name='Product&Services 2')
    dataframe2 = read_excel(os.path.join('data/Final_FAQ_Chatbot_Masterlist.xlsx'), sheet_name='Product&Service 3')

    catch_name = ''
    for i in range(0, 3):
        iq_en: str = general.loc[i, 'Question EN']
        ia_en: str = general.loc[i, 'Answer EN']
        iq_km: str = general.loc[i, 'Question KM']
        ia_km: str = general.loc[i, 'Answer KM']
        catch_name = 'Welcome'
        if len(iq_en) != 0:
            iq_en_cleaned = str(iq_en).strip()
            ia_en_cleaned = str(ia_en).strip()
            iq_km_cleaned = str(iq_km).strip()
            ia_km_cleaned = str(ia_km).strip()
            data = {
                "id": "",
                "name": "({0}) {1}".format(catch_name, iq_en_cleaned)[:99],
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
                                "lang": "en",
                                "speech": [
                                    ia_en_cleaned
                                ],
                                "condition": ""
                            },
                            {
                                "type": "0",
                                "title": "",
                                "textToSpeech": "",
                                "lang": "km",
                                "speech": [
                                    ia_km_cleaned
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

            data_usersays_en = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_en_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "en",
                    "updated": 0
                }
            ]

            data_usersays_km = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_km_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "km",
                    "updated": 0
                }
            ]
            with open("intents/({0}) {1}".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json', 'w') as file:
                json.dump(data, file, indent=2)
            with open("intents/({0}) {1}_usersays_en".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json', 'w') as says_en_file:
                json.dump(data_usersays_en, says_en_file, indent=2)
            with open("intents/({0}) {1}_usersays_km".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json', 'w') as says_km_file:
                json.dump(data_usersays_km, says_km_file, indent=2)

    for i in range(0, len(dataframe)):
        iq_en: str = dataframe.loc[i, 'Questions_ENG']
        ia_en: str = dataframe.loc[i, 'Answers_ENG']
        iq_km: str = dataframe.loc[i, 'Questions_KH']
        ia_km: str = dataframe.loc[i, 'Answers_KH']
        ip_en: str = dataframe.loc[i, 'Product Name']
        if ip_en is not numpy.NaN:
            catch_name = ip_en
            catch_name = catch_name.strip()
        if len(iq_en) != 0:
            iq_en_cleaned = re.sub(r'[0-9]+', '', iq_en.strip())[1:].strip()
            ia_en_cleaned = str(ia_en).strip()
            iq_km_cleaned = re.sub(r'[0-9]+', '', iq_km.strip())[1:].strip()
            ia_km_cleaned = str(ia_km).strip()
            data = {
                "id": "",
                "name": "({0}) {1}".format(catch_name, iq_en_cleaned)[:99],
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
                                "lang": "en",
                                "speech": [
                                    ia_en_cleaned
                                ],
                                "condition": ""
                            },
                            {
                                "type": "0",
                                "title": "",
                                "textToSpeech": "",
                                "lang": "km",
                                "speech": [
                                    ia_km_cleaned
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

            data_usersays_en = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_en_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "en",
                    "updated": 0
                }
            ]

            data_usersays_km = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_km_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "km",
                    "updated": 0
                }
            ]
            with open("intents/({0}) {1}".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json', 'w') as file:
                json.dump(data, file, indent=2)
            with open("intents/({0}) {1}_usersays_en".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json', 'w') as says_en_file:
                json.dump(data_usersays_en, says_en_file, indent=2)
            with open("intents/({0}) {1}_usersays_km".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json', 'w') as says_km_file:
                json.dump(data_usersays_km, says_km_file, indent=2)

    for i in range(0, len(dataframe1)):
        iq_en: str = dataframe1.loc[i, 'Question_ENG']
        ia_en: str = dataframe1.loc[i, 'Answer_ENG']
        iq_km: str = dataframe1.loc[i, 'Question_KHM']
        ia_km: str = dataframe1.loc[i, 'Answer_KHM']
        ig_en: str = dataframe1.loc[i, 'Group']
        is_en: str = dataframe1.loc[i, 'Service Name']
        if ig_en is not numpy.NaN or is_en is not numpy.NaN:
            catch_name = (ig_en if ig_en is not numpy.NaN else '') + ' ' + (is_en if is_en is not numpy.NaN else '')
            catch_name = catch_name.strip()
            # print(catch_name)
        if len(iq_en) != 0:
            iq_en_cleaned = re.sub(r'[0-9]+', '', iq_en.strip())[1:].strip()
            ia_en_cleaned = str(ia_en).strip()
            iq_km_cleaned = re.sub(r'[0-9]+', '', iq_km.strip())[1:].strip()
            ia_km_cleaned = str(ia_km).strip()
            data = {
                "id": "",
                "name": "({0}) {1}".format(catch_name, iq_en_cleaned)[:99],
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
                                "lang": "en",
                                "speech": [
                                    ia_en_cleaned
                                ],
                                "condition": ""
                            },
                            {
                                "type": "0",
                                "title": "",
                                "textToSpeech": "",
                                "lang": "km",
                                "speech": [
                                    ia_km_cleaned
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

            data_usersays_en = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_en_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "en",
                    "updated": 0
                }
            ]

            data_usersays_km = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_km_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "km",
                    "updated": 0
                }
            ]
            with open("intents/({0}) {1}".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json',
                      'w') as file:
                json.dump(data, file, indent=2)
            with open("intents/({0}) {1}_usersays_en".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json',
                      'w') as says_en_file:
                json.dump(data_usersays_en, says_en_file, indent=2)
            with open("intents/({0}) {1}_usersays_km".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json',
                      'w') as says_km_file:
                json.dump(data_usersays_km, says_km_file, indent=2)

    for i in range(0, len(dataframe2)):
        iq_en: str = dataframe2.loc[i, 'Question_ENG']
        ia_en: str = dataframe2.loc[i, 'Answer_ENG']
        iq_km: str = dataframe2.loc[i, 'Question_KHM']
        ia_km: str = dataframe2.loc[i, 'Answer_KHM']
        is_en: str = dataframe2.loc[i, 'Service Name']
        if is_en is not numpy.NaN:
            catch_name = is_en
            catch_name = catch_name.strip()
            # print(catch_name)
        if len(iq_en) != 0:
            iq_en_cleaned = re.sub(r'[0-9]+', '', iq_en.strip())[1:].strip()
            ia_en_cleaned = str(ia_en).strip()
            iq_km_cleaned = re.sub(r'[0-9]+', '', iq_km.strip())[1:].strip()
            ia_km_cleaned = str(ia_km).strip()
            data = {
                "id": "",
                "name": "({0}) {1}".format(catch_name, iq_en_cleaned)[:99],
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
                                "lang": "en",
                                "speech": [
                                    ia_en_cleaned
                                ],
                                "condition": ""
                            },
                            {
                                "type": "0",
                                "title": "",
                                "textToSpeech": "",
                                "lang": "km",
                                "speech": [
                                    ia_km_cleaned
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

            data_usersays_en = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_en_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "en",
                    "updated": 0
                }
            ]

            data_usersays_km = [
                {
                    "id": "",
                    "data": [
                        {
                            "text": '({0}) {1}'.format(catch_name, iq_km_cleaned),
                            "userDefined": False
                        }
                    ],
                    "isTemplate": False,
                    "count": 0,
                    "lang": "km",
                    "updated": 0
                }
            ]
            with open("intents/({0}) {1}".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json',
                      'w') as file:
                json.dump(data, file, indent=2)
            with open("intents/({0}) {1}_usersays_en".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json',
                      'w') as says_en_file:
                json.dump(data_usersays_en, says_en_file, indent=2)
            with open("intents/({0}) {1}_usersays_km".format(catch_name, iq_en_cleaned.replace('/', '-')) + '.json',
                      'w') as says_km_file:
                json.dump(data_usersays_km, says_km_file, indent=2)

    print("Done Extracting Knowledge from WingBank FAQs.")


if __name__ == '__main__':
    try:
        main()
    except EOFError or KeyboardInterrupt:
        print("Main Error or Interrupted.")
