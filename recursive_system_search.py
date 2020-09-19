import os
from pathlib import Path
# c = 'c:\\'
print(r'Enter the directory in which you want to initialize the search: (example "e:" or "c:")')
e = input('>>>') +'\\'

text = input('input text_to_search: ')

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def check(file):
    with open(Path(file),'r',errors ='ignore') as f:
            read = f.read()
            if text in read:
                 return True
    return False



        #print(file)

def ilen(it):
    return sum(map(lambda _: 1, it))


dirs = []

P = e
a = os.walk(P)
g = ilen(a)
c = 0
a = os.walk(P)
print('checking drive E:')
printProgressBar(0, g, prefix = "Progress:", suffix = 'Complete', length = 50)
for dpath,_,names in a:
    c += 1
    printProgressBar(c, g, prefix = "Progress:", suffix = 'Complete', length = 50)
    for name in names:
             if name[-3:] == 'txt' or name[-4:] == 'docx' or name[-3:] == 'rtf':
                 dirs.append(dpath+'\\'+name)


d =[]
d = filter(check,dirs)
d = [i for i in d]
if d:
    print(len(d),"files found")
    opt = input('show?:')
    if  opt == 'y':
        for i in d:
            print(i)
else:
    print('file not found')
# from pathlib import pathlib

input('press enter to continue...')
