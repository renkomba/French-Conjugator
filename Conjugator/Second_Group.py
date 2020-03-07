from Verb import Verb

class SecondGroup(Verb):
    """ Subclass of 2nd group verbs. """

    """ Set up an infinitive and stem (parent class), then identify the verb
    "haïr" and give it its own endings. Establishes the group and finally
    creates a dictionary of person to stem (regular and irregular). """
    def __init__(self, infinitive):
        Verb.__init__(self, infinitive)
        if self.infinitive.endswith("haïr"):
            self.type = "haïr"
            self.endings = {1: "is", 2: "is", 3: "it", 4: "ïssons", 5: "ïssez", 6: "ïssent"}
        else:
            self.type = "ir"
        self.group = 2
        self.stem_dict = {person:self.stem for person in range(1, 7, 1)}

    """ Print verb type, group, stem, and person-to-stem dictionary. """
    def __repr__(self):
        return f"Type: {self.type}\nGroup: {self.group}\nModifications: {self.stem_dict}"
