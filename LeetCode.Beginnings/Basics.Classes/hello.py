class Hello:

    def __init__(self, name, age=24):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}; I am {self.age} years old")


patrick = Hello('Patrick', age=60)
patrick.greet()

cedric = Hello('Cedric')
cedric.greet()

h2 = Hello('Viviane', age=59)
h2.greet()

# h1 = Hello()
