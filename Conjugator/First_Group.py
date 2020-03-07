from Verb import Verb

class FirstGroup(Verb):
    """ Subclass of 1st group verbs """

    """ As per the French Academy's recent change, the following verbs still
    double the last consonant of their stem before adding the ending. """
    double_consonant = ("interpeler", "appeler", "jeter")

    """ All the irregular 1st group verb groups (keys) and the person pronouns (value) for which their stem changes. """
    irregular_groups = {"cer": (4), "ger": (4), "yer": (1, 2, 3, 6),
                        "e*er": (1, 2, 3, 6), "double": (1, 2, 3, 6)}

    """ Set up an infinitive and stem (parent class), then identify the "cer",
    "ger", "yer", and "double" types. Establishes the group and creates a
    dictionary of person to stem (regular and irregular). """
    def __init__(self, infinitive):
        Verb.__init__(self, infinitive)
        if self.infinitive.endswith(("cer", "ger", "yer")):
            self.type = self.infinitive[-3:]
        elif self.infinitive.endswith(self.double_consonant):
            self.type = "double"
        else:
            self.type = "er"
        self.group = 1
        self.stem_dict = self.establish_stems()

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
