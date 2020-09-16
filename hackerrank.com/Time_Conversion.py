def timeConversion(s):
    if s[8] == 'P':
        t = str(int(t[:2])+12) +t[2:8]
    else:
        t = t[:8]
    return(t)
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
