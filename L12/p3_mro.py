"""
https://levelup.gitconnected.com/method-resolution-order-in-python-5afbaecc25e0    C3 mro algorithm
C3 MRO algorithm
MRO(A) = A + merge(L(Parent1), L(Parent2), ..., L(ParentN), Parent1, Parent2, ..., ParentN)
merge:
    - Check HEAD of L(Parent1) - it would be Parent1
    - IF HEAD doesn't appear in any tail of L(Parent2), ..., L(ParentN):
        - Append HEAD to linearized part, and remove all other occurrences
    - ELSE (if HEAD appears in some TAIL):
        - Check next list
    - Continue till process all linerizations for parents
- IF there is no, more parent linearization - completed successfully
- Otherwise, fail - it is impossible to build inheritance tree, interpretator will raise TypeError: Cannot create a consistent method resolution

HEAD - first element of the list
TAIL - all elements of the lists except HEAD
"""


class Root:
    def method(self):
        print(f"Method in Root class")


class ALevel2(Root):
    pass
    def method(self):
        print(f"Method in ALevel2 class")


class BLevel2(Root):
    pass
    def method(self):
        print(f"Method in BLevel2 class")


class ALevel1(ALevel2):
    pass
    # def method(self):
    #     print(f"Method in ALevel1 class")


class BLevel1(BLevel2):
    pass
    def method(self):
        print(f"Method in BLevel1 class")


class Child(ALevel1, BLevel1):
    pass
    # def method(self):
    #     print(f"Method in Child class")


print(Child.__mro__)
child = Child()
child.method()

"""
      Object
        ^
        |
       Root
        ^
        |
ALevel2    BLevel2
   ^          ^
   |          |
ALevel1    BLevel1
        ^
        |
      Child


Object
 Root
D   E
B   C
  A

"""


# O = object
# class X(O): pass
# class Y(O): pass
# class C(X, Y): pass
# class B(Y, X): pass
# class A(B, C): pass

"""
  O
  ^
 / \ 
X   Y
 \ /
  X
 / \
B   C
^   ^
 \ /
  A
TypeError: Cannot create a consistent method resolution
order (MRO) for bases Y, X
"""
