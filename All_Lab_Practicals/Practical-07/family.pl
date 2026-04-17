% Facts (Parent relationships)
parent(john, mary).
parent(john, sam).
parent(mary, alice).
parent(mary, bob).
parent(sam, tom).

male(john).
male(sam).
male(bob).
male(tom).

female(mary).
female(alice).

% Rules

% Father
father(X, Y) :- parent(X, Y), male(X).

% Mother
mother(X, Y) :- parent(X, Y), female(X).

% Grandparent
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Brother
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), X \= Y.

% Sister
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \= Y.