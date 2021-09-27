def define(word):

    word = word.lower()


    if word == "sports":
        return "An activity involving physical activity"

    elif word == "gear":
        return "A circular object that has teeth that rotates"

    elif word == "efficiency": 
        return "calculation of how effective something is"

    elif word == "effort":
        return "the force you are applying to try and overcome resistance"

    elif word == "resistance":
        return "effect exerted by one material object on another"

    elif word == "pulley":
        return "a simple machine that consists of a rope that fits into a groove in a wheel"

    elif word == "basketball":
        return "a type of sport that uses a ball and a 10 foot high hoop"

    elif word == "baseball":
        return "a type of sport that uses a small ball, a glove, and a bat"

    elif word == "dictionary":
        return "a book full of definitions"

    elif word == "boolean":
        return "data that is either true or false"

    else:
        return word + "is not defined in this dictionary"

print(define("Dictionary"))