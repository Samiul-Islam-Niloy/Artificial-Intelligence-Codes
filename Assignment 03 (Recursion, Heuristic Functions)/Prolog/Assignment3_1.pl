sum1(A,D,1,A):-
               !.

sum1(A,D,N,S):-
               N1 is N-1, A1 is A, D1 is D, sum1(A1,D1,N1,S1),
               S is S1+A1+(N-1)*D1.
