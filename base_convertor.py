# i/o --------------------
N = input("ENTER value:")
print("""\n\nOPTIONS:
-------:
binary: b
octal: o
hexadecimal: x
decimal: d

~enter REQUIRED bases:-\n""")
base_init = input("from?\t:")
base_final = input("to?\t:")
# code -------------------
convert = {'b':2,    'o':8,    'x':16,    'd':10}
s = "{:"+base_final+"}"
try:
    print("converted no.: 0"+base_final+s.format(int(N,convert[base_init])))
except:
    print("invalid number entered for {} type".format(base_init))
