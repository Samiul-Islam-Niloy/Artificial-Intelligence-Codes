sum1(1,100):-
    !.

sum1(N,S):-
    N1 is N-1, sum1(N1, S1), S is S1+100+(N-1)*5.



%%    %%%%%%%%%%%%%%%%%%%%%%
%Sample Queries and Outputs
%
%
%?-sum1(2,X).
%X = 205.
%
%
%?-sum1(3,X).
%X = 315
%
%
%%    %%%%%%%%%%%%%%%%%%%%%%%
