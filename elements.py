class Element:
    def __init__(self, name, symbol, mass, number, group, period):
        self.name = name
        self.symbol = symbol
        self.mass = mass
        self.number = number
        self.group = group
        self.period = period
        
elements = [
        Element("Hydrogen", "H", 1.00794, 1, 1, 1),
        Element("Helium", "He", 4.002602, 2, 18, 1),
        Element("Lithium", "Li", 6.941, 3, 1, 2),
        Element("Beryllium", "Be", 9.012182, 4, 2, 2),
        Element("Boron", "B", 10.811, 5, 13, 2),
        Element("Carbon", "C", 12.0107, 6, 14, 2),
        Element("Nitrogen", "N", 14.0067, 7, 15, 2),
        Element("Oxygen", "O", 15.9994, 8, 16, 2),
        Element("Fluorine", "F", 18.9984032, 9, 17, 2),
        Element("Neon", "Ne", 20.1797, 10, 18, 2),
        Element("Sodium", "Na", 22.98976928, 11, 1, 3),
        Element("Magnesium", "Mg", 24.305, 12, 2, 3),
        Element("Aluminum", "Al", 26.9815386, 13, 13, 3),
        Element("Silicon", "Si", 28.0855, 14, 14, 3),
        Element("Phosphorus", "P", 30.973762, 15, 15, 3),
        Element("Sulfur", "S", 32.065, 16, 16, 3),
        Element("Chlorine", "Cl", 35.453, 17, 17, 3),
        Element("Argon", "Ar", 39.948, 18, 18, 3),
        Element("Potassium", "K", 39.0983, 19, 1, 4),
        Element("Calcium", "Ca", 40.078, 20, 2, 4)
    ]