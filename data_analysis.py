import os
from pandas import read_excel
import numpy
import re
from difflib import SequenceMatcher


def similarity(str1: str, str2: str):
    return SequenceMatcher(None, str1, str2).ratio()


class DataAnalysis:
    @staticmethod
    def extract_faq_elements() -> tuple:
        print("---- Extracting FAQ Elements ----")
        sheet0 = read_excel(os.path.join('data/Final_FAQ_Chatbot_Masterlist.xlsx'), sheet_name='Products&services 1')
        sheet1 = read_excel(os.path.join('data/Final_FAQ_Chatbot_Masterlist.xlsx'), sheet_name='Product&Services 2')
        sheet2 = read_excel(os.path.join('data/Final_FAQ_Chatbot_Masterlist.xlsx'), sheet_name='Product&Service 3')

        l_name = []
        lq_en = []
        la_en = []
        lq_km = []
        la_km = []

        catch_name = ''
        for i in range(0, len(sheet0)):
            iq_en: str = sheet0.loc[i, 'Questions_ENG']
            ia_en: str = sheet0.loc[i, 'Answers_ENG']
            iq_km: str = sheet0.loc[i, 'Questions_KH']
            ia_km: str = sheet0.loc[i, 'Answers_KH']
            ip_en: str = sheet0.loc[i, 'Product Name']
            if ip_en is not numpy.NaN:
                catch_name = ip_en
                catch_name = catch_name.strip()
            if len(iq_en) != 0:
                iq_en_cleaned = re.sub(r'[0-9]+', '', iq_en.strip())[1:].strip()
                ia_en_cleaned = str(ia_en).strip()
                iq_km_cleaned = re.sub(r'[0-9]+', '', iq_km.strip())[1:].strip()
                ia_km_cleaned = str(ia_km).strip()

                # Insert Element from Excel Sheet 0
                l_name.append(catch_name)
                lq_en.append(iq_en_cleaned)
                la_en.append(ia_en_cleaned)
                lq_km.append(iq_km_cleaned)
                la_km.append(ia_km_cleaned)

        for i in range(0, len(sheet1)):
            iq_en: str = sheet1.loc[i, 'Question_ENG']
            ia_en: str = sheet1.loc[i, 'Answer_ENG']
            iq_km: str = sheet1.loc[i, 'Question_KHM']
            ia_km: str = sheet1.loc[i, 'Answer_KHM']
            ig_en: str = sheet1.loc[i, 'Group']
            is_en: str = sheet1.loc[i, 'Service Name']
            if ig_en is not numpy.NaN or is_en is not numpy.NaN:
                catch_name = (ig_en if ig_en is not numpy.NaN else '') + ' ' + (is_en if is_en is not numpy.NaN else '')
                catch_name = catch_name.strip()
                # print(catch_name)
            if len(iq_en) != 0:
                iq_en_cleaned = re.sub(r'[0-9]+', '', iq_en.strip())[1:].strip()
                ia_en_cleaned = str(ia_en).strip()
                iq_km_cleaned = re.sub(r'[0-9]+', '', iq_km.strip())[1:].strip()
                ia_km_cleaned = str(ia_km).strip()

                # Insert Element from Excel Sheet 0
                l_name.append(catch_name)
                lq_en.append(iq_en_cleaned)
                la_en.append(ia_en_cleaned)
                lq_km.append(iq_km_cleaned)
                la_km.append(ia_km_cleaned)

        for i in range(0, len(sheet2)):
            iq_en: str = sheet2.loc[i, 'Question_ENG']
            ia_en: str = sheet2.loc[i, 'Answer_ENG']
            iq_km: str = sheet2.loc[i, 'Question_KHM']
            ia_km: str = sheet2.loc[i, 'Answer_KHM']
            is_en: str = sheet2.loc[i, 'Service Name']
            if is_en is not numpy.NaN:
                catch_name = is_en
                catch_name = catch_name.strip()
                # print(catch_name)
            if len(iq_en) != 0:
                iq_en_cleaned = re.sub(r'[0-9]+', '', iq_en.strip())[1:].strip()
                ia_en_cleaned = str(ia_en).strip()
                iq_km_cleaned = re.sub(r'[0-9]+', '', iq_km.strip())[1:].strip()
                ia_km_cleaned = str(ia_km).strip()

                # Insert Element from Excel Sheet 0
                l_name.append(catch_name)
                lq_en.append(iq_en_cleaned)
                la_en.append(ia_en_cleaned)
                lq_km.append(iq_km_cleaned)
                la_km.append(ia_km_cleaned)

        print("++++ Done Extracting FAQ Elements ++++")
        assert len(l_name) == len(lq_en) == len(la_en) == len(lq_km) == len(la_km)
        return l_name, lq_en, la_en, lq_km, la_km

    @staticmethod
    def detect_duplicate_indices(questions: list) -> list:
        print("---- Detecting Duplicates ----")
        sq_en = []
        siq_en = []
        dq_en = []
        diq_en = []
        for i in range(0, len(questions)):
            is_duplicated = False
            for question in sq_en:
                if similarity(questions[i], question) >= 1:
                    is_duplicated = True

            if not is_duplicated:
                sq_en.append(questions[i])
                siq_en.append(i)
            else:
                dq_en.append(questions[i])
                diq_en.append(i)

        for i in range(0, len(sq_en)):
            is_duplicated = False
            for question in dq_en:
                if similarity(sq_en[i], question) >= 1:
                    is_duplicated = True
            if is_duplicated:
                diq_en.append(siq_en[i])

        print("++++ Done Detecting Duplicates ++++")
        return sorted(diq_en)
