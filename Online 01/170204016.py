tupplelist1 = [
    ('parent', 'Rickard', 'Eddard'),
    ('parent', 'Lyarra', 'Eddard'),
    ('parent', 'Rickard', 'Brandon'),
    ('parent', 'Lyarra', 'Brandon'),
    ('parent', 'Rickard', 'Benjen'),
    ('parent', 'Lyarra', 'Benjen'),
    ('parent', 'Rickard', 'Lyanna'),
    ('parent', 'Lyarra', 'Lyanna'),
    ('parent', 'Eddard', 'Robb'),
    ('parent', 'Eddard', 'Sansa'),
    ('parent', 'Eddard', 'Arya'),
    ('parent', 'Eddard', 'Bran'),
    ('parent', 'Eddard', 'Rickon'),
    ('parent', 'Edwyle', 'Rickard')
]

male = ['Rickard', 'Eddard', 'Brandon', 'Benjen', 'Robb', 'Bran', 'Rickon', 'Edwyle']
female = ['Lyanna', 'Lyarra', 'Sansa', 'Arya']


def findGran(x):
    for i in range(len(tupplelist1)):
        if (tupplelist1[i][0] == 'parent') and (tupplelist1[i][2] == x):
            for j in range(len(tupplelist1)):
                if (tupplelist1[j][0] == 'parent') and (tupplelist1[j][2] == tupplelist1[i][1]) and (tupplelist1[j][1] in male):
                    return tupplelist1[j][1]

    return None


X = str(input('Grandchild: '))
print('Grandfather: ', end='')

grandfather = findGran(X)

if grandfather:
    print(grandfather)
else:
    print('No Grandfather!')