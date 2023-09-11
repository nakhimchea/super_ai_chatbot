from data_analysis import *
from export_json_cx import *

from models import FAQ, StructuredFAQ


def main():
    print(">>>>>> Processing Data Analysis <<<<<<")
    l_name, lq_en, la_en, lq_km, la_km = DataAnalysis.extract_faq_elements()
    diq = DataAnalysis.detect_duplicate_indices(lq_en)

    print("---- Process DataList to Cleaned DataList ----")
    cleaned_faqs = []
    for i in range(0, len(lq_en)):
        nq_en: str
        nq_km: str
        if i in diq:
            nq_en = "{0}, {1}".format(l_name[i], lq_en[i])
            nq_km = "{0}, {1}".format(l_name[i], lq_km[i])
        else:
            nq_en = lq_en[i]
            nq_km = lq_km[i]
        cleaned_faqs.append(FAQ(l_name[i], nq_en, la_en[i], nq_km, la_km[i], i))

    dlq_en = []
    for index in diq:
        dlq_en.append(FAQ(l_name[index], lq_en[index], la_en[index], lq_km[index], la_km[index], index))
    dlq_en = sorted(dlq_en, key=lambda x: x.q_en)

    catch_question_en = ''
    catch_question_km = ''
    category_indices = []
    tl_dq = []
    for faq in dlq_en:
        if faq.q_en != catch_question_en:
            if category_indices:
                tl_dq.append((catch_question_en, catch_question_km, category_indices))
            catch_question_en = faq.q_en
            catch_question_km = faq.q_km
            category_indices = []
        category_indices.append(faq.index)
    tl_dq.append((catch_question_en, catch_question_km, category_indices))

    structured_faqs = []
    for i in range(0, len(cleaned_faqs)):
        lo_a_en = [{
            "category": str(cleaned_faqs[i].category),
            "answer": str(cleaned_faqs[i].a_en)
        }]
        lo_a_km = [{
            "category": str(cleaned_faqs[i].category),
            "answer": str(cleaned_faqs[i].a_km)
        }]
        structured_faqs.append(
            StructuredFAQ(cleaned_faqs[i].q_en, lo_a_en, cleaned_faqs[i].q_km, lo_a_km))
    for i in range(0, len(tl_dq)):
        q_en = tl_dq[i][0]
        q_km = tl_dq[i][1]

        # Study Multiple Questions
        lo_a_en = []
        lo_a_km = []
        for index in range(0, len(tl_dq[i][2])):
            lo_a_en.append({
                "category": str(l_name[tl_dq[i][2][index]]),
                "answer": str(la_en[tl_dq[i][2][index]])
            })
            lo_a_km.append({
                "question": str(l_name[tl_dq[i][2][index]]),
                "answer": str(la_km[tl_dq[i][2][index]])
            })
        structured_faqs.append(StructuredFAQ(q_en, lo_a_en, q_km, lo_a_km))
    print("++++ Done Process DataList to Cleaned DataList ++++")

    export = Export(structured_faqs)
    export.json_append()
    export.json_export()

    print(">>>>>> Done Processing Data Analysis <<<<<<")


if __name__ == "__main__":
    try:
        main()
    except EOFError or KeyboardInterrupt:
        print('Main Error or Interrupted.')
