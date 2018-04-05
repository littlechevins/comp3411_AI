% Kevin Luo
% z5061845
% COMP3411 AI
% Started: 17th March
% Q1 Completed: 18th March
% Q2 Completed: 18th March  -  Updated 4 April
% Q3 Completed: 22nd March
% Q4 Completed: 5 April
% Q5 Completed: 5 April


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                             Question 1                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% f(List, List) Removes all positive numbers from a list
remove_pos([],[]).
remove_pos([Head|Tail],Sum) :-
  Head>=0,
  remove_pos(Tail,Sum).
remove_pos([Head|Tail],[Head|Sum]) :-
  remove_pos(Tail,Sum).


% Sums up all square roots in list
sum_sq([], 0).
sum_sq([X], Ret):-         % Case where negative item returns its sqr
  Ret is (X * X).
sum_sq([Item], Item * Item).
sum_sq([Head | Tail], Tas) :-
    sum_sq(Tail, Tmp),
Tas is (Head * Head) + (Tmp).

% Sums up all square roots of negative numbers in the list
sumsq_neg(List, Result):-
  remove_pos(List, Pos_list),
  sum_sq(Pos_list, Result).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                             Question 2                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% testing only
%likes(mary, apple).
%likes(mary, pear).
%likes(mary, grapes).
%likes(tim, mango).
%likes(tim, apple).
%likes(jane, apple).
%likes(jane, mango).

% f(X, List) Checks if X likes everything in the list
xlikes(_, []).
xlikes(X, [H2|T2]):-
  likes(X,H2),
  xlikes(X, T2).

% Given a list of people, calls xlikes to check if every member likes Fruit.
%all_like_all([people], Fruits):-
all_like_all(_, []).
all_like_all([], _).
all_like_all([H1|T1], Fruits):-
  xlikes(H1, Fruits),
  all_like_all(T1, Fruits).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                             Question 3                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% Returns the num and its sqrt
sqrt_pair(Num, [Num, Result]):-
    Result is sqrt(Num).


% returns sqr for a given list
recursive_sqr([], []).
recursive_sqr([H|T], [Result|Sum]):-
  sqrt_pair(H, Result),
  recursive_sqr(T, Sum).


% generates nums from N -> M where N >= M
% result is a list
high_low(M, M, [M]).
high_low(N, M, [N|T]):-
  N >= M,
  N1 is N-1,
  high_low(N1, M, T).

% Generates pairs of [Num, sqrt(Num)] from N to M
sqrt_table(N, M, Result):-
  high_low(N, M, Gen_nums),
  recursive_sqr(Gen_nums, Result).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                             Question 4                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% %checks if two numbers are successively increasing
% if_succ(A, [H|_]):-
%   write(A),
%   write(" == "),
%   write(H),
%   write("\n"),
%   (A+1) =:= H.
%
% chop_up([], []).                            % default
% chop_up([X], [X]).
%
% chop_up([H|T], [H|T]):-                   % if next value is succ, we go to iter with start var
%   if_succ(H, T),
%   write("is succ\n"),
%   chop_up(T, H, _).
%
% chop_up([H|T], [H | Result]):-                      % if next value is NOT succ
%   write("is NOT succ\n"),
%   chop_up(T, Result).
%
% chop_up([H|T], Start, [H|Return]):-            % iter with start var
%   if_succ(H, T),
%   write("is succ start\n"),
%   chop_up(T, Start, Return).
%
% chop_up([H|T], Start, [[Start | H] | Result]):-       % if iter with start var next value is NOT succ
%   write("is NOT succ start\n"),
%   chop_up(T, _, Result).

% returns the last element in list
last([], []).
last([X], X).
last([_, H2 | []], H2).
last([H1, H2 | T], X):-
  H1 + 1 =:= H2,
  last(T, X).

% returns first element in list
first([], []).
first([X], X).
first([H | _], H).

% f(List, [start, end]) Given a list, return a pair X,Y where X is start of list and Y is end
% concat List -> [First, Last] || [Single]
concat([], []).
concat([X], X).
concat(List, [First, Last]):-
  first(List, First),
  last(List, Last).

% Given a list, seperate it into a List of successive numbers and the rest of the List
% If the first number(s) are not successive then List is just the non succ
succ_remainder([X], [X], []).
succ_remainder([H1, H2 | Rmdr], [H1], [H2 | Rmdr]):-
  H1 + 1 =\= H2.
succ_remainder([H1, H2 | T], [H1 | Succ], Rmdr):-
  H1 + 1 =:= H2,
  succ_remainder([H2 | T], Succ, Rmdr).


% Given a list, concatinate all successive numbers. Concainate defined above
% Single digits are left alone
chop_up([], []).
chop_up([X], [X]).
chop_up(List, [Concated | Chopped]):-

  succ_remainder(List, Succ, Rest),
  concat(Succ, Concated),

  % write("List -> "),
  % write(List),
  % write("\n"),
  % write("Succ -> "),
  % write(Succ),
  % write("\n"),
  % write("Rest -> "),
  % write(Rest),
  % write("\n"),
  % write("Concated -> "),
  % write(Concated),
  % write("\nLoop\n"),

  chop_up(Rest, Chopped).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                             Question 5                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% Given a Value and a tree (can be nested),
% Return the OP of all leaves then recurse up and let the root become a leaf.
tree_eval(Value, tree(empty, z, empty), Value).
tree_eval(_, tree(empty, Num, empty), Num).
tree_eval(Value, tree(L, Op, R), Eval):-
  tree_eval(Value, L, L_eval),
  tree_eval(Value, R, R_eval),
  Expression =.. [Op, L_eval, R_eval],         % prolog generics?
  Eval is Expression.



% op_leaf([], []).
% op_leaf([X], getNum(X)).
