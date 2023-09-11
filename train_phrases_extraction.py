import os
from pandas import read_excel, DataFrame
import pandas
import re
from difflib import SequenceMatcher


def similarity(str1: str, str2: str):
    return SequenceMatcher(None, str1, str2).ratio()


def main():
    print("---- Reading from File ----")
    sheet0 = read_excel(os.path.join('data/training_questions.xlsx'), sheet_name='Training Question 2')
    sheet1 = read_excel(os.path.join('data/training_questions.xlsx'), sheet_name='Training Question 3')
    print("++++ Done Reading from File ++++")

    print("---- Extracting from File ----")
    lq_training = []
    for i in range(0, len(sheet0)):
        r_tp = str(sheet0.loc[i, 'Training Questions'])
        rl_tp = r_tp.splitlines()
        rl_tp_cleaned = []
        for tp in rl_tp:
            tp_cleaned = re.sub(r'[0-9]+', '', tp.strip())[1:].strip()
            # print(tp_cleaned)
            rl_tp_cleaned.append(tp_cleaned)
        # print(rl_tp_cleaned)
        lq_training.append(rl_tp_cleaned)

    for i in range(0, len(sheet1)):
        r_tp = str(sheet1.loc[i, 'Training Questions'])
        rl_tp = r_tp.splitlines()
        rl_tp_cleaned = []
        for tp in rl_tp:
            tp_cleaned = re.sub(r'[0-9]+', '', tp.strip())[1:].strip()
            # print(tp_cleaned)
            rl_tp_cleaned.append(tp_cleaned)
        # print(rl_tp_cleaned)
        lq_training.append(rl_tp_cleaned)
    print("Previous: {}".format(len(sum(lq_training, []))))
    print("++++ Done Extracting from File ++++")

    # print("---- Flattening Data ----")
    # lq_training_flatten = sum(lq_training, [])
    # print(lq_training_flatten)
    # print(len(lq_training_flatten))
    # print("++++ Done Flattening Data ++++")

    # print("---- Checking Duplicates ----")
    # sq_en = []
    # dq_en = []
    # for i in range(0, len(lq_training_flatten)):
    #     if lq_training_flatten[i] not in sq_en:
    #         sq_en.append(lq_training_flatten[i])
    #     else:
    #         dq_en.append(lq_training_flatten[i])
    # print("SQ length: {}".format(len(sq_en)))
    # for question in sq_en:
    #     if question in set(dq_en):
    #         sq_en.remove(question)
    # print("len(set(dq)): {}".format(len(set(dq_en))))
    # print("Done SQ length: {}".format(len(sq_en)))
    # print("++++ Done Checking Duplicates ++++")

    sq_en = []
    dq_en = []
    for i in range(0, len(lq_training)):
        for question in lq_training[i]:
            is_duplicated = False
            for q in sq_en:
                if similarity(question, q) >= 1:
                    is_duplicated = True

            if not is_duplicated:
                sq_en.append(question)
            else:
                dq_en.append(question)
                lq_training[i].remove(question)
    print("Before: {}".format(len(sum(lq_training, []))))
    for i in range(0, len(lq_training)):
        for question in lq_training[i]:
            is_duplicated = False
            for q in dq_en:
                if similarity(question, q) >= 1:
                    is_duplicated = True
            if is_duplicated:
                lq_training[i].remove(question)
    print("After: {}".format(len(sum(lq_training, []))))
    print("++++ Done Checking Duplicates ++++")

    print("---- Writing to File ----")
    after_clean = []
    for i in range(0, len(lq_training)):
        after_clean.append('\n'.join(lq_training[i]))
    dataframe = DataFrame(after_clean, columns=['Cleaned Phrases'])

    with pandas.ExcelWriter("data/cleaned.xlsx", engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        cell_format = workbook.add_format({'text_wrap': True})
        worksheet.set_column('A:Z', cell_format=cell_format)

    print("++++ Done Writing to File ++++")


if __name__ == '__main__':
    try:
        main()
    except EOFError or KeyboardInterrupt:
        print("Catch error on EOF or Interrupted.")
