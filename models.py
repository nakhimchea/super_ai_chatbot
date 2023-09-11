class FAQ:
    def __init__(self, category: str, q_en: str, a_en: str, q_km: str, a_km: str, index: int):
        self.category = category
        self.q_en = q_en
        self.a_en = a_en
        self.q_km = q_km
        self.a_km = a_km
        self.index = index

    def __repr__(self):
        return repr((self.category, self.q_en, self.a_en, self.q_km, self.a_km, self.index))

    def __len__(self):
        return len(self.q_en)


class StructuredFAQ:
    def __init__(self, q_en: str, a_en: list, q_km: str, a_km: list):
        self.q_en = q_en
        self.a_en = a_en
        self.q_km = q_km
        self.a_km = a_km

    def __repr__(self):
        return repr((self.q_en, self.a_en, self.q_km, self.a_km))

    def __len__(self):
        return len(self.q_en)
