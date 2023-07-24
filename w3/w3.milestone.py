#03 Prove Milestone: Writing Functions

# Import Random to get the random words

import random

# Define lists of words
determiners = ["the", "a", "an"]
verbs = ["ran", "jumped", "swam", "ate", "slept"]
nouns = ["dog", "cat", "bird", "man", "women"]

def get_determiner(number):
    if number == "singular":
        return random.choice(["the", "a", "an"])
    else:
        return "the"

def get_verb(number, tense):
    if tense == "past":
        return random.choice(["ran", "jumped", "swam", "ate", "slept"])
    elif tense == "present":
        if number == "singular":
            return random.choice(["runs", "jumps", "swims", "eats", "sleeps"])
        else:
            return random.choice(["run", "jump", "swim", "eat", "sleep"])
    else:
        return random.choice(["will run", "will jump", "will swim", "will eat", "will sleep"])

def get_noun(number):
    if number == "singular":
        return random.choice(["dog", "cat", "bird", "man", "women"])
    else:
        return random.choice(["dogs", "cats", "birds", "men",""])
    
def get_preposition(number):
    return random.choice(preposition)

def make_sentence(number, tense):
    determiner = get_determiner(number)
    verb = get_verb(number, tense)
    noun = get_noun(number)
    preposition = get_preposition(number)
    return f"{determiner} {noun} {verb} {preposition}."

# Main function
def main():
    #Show the 6 sentences with the requested criteria
    # Single past
    print(make_sentence("singular", "past").capitalize())
    # Single present
    print(make_sentence("singular", "present").capitalize())
    # Single future
    print(make_sentence("singular", "future").capitalize())
    # Plural past
    print(make_sentence("plural", "past").capitalize())
    # Plural present
    print(make_sentence("plural", "present").capitalize())
    # Plural future
    print(make_sentence("plural", "future").capitalize())

# Call the main function
if __name__ == '__main__':
    main()