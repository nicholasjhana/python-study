import math

class Car:
    """
    An example class of a car from the Linux Adacemy course intro to python.



    """

    def __init__(self, engine, tires):
        """
        Use init function to initalize the class object. Engine and tires
        """
        self.engine = engine
        self.tires = tires

    def descrption(self):
        return f"A car with a {self.engine} engine, and {self.tires} tires."

    def wheel_circumference(self):
        """
        A method in Car that uses the circumference method from the Tire class.

        Here we see how composition works because Car doesn't know how to calcuate Tire detials. We have a small method that checks implementation of Car input and uses Tire to do the calculating.
        """

        if len(self.tires)>0:
            return self.tires[0].circumference()
        else:
            return 0

class Tire:
    """
    A tire represents part of a car. So can be consitered part of composition of the car.

    Composition allows us to separate concerns of one type from another. In this case, a car doesn't need to know how to calculate details for its tires. That would be the job of the Tire clas. The car class just uses this information.

    Inheritance: A class that is based off of a different class. Same type of object but based off the parent.
    """
    def __init__(self, tire_type, width, ratio, diameter, brand="", construction='R'):
        self.tire_type = tire_type
        self.width=width
        self.ratio=ratio
        self.diameter=diameter
        self.brand=brand
        self.construction=construction

    def __repr__(self):
        """
        Repr double undermethod allows us to change the way class information is printed out.
        """
        return f"{self.tire_type}{self.width}/{self.width}" + f"{self.construction}{self.diameter}"

    def circumference(self):
        """
        Circumference of the tire in inches.
        Uses a docstring test to check the implementation. Doctesting in this way prevents regresive errors.

        Doctests work by executing code inidcated by the >>> and checking versus the output (indicated with no indent) on the line below. We can run the doctest in the terminal with:
            python3 -m doctest -v <name_of_file>.py

        In the below example doctest checks that the class instantiates correctly. Then it checks the output of the circumference method.
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """

        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def _side_wall_inches(self):
        """
        We use this calculation as a hidden method. Known as a private method.

        We create this because it allows us to use in inherited classes.
        """
        return (self.width * (self.ratio / 100)) / 25.4

class SnowTire(Tire):
    """
    In this case we use inheritance ofthe Tire class because snow tire is the same 'thing' as a tire. The difference is it has some extra features/methods that dont' exist with stanard Tire class.
    """

    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        """
        We do not need to write an __init__ because we will have all the details from the Tire __init__. Becuase we want to extend the number of variables we add an __init__.

        One option is to define the init where we pass in variables in a typical way:
        #def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
            # we pass in the values dicretly to the Tire __init__ function
            #Tire.__init__(self, tire_type, width, ratio, diameter, branc, construction)
            # Then we add the extra varibales like any other __init__
            #self.chain_thickness = chain_thickness

        In the example below we make use of the super() method that calls the ini from the parent class

        """

        super().__init__(self, tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

        def circumference(self):
            """
            The circumference function specific to the snow tire class.
            We use a doctest like in the Tire class.

            >>> tire = SnowTire('P', 205, 65, 15, 2)
            >>> tire.circumference()
            92.7
            """
            total_diameter = (self._side_wall_inches() + self.chain_thickness * 2 + self.diameter)
            return round(total_diameter * math.pi, 1)

        def __repr__(self):
            """
            We want this to return exactly like the __repr__ in the Tire class and add to it that we are using a sow tire. Todo this we use the super() method.

            Super calls the method from the parent class. So in this case it is calling the __repr__ from the Tire class.
            """
            return super().__repr__() + "(Snow)"


