import pyperclip
import os

N = input()
base_init = input().rstrip()
base_final = input().rstrip()
# code -------------------
convert = {'b':2,    'o':8,    'x':16,    'd':10}
s = "{:"+base_final+"}"
os.system('cls')
try:
    value =s.format(int(N,convert[base_init]))
    print("converted no.: 0"+base_final+value)
    pyperclip.copy(value)
    print("value copied to clipboard!")
except:
    print("invalid number entered for {} type".format(base_init))
