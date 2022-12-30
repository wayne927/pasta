import sys

def run(lines):
    bigLine = ''

    for line in lines:
        words = (line.split(' '))[1:]
        thisLine = ' '.join(words)
    
        words = thisLine.split('\n')
        thisLine = ''.join(words)
    
        bigLine = bigLine + thisLine
    
    bigLine = (''.join(bigLine))[1:-3]
    
    out = '\n'.join(bigLine.split('\\\\n'))
    
    return out


if __name__ == "__main__":
    filename = sys.argv[1]
    infile = open(filename, 'r')
    lines = infile.readlines()

    dat = run(lines)

    print(dat)
