a = 5
import os

os.system("py C:\\src_code_py\\school\\demo.py")



for i in range(a,a+10):
    print(a)

f = open('demo.py','a')
f.append("a="+str(a+10))

f.close()
