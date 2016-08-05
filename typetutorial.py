class Foobar:
    pass

print(type(Foobar))

foo = Foobar()
print(type(foo))

print(isinstance(foo,Foobar))
print(isinstance(Foobar,type))


MyClass = type('MyClass', (), {})
print(MyClass)

class Meta(type):
    pass

class Complex(metaclass=Meta):
    pass

print(type(Complex))

class Funky:
    def __call__(self, *args, **kwargs):
        print("Look at me, I work like a function!")

f = Funky()
f()

