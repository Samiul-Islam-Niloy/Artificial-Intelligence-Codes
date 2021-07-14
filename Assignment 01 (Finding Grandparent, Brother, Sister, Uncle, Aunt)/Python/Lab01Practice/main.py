tupplelist1 = [
    ('parent', 'Hasib', 'Rakib'),
    ('parent', 'Rakib', 'Sohel'),
    ('parent', 'Rakib', 'Rebeka'),
    ('parent', 'Rashid', 'Hasib'),
    ('parent', 'Molly', 'Zisha'),
    ('parent', 'Molly', 'Wally'),
    ('parent', 'Shamsul', 'Molly'),
    ('parent', 'Dolly', 'Tonoy'),
    ('parent', 'Dolly', 'Niloy'),
    ('parent', 'Shamsul', 'Dolly'),
    ('parent', 'Shamsul', 'Russel'),
    ('parent', 'Nur', 'Niloy'),
    ('parent', 'Nur', 'Tonoy'),
    ('parent', 'Ali', 'Nur'),
    ('parent', 'Ali', 'Sobhan')
]

male = ['Wally', 'Shamsul', 'Tonoy', 'Niloy', 'Nur', 'Ali', 'Sobhan', 'Russel']
female = ['Molly', 'Zisha', 'Dolly']

def findBro(B):
    i,j,k = 0,0,0
    flag = 2
    while (i <= len(tupplelist1) - 1):
        if ((tupplelist1[i][0] == 'parent') & (tupplelist1[i][2] == B)):
            for j in range(len(tupplelist1)):
                if ((tupplelist1[j][0] == 'parent') & (tupplelist1[i][1] == tupplelist1[j][1]) & (tupplelist1[i][2] != tupplelist1[j][2])):
                    for k in range(len(male)):
                        if(male[k] == tupplelist1[j][2]):
                            print("Brother: " + tupplelist1[j][2])
                            flag = 0
                        else:
                            if(flag != 0):
                                flag = 1
        i = i + 1
    return flag

B = str(input("Enter Name: "))
flag = findBro(B)
if(flag == 1):
    print("No Brother! ")


def findSis(S):
    i,j,k = 0,0,0
    flag = 2
    while (i <= len(tupplelist1) - 1):
        if ((tupplelist1[i][0] == 'parent') & (tupplelist1[i][2] == S)):
            for j in range(len(tupplelist1)):
                if ((tupplelist1[j][0] == 'parent') & (tupplelist1[i][1] == tupplelist1[j][1]) & (tupplelist1[i][2] != tupplelist1[j][2])):
                    for k in range(len(female)):
                        if(female[k] == tupplelist1[j][2]):
                            print("Sister: " + tupplelist1[j][2])
                            flag = 0
                        else:
                            if(flag != 0):
                                flag = 1
        i = i + 1
    return flag

S = str(input("Enter Name: "))
flag = findSis(S)
if(flag == 1):
   print("No Sister! ")


def findUnc(U):
    i,j,k,l = 0,0,0,0
    flag = 2
    while (i <= len(tupplelist1) - 1):
        if ((tupplelist1[i][0] == 'parent') & (tupplelist1[i][2] == U)):
            for j in range(len(tupplelist1)):
                if ((tupplelist1[j][0] == 'parent') & (tupplelist1[i][1] == tupplelist1[j][2])):
                    for l in range(len(tupplelist1)):
                        if((tupplelist1[l][0] == 'parent') & (tupplelist1[j][1] == tupplelist1[l][1]) & (tupplelist1[i][1] != tupplelist1[l][2])):
                            for k in range(len(male)):
                                if(male[k] == tupplelist1[l][2]):
                                    print("Uncle: " + tupplelist1[l][2])
                                    flag = 0
                                else:
                                    if(flag != 0):
                                        flag = 1
        i = i + 1
    return flag

U = str(input("Enter Name: "))
flag = findUnc(U)
if(flag == 1):
   print("No Uncle! ")


def findAun(A):
    i,j,k,l = 0,0,0,0
    flag = 2
    while (i <= len(tupplelist1) - 1):
        if ((tupplelist1[i][0] == 'parent') & (tupplelist1[i][2] == A)):
            for j in range(len(tupplelist1)):
                if ((tupplelist1[j][0] == 'parent') & (tupplelist1[i][1] == tupplelist1[j][2])):
                    for l in range(len(tupplelist1)):
                        if((tupplelist1[l][0] == 'parent') & (tupplelist1[j][1] == tupplelist1[l][1]) & (tupplelist1[i][1] != tupplelist1[l][2])):
                            for k in range(len(female)):
                                if(female[k] == tupplelist1[l][2]):
                                    print("Aunt: " + tupplelist1[l][2])
                                    flag = 0
                                else:
                                    if(flag != 0):
                                        flag = 1
        i = i + 1
    return flag

A = str(input("Enter Name: "))
flag = findAun(A)
if(flag == 1):
   print("No Aunt! ")