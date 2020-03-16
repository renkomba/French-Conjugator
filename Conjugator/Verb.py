class Verb:
    """ This class is for all verb objects """

    """ A list of verbs with aspirated 'h's that don't modify the subject pronoun. """
    aspirated = ("haïr")

    """ A list of vowel and silent sounds """
    vowels = ("a", "e", "i", "o", "u", "h")

    """ Dictionary of regular present endings for each verb group. """
    present_endings = {1: ("e", "es", "e", "ons", "ez", "ent"),
                        2: ("is", "is", "it", "issons", "issez", "issent"),
                        3: ("s", "s", "", "ons", "ez", "ent")}

    def __init__(self, infinitive):
        self.infinitive = infinitive
        self.stem = self.infinitive[:-2]
        self.endings = []

    def __repr__(self):
        return f"Verbe: {self.infinitive}"

    def replace_in_stem(self, stem, letter, index=-2):
        return stem[:index] + letter + stem[index+1:]

    def add_in_stem(self, stem, letter, index=-2):
        return stem[:index] + letter + stem[index:]

    def conjugate_present(self, persons):
        conjugations = []
        for person in persons:
            subject = Subject()[person]
            stem = self.stem_dict[person]
            if self.endings:
                ending = self.endings[person]
            else:
                ending = self.present_endings[self.group][person]
            if stem.startswith(self.vowels) and person in (1, 3):
                if (self.infinitive == "être" and person == 3) or (self.infinitive not in self.aspirated and person == 1):
                    subject = Subject.modify_pronoun(subject)
            conjugation = f"{subject}{stem}{ending}"
            conjugations.append(conjugation)
        return conjugations

class Subject:
    """ This class is for all subject pronouns. """
    subjects = {"je ":1, "tu ":2, "il ":3, "elle ":3, "on ":3, "ça ":3,
                "nous ":4, "vous ":5, "ils ":6, "elles ":6}

    def __init__(self):
        self.subject_dict = {1: "je ", 2: "tu ", 3: "il/elle/on/ça ",
                                4: "nous ", 5: "vous ", 6: "ils/elles "}

    def __repr__(self):
        return f"{self.subject_dict}"

    def __getitem__(self, place):
        return self.subject_dict[place]

    def modify_pronoun(pronoun):
        equivalent_pronouns = {"je ": "j'", "j'": "je ",
                                "ça ": "c'", "c'": "ça "}
        return equivalent_pronouns[pronoun]
