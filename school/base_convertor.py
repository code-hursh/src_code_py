import pyperclip

# i/o --------------------
N = input("ENTER value:")
# print("""\n\nOPTIONS:
# -------:
# binary: b
# octal: o
# hexadecimal: x
# decimal: d

# ~enter REQUIRED bases:-\n""")
base_init = input("from?\t:").rstrip()
base_final = input("to?\t:").rstrip()
# code -------------------
convert = {'b':2,    'o':8,    'x':16,    'd':10}
s = "{:"+base_final+"}"
print(";"+str(base_init)+str(base_final))
try:
    value =s.format(int(N,convert[base_init]))
    print("converted no.: 0"+base_final+value)
    pyperclip.copy(value)
    print("value copied to clipboard!")
except:
    print("invalid number entered for {} type".format(base_init))
