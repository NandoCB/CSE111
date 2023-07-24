import random

def main():
    # Sentence characteristics
    characteristics = [
        ("single", "past"),
        ("single", "present"),
        ("single", "future"),
        ("plural", "past"),
        ("plural", "present"),
        ("plural", "future")
    ]

    for characteristic in characteristics:
        sentence = make_sentence(characteristic[0], characteristic[1])
        print(sentence)

def make_sentence(number, tense):
    subject = get_subject(number)
    verb = get_verb(tense)
    prepositional_phrase = get_prepositional_phrase()

    sentence = f"{subject} {verb} {prepositional_phrase}."
    return sentence

def get_subject(number):
    # Are words that replace the subject, name or noun of the sentence and are used to replace people, animals or things, without the need to name them.
    if number == "single":
        subjects = ["He", "She", "The dog", "The cat"]
    else:
        subjects = ["They", "The dogs", "The cats"]

    subject = random.choice(subjects)
    return subject

def get_verb(tense):
    # Verbs are those words that express an action, existence or state (of being) in a sentence.
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    else:
        verbs = [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_prepositional_phrase():
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun()

    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def get_preposition():
    # word used to express spatial or temporal relations, such as “in”, “over”, and “before”.
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without", "over"]

    preposition = random.choice(prepositions)
    return preposition

def get_determiner():
    # words placed in front of a noun to make it clear what the noun refers to.
    determiners = ["the", "a", "an"]

    determiner = random.choice(determiners)
    return determiner

def get_noun():
    # Words that give a name to people, places or things, though they can also refer to ideas and other abstract objects.
    nouns = ["table", "chair", "cat", "dog", "bird", "boy", "car", "child", "girl", "man", "rabbit", "woman"]

    noun = random.choice(nouns)
    return noun

# Call the main function
main()
