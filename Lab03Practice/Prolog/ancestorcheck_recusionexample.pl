parent('a','b').
parent('b','c').
parent('c','d').

ancestor(X, Y):-
    parent(X, Y), !.
ancestor(X, Y):-
    parent(X, Z), ancestor(Z, Y).

%%  Sample Queries and Outputs
%?-ancestor('a','b').
%true
%
%?-ancestor('a','d').
%true
%
%?-ancestor('c','a').
%false
%
%
%
%%    %%%%%%%%%%%%%%%%%%%%%%%%%


