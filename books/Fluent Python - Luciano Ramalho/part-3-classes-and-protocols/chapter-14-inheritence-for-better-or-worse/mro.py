"""
This is an MRO demo. How many pings we will get? Number?
Extra: what will be the output here?
Tip: Look at the Leaf class and decide from there.
"""


class Root:  # <1>
    def ping(self):
        print(f'{self}.ping() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


class A(Root):  # <2>
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()


class B(Root):  # <3>
    pass
    # def ping(self):
    #     print(f'{self}.ping() in B')
    #     # super().ping()


class Leaf(A, B):  # <4>
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


leaf = Leaf()
leaf.ping()
