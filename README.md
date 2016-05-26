# book_algo-strategy
"알고리즘 문제 해결 전략: Algorithmic Problem Solving Strategies" - 인사이트(insight)  

1.Start Solving Problem
-----------------------

1\) How to solve it?
- Understanding a problem
- Redefine the problem (and Abstraction)
- Build a plan how to solve
- Verify the plan
- Carry out the plan then solve it
- Look back and find improvements

2\) Start solving a problem from simple ways

3\) < strict weak ordering  
- Irreflexivity: a < a is always False
- Asymmetry: a < b is True then b < a is False
- Transitivity: a < b is True, b < c True then a < c
- Transitivity of equivalence: a < b and a > b are False then a = b

4\) Considering floating point  
IEEE 754  
When decimal fractions changes to binary, some fractions will be unlimited <- /2 . x2 ->  
...


2.Analyse Algo
--------------

1\) Linear / Sublinear / Polynomial / Exponential time algorithm

2\) Big-O Notation

3\) NP Problem  
P(Polynomial): easy to solve  
NP(Nondeterministic Polynomial): at least, easy to check  
NP-Hard: In case NP could do reduction to something in polynomial time  
NP-Complete: NP-Hard in NP  
P=NP? (P⊂NP but NP⊂P?)  

4\) Verification
- Mathematical induction: pattern (Loop in variant with induction)  
- Proof by contradiction  
- Pigeonhole Principle: Suppose 10 pigeons enter 9 holes, Surely there is a hole which has more than 2 pigeons.
- Constructive proof: example
- Nonconstructive proof: guide (algorithm)


3.Algo Design Paradigm
----------------------
Basic: brute-force, exhausive search  
  
- Recursive function(recursion)
base case: atom  
problem and subproblem  




