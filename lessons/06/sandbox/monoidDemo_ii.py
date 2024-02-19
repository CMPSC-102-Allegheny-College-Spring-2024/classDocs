class Monoid:
    def __init__(self, elements, operation, identity_element):
        self.elements = elements
        self.operation = operation
        self.identity_element = identity_element

    def is_associative(self):
        # Check if the operation is associative
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if self.operation(self.operation(a, b), c) != self.operation(a, self.operation(b, c)):
                        return False
        return True

    def has_identity_element(self):
        # Check if the identity element is valid
        for a in self.elements:
            if self.operation(self.identity_element, a) != self.operation(a, self.identity_element) != a:
                return False
        return True

    def demonstrate_properties(self):
        print(f"Set of elements: {self.elements}")
        print(f"Operation: {self.operation.__name__}")
        print(f"Identity Element: {self.identity_element}")
        print(f"Associative: {self.is_associative()}")
        print(f"Has Identity Element: {self.has_identity_element()}")
        print()

# Example 1: Boolean AND as a Monoid
def boolean_and(a, b):
    return a and b

boolean_monoid = Monoid(elements={True, False}, operation=boolean_and, identity_element=True)
boolean_monoid.demonstrate_properties()

# Example 2: String Concatenation as a Monoid
def string_concatenation(a, b):
    return a + b

string_monoid = Monoid(elements={"hello", "world", "python"}, operation=string_concatenation, identity_element="")
string_monoid.demonstrate_properties()

# Example 3: Integer Addition as a Monoid
def integer_addition(a, b):
    return a + b

integer_monoid = Monoid(elements={0, 1, 2, 3, 4}, operation=integer_addition, identity_element=0)
integer_monoid.demonstrate_properties()

# Example 4: List Concatenation as a Monoid
def list_concatenation(a, b):
    return a + b

list_monoid = Monoid(elements=[[1, 2], [3, 4], [5, 6]], operation=list_concatenation, identity_element=[])
list_monoid.demonstrate_properties()

# Example 5: Dictionary Union as a Monoid
def dict_union(a, b):
    return {**a, **b}

dict_monoid = Monoid(elements=[{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5}], operation=dict_union, identity_element={})
dict_monoid.demonstrate_properties()

