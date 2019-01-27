# Cette fonction sert a trouver les synonymes sur synonyme
def chercher_synonime(driverd, mot):
    driverd.implicitly_wait(3)
    try:
        driverd.get("http://www.synonymo.fr/synonyme/" + mot)
    except Exception as e:
        return None

    try:
        conteneurmot = driverd.find_element_by_class_name("fiche")
    except Exception as e:
        return None

    try:
        motsobjects = conteneurmot.find_elements_by_class_name("word")
    except Exception as e:
        return None

    mots = []

    for motobject in motsobjects:
        motfinal = motobject.text
        mots.append(motfinal)
    return mots

# Les class suivantes sont utiliser pour organiser la traduction
class ParagraphE:
    def __init__(self, phrases_original, index):
        self.phrases_original = phrases_original
        self.index = index


class PhraseE:
    def __init__(self, phrases_original, index, index_paragraphe):
        self.phrase_final = phrases_original
        self.index = index
        self.index_paragraphe = index_paragraphe
        if phrases_original != " " and phrases_original != "":
            self.phrase_final += "."

    def changer_phrase(self, mot, index_mot):
        mots = self.phrase_final.split(" ")
        nv_phrase = ""
        indexparcouru = 0
        for motin in mots:
            if indexparcouru != index_mot:
                nv_phrase += motin
                nv_phrase += " "
                indexparcouru += 1
            else:
                nv_phrase += mot
                nv_phrase += " "
                indexparcouru += 1
        self.phrase_final = nv_phrase



class mot:
    def __init__(self, lettres_mot, index_paragraphe, index_mot):
        self.lettres_mot = lettres_mot
        self.index_phrase = index_paragraphe
        self.index_mot = index_mot


class mot_synonime:
    def __init__(self, lettres_mot, synonimes, index_paragraphe, index_mot):
        self.lettres_mot = lettres_mot
        self.index_phrase = index_paragraphe
        self.index_mot = index_mot
        self.synonimes = synonimes
