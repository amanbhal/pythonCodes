#! /usr/bin/python

from subprocess import call

def main():
    initString = "#! /usr/bin/python\n\ndef main():\n    print \"hello world!\"\n\nif __name__ == \"__main__\":\n    main()"
    fileName = raw_input("Name of the script\n-> ")
    fileO = open(fileName+".py", "wb")
    fileO.write(initString)
    call( ['chmod','+x',fileName+'.py'] )

if __name__ == "__main__":
    main()
