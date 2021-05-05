che={'H':1,
     'He':4,
     'Li':7,
     'Be':9,
     'B':11,
     'C':12,
     'N':14,
     'O':16,
     'F':19,
     'Ne':20,
     'Na':23,
     'Mg':24,
     'Al':27,
     'Si':28,
     'P':31,
     'S':32,
     'Cl':35.5,
     'Ar':40,
     'K':39,
     'Ca':40,
     'Sc':45,
     'Ti':48,
     'V':51,
     'Cr':52,
     'Mn':55,
     'Fe':56,
     'Co':59,
     'Ni':59,
     'Cu':64,
     'Zn':65,
     'Ga':70,
     'Ge':73,
     'As':75,
     'Se':79,
     'Br':80,
     'Kr':84,
     'Rb':85,
     'Sr':88,
     'Y':89,
     'Zr':91,
     'Nb':93,
     'Mo':96,
     'Tc':98}
def mole(n):
    mol=0
    for i in range(0,len(n)):
        k=ord(n[i])
        if i+2>len(n)-1:
            k_2=k
        else:
            k_2=ord(n[i+2])
        if i+1>len(n)-1:
            k_1=k
        else:
            k_1=ord(n[i+1])
        if k>=97 and k<=122:
            continue
        elif k>=48 and k<=57:
            continue
        elif k==40 or k==41:
            continue
        else:
            if k_1>=97 and k_1<=122:
                if k_2>=48 and k_2<=57:
                    numb=chr(k_2)
                    for i_1 in range(3,len(n)-i):
                        if ord(n[i+i_1])>=48 and ord(n[i+i_1])<=57:
                            numb=numb+n[i+i_1]
                        else:
                            break
                    mol=mol+int(numb)*che[n[i]+n[i+1]]
                else:
                    mol=mol+che[n[i]+n[i+1]]
            elif k_1>=48 and k_1<=57:
                num=chr(k_1)
                for i_2 in range(2,len(n)-i):
                    if ord(n[i+i_2])>=48 and ord(n[i+i_2])<=57:
                        num=num+n[i+i_2]
                    else:
                        break
                mol=mol+int(num)*che[n[i]]
            else:
                mol=mol+che[n[i]]
    return mol

def left(a):
    b=0
    for l in range(0,len(a)):
        if a[l]=='(':
            b=l
            return b
        else:
            continue
    if b==0:
        return None

def right(a):
    c=0
    for r in range(0,len(a)):
        if a[r]==')':
            c=r
            return c
        else:
            continue
    if c==0:
        return None

def calculate(n):
    if left(n)==None:
        mol_1=mole(n)
        return mol_1
    elif len(n)==right(n)+1:
        mol_2=mole(n[0:left(n)])+mole(n[left(n):right(n)])*int(n[right(n)+1])
        return mol_2
    elif ord(n[right(n)+1])<=48 or ord(n[right(n)+1])>=57:
        mol_3=mole(n)
        return mol_3
    else:
        mol_4=mole(n[0:left(n)])+mole(n[left(n):right(n)])*int(n[right(n)+1])+mole(n[right(n)+2:])
        return mol_4