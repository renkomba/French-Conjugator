""" This will hold a modest library of verbs for conjugation practice. """
from random import randint, choice

""" Dictionary of verb type to verb option (10 per subgroup). """
subgroups = {
    'regular': ['meubler', 'chanter', 'danser', 'colorier', 'demander', 'poser', 'fêter', 'toucher', 'brûler', 'blesser'],
    'yer': ['payer', 'appuyer', 'balayer', 'nettoyer', 'tutoyer', 'essayer', 'essuyer', 'noyer', 'aboyer', 'ennuyer'],
    'ger': ['bouger', 'manger', 'nager', 'ranger', 'venger', 'arranger', 'loger', 'songer', 'corriger', 'envisager'],
    'cer': ['lancer', 'avancer', 'commencer', 'rincer', 'placer', 'coincer', 'balancer', 'percer', 'agacer', 'effacer'],
    'e*er': ['appeler', 'jeter', 'acheter', 'céder', 'tolérer', 'peser', 'considérer', 'élever', 'préférer', 'lever'],
    'ir': ['grossir', 'maigrir', 'finir', 'rougir', 'jaunir', 'refroidir', 'fournir', 'subir', 'âgir', 'vomir'],
    're': ['fondre', 'fendre', 'tondre', 'tendre', 'pendre', 'pondre', 'attendre', 'entendre', 'rendre', 'vendre'],
    'rir': ['souffrir', 'offrir', 'ouvrir', 'couvrir', 'découvrir'],
    'ou*oir': ['pouvoir', 'vouloir'],
    'ire': ['lire', 'conduire', 'produire', 'construire', 'dire'],
    'tre': ['battre', 'mettre', 'promettre', 'combattre', 'remettre']
    }

""" Dictionary of verb group to subgroup. Group 3 pending*. """
groups = {
    1: ('er', 'yer', 'ger', 'cer', 'e*er'),
    2: ('ir'),
    3: ('re', 'rir', 'ou*oir', 'ire', 'tre')
}

""" Use a verb group value to randomly select a verb. """
def choose_verb(group):
    if group.isnumeric():
        group_number = int(group)
    elif group.isalpha():            #if the group given matches the keys in the
        if group in subgroups:       #subgroups dictionary, use that subgroup.
            choice_of_subgroup = group
        else:                        #Otherwise, randomly choose a verb group.
            group_number = randint(1, 2)
    else:
        group_number = randint(1, 2)
    if not choice_of_subgroup:
        choice_of_group = groups[group_number] #group_number as key in groups
        choice_of_subgroup = choice(choice_of_group) #rand choose from list
    choice_of_verb_list = subgroups[choice_of_subgroup] #use above as key
    choice_of_verb = choice(choice_of_verb_list) #rand choose a listed verb
    return choice_of_verb
