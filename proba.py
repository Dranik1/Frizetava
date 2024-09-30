
Dalibnieka_dzimums="s"
Dalibnieka_svars=51


kategorijas_siev=[51, 56, 62, 69, 300]
'''if Dalibnieka_dzimums[0]=="s":
    for i in range(6):
        a=0
        if Dalibnieka_svars in range(1, kategorijas_siev[i]):
            print(a)
            break
        elif Dalibnieka_svars in range(kategorijas_siev[i], kategorijas_siev[i+1]):
            print(a)'''
if Dalibnieka_svars in range(1, 51):
    print(Dalibnieka_dzimums)
stop=False
a=0
b=1
c=1
while stop!=True:
    if Dalibnieka_svars in range(1, kategorijas_siev[0]):
        print(c)
        stop=True
    elif Dalibnieka_svars in range(kategorijas_siev[a], kategorijas_siev[b]):
        c+=1
        print(c)
        stop=True
    else:
        a=a+1
        b=b+1
        c+=1