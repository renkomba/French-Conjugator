from Verb import Verb

class ThirdGroup(Verb):
    """ Subclass of 3rd group verbs """

    """ Matching persons (keys) to a tuple for regular and irregular endings. """
    endings = {1: ("s", "s", "x", "is", "ois", "is", "ais"),
                2: ("s", "s", "x", "is", "ois", "is", "as"),
                3: ("", "t", "t", "it", "oit", "it", "a"),
                4: ("ons", "ons", "ons", "isons", "oyons", "isons", "ons"),
                5: ("ez", "ez", "ez", "isez", "oyez", "es", "ez"),
                6: ("ent", "ent", "ent", "isent", "oient", "ont", "ont")}

    """ All the irregular 1st group verb groups (keys) and the person pronouns (value) for which their stem changes. """
    irregular_groups = {"vouloir": (1, 2, 3, 6), "enir": (1, 2, 3, 6), "ire": (4, 5, 6), "aller": (1, 2, 3, 6), "quérir": (1, 2, 3, 6), "soudre": (4, 5, 6), "asseoir": (1, 2, 3, 4, 5, 6), "ttre": (1, 2, 3), "boire": (4, 5, 6), "ouillir": (1, 2, 3), "choir": (4, 5), "coudre": (4, 5, 6), "croire": (4, 5), "croître": (1, 2, 3, 4, 5, 6)}
    irregular_groups = {"bouillir": [1, 2, 3], "partir": [1, 2, 3],
                "venir": [1, 2, 3, 6], "mourir": [1, 2, 3, 6], "savoir": [1, 2, 3],
                "quérir": [1, 2, 3, 6], "devoir": [1, 2, 3, 6], "loir": [1, 2, 3],
                "recevoir": [1, 2, 3, 6], "mouvoir": [1, 2, 3, 6], "fuir": [4, 5],
                "ou*oir": [1, 2, 3, 6], "eoir": [1, 2, 3, 4, 5, 6]}

    """ 1st group present-tense endings (values) matched to a person pronoun. """
    endings = {1: "e", 2: "es", 3: "e", 4: "ons", 5: "ez", 6: "ent"}

    """ Set up an infinitive (parent class), then identify the "cer", "ger", "yer",
    and "double" types. Establishes the stem, group, and finally creates a dictionary
    of person to stem (regular and irregular). """
    def __init__(self, infinitive):
        Verb.__init__(self, infinitive)
        if infinitive in ("avoir", "être"):
            auxiliaries = {"avoir": ("ai", "as", "a", "avons", "avez", "ont"),
                            "être": ("suis", "es", "est", "sommes", "êtes", "sont")}
            self.group = None
            self.stem_dict = {person:conjugation for person,conjugation in zip(range(1, 7, 1), auxiliaries[infinitive])}
        self.group = 3
        self.stem_dict = self.establish_stems()

    def establish_stems(self):
        stem_change = []
        if self.infinitive.endswith("ir"):
            if self.stem.endswith(("t", "m", "v", "ouill")):
                if self.stem.endswith("ill"):
                    if self.infinitive.endswith("bouillir"):
                        self.type = "bouillir"
                        stem_change = [self.stem[:-3]]
                    else:
                        self.type = "illir"
                else:
                    self.type = "partir"    ## dormir, partir, sortir, etc.
                    stem_change = [self.stem[:-1]]
            elif self.stem.endswith("n"):
                self.type = "venir"         ## tenir, venir, etc.
                stem_change = [Verb.add_in_stem(self.stem, "i")]
            elif self.stem.endswith("r"):
                if self.infinitive == "mourir":
                    self.type = "mourir"
                    stem_change = [Verb.replace_in_stem(self.stem, "e", -3)]
                elif self.stem.endswith(("ér", "er")):
                    self.type = "quérir"
                    stem_change = [Verb.replace_in_stem(self.stem, "ie"), Verb.replace_in_stem(self.stem, "iè")]
                elif self.infinitive.endswith("courir"):
                    self.type = "courir"
                else:
                    self.type = "offrir"
            elif self.stem.endswith(("o", "u")):
                self.stem = self.stem[:-1]
                if self.infinitive.endswith("savoir"):
                    self.type = "savoir"
                    stem_change = [(self.stem[:-1]+"i")]
                elif self.infinitive != "revoir" and self.stem.endswith("ev"):
                    if self.infinitive.endswith("devoir"):
                        self.type = "devoir"
                        stem_change = [Verb.replace_in_stem(self.stem, "oi")]
                    elif self.infinitive.endswith("cevoir"):
                        self.type = "recevoir"
                        stem_change = [self.stem[:-3]+"çoi", self.stem[:-3]+"çoiv"]
                elif self.stem.endswith(("ouv", "oul")):
                    if self.infinitive.endswith("mouvoir"):
                        self.type = "mouvoir"
                        stem_change = [Verb.replace_in_stem(self.stem, "e", -3)[:-1], Verb.replace_in_stem(self.stem, "e", -3)]

    """ Print verb type, group, stem, and person-to-stem dictionary. """
    def __repr__(self):
        return f"Type: {self.type}\nGroup: {self.group}\nModifications: {self.stem_dict}"

    """ Creates a person-to-regular-stem dictionary, then one for stem changes.
    If the person pronoun should have an irregular stem, update the stem_dict. """
    def establish_stems(self):
        stem_dict = {i:self.stem for i in range(1, 7, 1)}
        stem_changes = self.get_present_stems()
        if stem_changes:
            for num in stem_changes:
                stem_dict[num] = stem_changes[num]
        return stem_dict

    """ Finds the penultimate letter of the stem for identifying e*er verbs and
    create a blank dictionary that will hold our stem changes. Also get a list of
    which person pronoun gets a stem change. Then, create those stems and populate
    the stem_changes dictionary with them by type. Since verbs can be "e*er" and
    "ger"/"yer"/"cer", look for the former type in all verbs. """
    def get_present_stems(self):
        stem_changes = {}
        penultimate_letter = self.stem[-2]
        where_stem_changes = self.irregular_groups.get(self.type)
        if self.type == "cer":
            stem_changes = {num:(self.stem[:-1] + "ç") for num in where_stem_changes}
        elif self.type == "ger":
            stem_changes = {num:(self.stem + "e") for num in where_stem_changes}
        elif self.type == "yer" and penultimate_letter != "e":
            stem_changes = {num:(self.stem[:-1] + "i") for num in where_stem_changes}
        if penultimate_letter in ("é", "e"):
            if self.type == "double":
                double = self.stem + self.stem[-1]
                stem_changes = {num:double for num in where_stem_changes}
            elif self.type in self.irregular_groups:
                self.type = f"{penultimate_letter}{self.type}"
                if self.type == "yer":
                    stem_changes = stem_changes
                else:
                    for num in self.irregular_groups["e*er"]:
                        if num in stem_changes:
                            stem = stem_changes[num]
                        else:
                            stem = self.stem
                        stem_changes[num] = Verb.replace_in_stem(stem, "è")
            else:
                self.type = f"{penultimate_letter}*{self.type}"
                stem = Verb.replace_in_stem(self.stem, "è")
                stem_changes = {num:stem for num in self.irregular_groups["e*er"]}
        return stem_changes
