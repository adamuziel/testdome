import spacy


def NER_system(text, language_code):
    """
    A multi-language NER system based on the Spacy library and module.
  
    :param str text: The input string with text.
    :param str language_code: The language code to be inserted to the spacy library.
  
    """
    list_of_ents = []
    try:
        # Loading  the spacy model
        nlp = spacy.load(language_code)
    except:
        raise Exception("Language code isn't valid")
    try:
        doc = nlp(text)
        ents = doc.ents
        # iterating through the entities that were detected and inserting of the requested dictionaries to the list:
        list_of_ents = [{"text": ent.text, "type": ent.label_, "start_pos": ent.start_char, "end_pos": ent.end_char} for
                        ent in ents]
    except:
        raise Exception("Problem with the text argument")
    return list_of_ents
