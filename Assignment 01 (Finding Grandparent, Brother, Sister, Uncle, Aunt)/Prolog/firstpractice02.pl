male('Wally'). male('Shamsul'). male('Tonoy'). male('Niloy'). male('Nur'). male('Ali'). male('Sobhan'). male('Russel').
female('Molly'). female('Zisha'). female('Dolly').
parent('Hasib' , 'Rakib').
parent('Rakib' , 'Sohel').
parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib').
parent('Molly' , 'Zisha').
parent('Molly' , 'Wally').
parent('Shamsul' , 'Molly').
parent('Dolly' , 'Tonoy').
parent('Dolly' , 'Niloy').
parent('Shamsul' , 'Dolly').
parent('Shamsul' , 'Russel').
parent('Nur' , 'Niloy').
parent('Nur' , 'Tonoy').
parent('Ali' , 'Nur').
parent('Ali' , 'Sobhan').

brother(X, Z):-
    parent(Y , X), parent(Y, Z), male(Z), not(X=Z).

findBro:-
    write('Name: '), read(Bro), write('Brother: '), brother(Bro, X), write(X), tab(5), fail.
findBro.


sister(X, Z):-
    parent(Y , X), parent(Y, Z), female(Z), not(X=Z).

findSis:-
    write('Name: '), read(Sis), write('Sister: '), sister(Sis, X), write(X), tab(5), fail.
findSis.


uncle(X, Z):-
    parent(Y , X), parent(D , Y), parent(D , Z), male(Z), not(Y=Z).

findUnc:-
    write('Name: '), read(Unc), write('Uncle: '), uncle(Unc, X), write(X), tab(5), fail.
findUnc.


aunt(X, Z):-
    parent(Y , X), parent(N , Y), parent(N , Z), female(Z), not(Y=Z).

findAun:-
    write('Name: '), read(Aun), write('Aunt: '), aunt(Aun, X), write(X), tab(5), fail.
findAun.
