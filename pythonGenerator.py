import string
import sys
import random

def printUsage():
    print('Usage: python pythonGenerator.py <lines> <in_file> <out_file>')
    print('    lines - Number of lines to generate per template')
    print('    in_file - that contains templates')
    quit()

def genVar():
    varLen = random.randint(1, 16)
    firstLetter = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + '_', k = 1))
    randomVar = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + '_', k = varLen))
    return firstLetter + randomVar

def genString():
    varString = random.randint(1, 64)
    randomString = ''.join(random.choices(string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation + '          ', k = varString))
    return randomString

def genNumber():
    return str(random.randint(-999999, 999999))



if len(sys.argv) != 3:
    printUsage()

try:
    n_lines = int(sys.argv[1])
except ValueError:
    printUsage()

in_file = sys.argv[2]

try:
    out_file = sys.argv[3]
except:
    pass



templates = open(in_file, 'r').readlines()

for template in templates:
    for _ in range(n_lines):
        reps = {}
        for s in range(template.count("$s")):
            reps["s"+str(s+1)] = genString()
        for n in range(template.count("$n")):
            reps["n"+str(n+1)] = genNumber()
        for v in range(template.count("$v")):
            reps["v"+str(v+1)] = genVar()

        out = string.Template(template.replace("\n", "")).substitute(reps)

        print(out)