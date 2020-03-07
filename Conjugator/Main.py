""" This program will conjugate any verb for any subject(s) in any tense.
It will also serve for conjugation practice: select a verb, evaluate answer,
and offer a second chance if wrong or move on and add a point if right. """

import sys
sys.path
from Verb import Verb, Subject
from First_Group import FirstGroup
from Second_Group import SecondGroup
from Third_Group import ThirdGroup
from Practice import choose_verb
from random import choice
from time import sleep

""" 3rd group "ir" verb types. """
not_ir = ("rir", "rmir", "rtir", "ntir", "ouillir", "enir", "oir", "uir")

""" Sorts the verb into its appropriate subclass. """
def create_verb(verb):
    if verb.endswith("er") and verb != "aller":
        instance = FirstGroup(verb)
    elif verb.endswith("ir") and not verb.endswith(not_ir):
        instance = SecondGroup(verb)
    else:
        instance = ThirdGroup(verb)

""" This establishes the verb groups you want to practice. """
def setup_practice():
    set = input("Options:\n'1' 1er groupe\n'2' 2e groupe\n'3' 3e groupe\n't' Tous\n")
    while not set in ("1", "2", "3", "t", ""):
        print("Érreur : cela n'était pas une option")
        set = input("Options:\n'1' 1er groupe\n'2' 2e groupe\n'3' 3e groupe\n't' Tous\n")
    if set.isalpha() or set == "":
        group = ["t"]
    elif set.isnumeric():
        if len(set) == 1:
            group = [set]
        else:
            group = [i for i in set]
            group = "t"
    return group

""" Runs the practice version of the program. """
def practice():
    group = setup_practice()
    exit = None
    score = tally = 0

    """ Practice loop """
    while exit != "o":
        retry = 0
        """ Choose a verb to conjugate """
        pc_or_user_input = choose_verb(group)
        pc_or_user_input =

given_verb = FirstGroup("nager")
persons = range(1, 7, 1)

for item in given_verb.conjugate_present(persons):
    print(item)
