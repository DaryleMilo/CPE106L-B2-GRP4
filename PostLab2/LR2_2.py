filename = input('Enter the file name: ')
lineNum = []
with open(filename, 'r') as f:
    for line in f:
        lineNum.append(line.strip())

while True:
    print("The file contains", len(lineNum), "lines. Input 0 if you want to close the program")
    if len(lineNum) == 0:
        break
    lineNumber = int(input("Please enter a line number that you want to print: "))
    if lineNumber == 0:
        break
    elif lineNumber > len(lineNum):
        print("ERROR: Sorry, the line number must not exceed", len(lineNum))
    else:
        print("Line number",lineNumber, ":", lineNum[lineNumber - 1])