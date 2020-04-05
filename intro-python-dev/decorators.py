"""
Decorators. Passing around functions and creating higher order functions.

Taking in funcitons as arguments and returning funcitions. Allow to extend funcitons with additional functionality.

Decorators are useful in code reuse. If we find something that allowsus to wrap functionality we can compose functions from funciotns without adding to the original implementation.
"""

# higher order funcitons
def inspect(func, *args):
    """
    Takes in a function. And an iterable of arguments. A variatic function.

    Funciton will wrap a function with additional information. So we haven't changed the function func, but we will see how we have extended the funciton's ability.

    """
    print(f"Running {func.__name__}")
    val=func(*args)
    print(val)
    return val

def combine(a, b):
    return a + b

"""
The above example takes in a function and evaluates it. To turn this into a decorator we need to return a function.
"""

def inspect_dec(func):
    """
    This version we create a function that returns a funciton. So when inspect_dec is evaluated it returns a function to be evaluated.
    """
    def wrapped_func(*args, **kwargs):
        print(f'Running{func.__name__}')
        val = func(*args, **kwargs)
        print(f'Result: {val}')
        return val
    return wrapped_func

@inspect_dec
def combine_dec(a, b):
    return a + b

"""
Most common decorators:
    @staticmethod
    @classmethod
    @property
"""

class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        """
        Query takes an instance of the class itself. Not an initalization of the class. So will only have information on the base url.

        This means when using this we wont create an instnce.
        Just use the class as:
            Class.query()

        """
        return cls.base_url + '?' + query_string


    @staticmethod
    def name():
        """
        A static method doesn't take in any arguments. It binds the output to the namespace of the class.

        Called with:
            Class.name
        """
        return 'Kevin Bacon'

    @property
    def full_name(self):
        """
        Property method allows us to call reference data inside the class. Its called as an attribute not as a method.

        So using this we can initalize a class and see values as an atribute.:
            user = User('Nicholas', 'Jhana')
            user.first_name
            Nicholas
            user.full_name
            Nicholas Jhana
        """
        return f"{self.first_name} {self.last_name}"
