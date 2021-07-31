neighbor(i,a,35).
neighbor(i,b,45).
neighbor(a,c,20).
neighbor(a,d,30).
neighbor(b,d,25).
neighbor(b,e,35).
neighbor(b,f,27).
neighbor(c,d,30).
neighbor(c,g,47).
neighbor(d,g,30).
neighbor(e,g,25).

pathLength(X,Y,L):-
    neighbor(X,Y,L),!.
pathLength(X,Y,L):-
    neighbor(X,Z,L1), pathLength(Z,Y,L2), L is L1+L2.

%%  Sample Query and Output
%?-pathLength(i,g,X).
%X=102;
%X=95;
%X=100;
%X=105;

