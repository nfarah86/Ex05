import sys
import string

def readCharacters(variousFileObjects):
    readFileText = variousFileObjects.read().lower()
    print readFileText
    alpha = string.ascii_lowercase
    for char in alpha:
        print readFileText.count(char)


    #for line in variousFileObjects:







def main():
    fileObject = open(sys.argv[1])
    readCharacters(fileObject)


if __name__ == "__main__":
    main()