%Female
female(rebecca).
female(sarah).
female(sandra).
female(georgina).
female(josephine).
female(magdelena).
%Male
male(hilary).
male(dennis).
male(angelo).
male(philip).

%Parent
father(angelo,hilary).
father(angelo,dennis).
father(hilary,sarah).
father(hilary,rebecca).
father(philip,sandra).
father(philip,georgina).

mother(magdelena,hilary).
mother(magdelena,dennis).
mother(josephine,sandra).
mother(josephine,georgina).
mother(sandra,rebecca).
mother(sandra,sarah).

%RULES
sister(X,Y):-
mother(Z,X),mother(Z,Y),father(W,X),father(W,Y),female(X),(X\==Y).
brother(X,Y):-
mother(Z,X),mother(Z,Y),father(W,X),father(W,Y),male(X),(X\==Y).
parent(X,Y):-mother(X,Y);father(X,Y).
sibling(X,Y):-mother(Z,X),mother(Z,Y);father(W,X),father(W,Y).
grandparent(X,Y):-parent(Z,Y),parent(X,Z).