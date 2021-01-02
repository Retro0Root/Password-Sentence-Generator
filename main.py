import sys, getopt
import unidecode
import random


def generatePassword(words):
    generatedSentence = ""

    while not len(generatedSentence) > 20:
        generatedSentence = generatedSentence + " " + words[random.randint(1, int(len(words)))]

    return generatePasswordFromWords(generatedSentence)


def generatePasswordFromWords(sentence):
    symbolsArray = ['@', '!', '?']

    trimmedSentence = sentence.strip()
    trimmedSentence = trimmedSentence.lower()
    trimmedSentence = trimmedSentence.title()
    trimmedSentence = unidecode.unidecode(trimmedSentence)
    trimmedSentence = trimmedSentence.replace(" ", "")
    trimmedSentence = trimmedSentence + str(random.randint(0, 100))
    trimmedSentence = trimmedSentence + symbolsArray[random.randint(0, 3)]

    return trimmedSentence


def yes_no_question(question, default_no=True):
    choices = ' [y/N]: ' if default_no else ' [Y/n]: '
    default_answer = 'n' if default_no else 'y'
    reply = str(input(question + choices)).lower().strip() or default_answer
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return False if default_no else True


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "a:")
    except getopt.GetoptError:
        print('Usage : python main.py -a <YES:NO>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            if arg.lower() == "yes":
                fileObj = open("liste_francais.txt", "r", encoding='utf-8')
                words = fileObj.read().splitlines()
                fileObj.close()

                ok = False
                generatedPassword = ""
                while not ok:
                    generatedPassword = generatePassword(words)
                    ok = yes_no_question("Est-ce que ce mot de passe vous convient : " + generatedPassword + " ? ")
                if generatedPassword is not None:
                    print("Votre mot de passe généré : " + generatedPassword)
            elif arg.lower() == "no":
                finished = False
                sentence = ""
                while not finished:
                    sentence = input('Ecrivez une phrase facile à retenir :  ')
                    sentence = str(sentence)
                    if len(sentence) > 20:
                        finished = True
                    else:
                        print("La phrase n'est pas assez longue !")

                if sentence is not None:
                    print("Votre mot de passe généré : " + generatePasswordFromWords(sentence))
            else:
                print("Mauvais argument saisi ! ")
                print('Usage : python main.py -a <YES:NO>')
                sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
