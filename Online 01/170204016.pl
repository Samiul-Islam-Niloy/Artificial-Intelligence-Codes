gtp(1,1,1). gtp(8,1,2). gtp(7,1,3). gtp(2,2,1). gtp(6,2,3). gtp(3,3,1). gtp(4,3,2). gtp(5,3,3). gblnk(2,2).
tp(1,1,1). tp(4,1,3). tp(7,2,1). tp(2,2,2). tp(8,2,3). tp(6,3,1). tp(5,3,2). tp(3,3,3).
blnk(1,2).
go:- calcH(1,[],L), sumList(L,V),write('Heuristics 2 (Manhattan Distance): '),write(V).
calcH(9,X,X):-!.
calcH(T,X,Y):- dist(T,D), append(X,[D],X1), T1 is T+1, calcH(T1,X1,Y).
dist(T,V):-tp(T,A,B), gtp(T,C,D), V is abs(A-C) + abs(B-D).
sumList([],0):-!.
sumList(L,V):-L=[H|T], sumList(T,V1), V is V1+H.
