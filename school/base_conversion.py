# i/o
base_init = base_final = N = 0
def io():
    import os
    global base_init, base_final, N
    print("""OPTIONS:
    -------:
    binary: b
    octal: o
    hexadecimal: x
    decimal: d""")
    print("enter REQUIRED bases:",end = '\n')
    base_init = input("from?\t:")
    base_final = input("to?\t:")
    N = input("Enter no\t:")
    print("\n"*4)
    os.system('cls')
#--------------------------------------------
# dicts
convert = {
    'b':2,
    'o':8,
    'x':16,
    'd':10
}
# code
io()
s = "{:"+base_final+"}"
try:
    print("converted no.: 0"+base_final+s.format(int(N,convert[base_init])))
except:
    print("invalid number entered for {} type".format(base_init))

