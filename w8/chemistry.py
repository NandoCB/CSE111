from collections import namedtuple


def make_periodic_table():
    
    Element = namedtuple("Element", ["name", "symbol", "atomic_mass"])
    table = {
         "Ac": Element("Actinium", "Ac", 227),
         "Ag": Element("Silver", "Ag", 107.8682),
         "Al": Element("Aluminum", "Al", 26.9815386),
         "Ar": Element("Argon", "Ar", 39.948),
         "As": Element("Arsenic", "As", 74.9216),
         "At": Element("Astatine", "At", 210),
         "Au": Element("Gold", "Au", 196.966569),
         "B": Element("Boron", "B", 10.811),
         "Ba": Element("Barium", "Ba", 137.327),
         "Be": Element("Beryllium", "Be", 9.012182),
         "Bi": Element("Bismuth", "Bi", 208.9804),
         "Br": Element("Bromine", "Br", 79.904),
         "C": Element("Carbon", "C", 12.0107),
         "Ca": Element("Calcium", "Ca", 40.078),
         "Cd": Element("Cadmium", "Cd", 112.411),
         "Ce": Element("Cerium", "Ce", 140.116),
         "Cl": Element("Chlorine", "Cl", 35.453),
         "Co": Element("Cobalt", "Co", 58.933195),
         "Cr": Element("Chromium", "Cr", 51.9961),
         "Cs": Element("Cesium", "Cs", 132.9054519),
         "Cu": Element("Copper", "Cu", 63.546),
         "Dy": Element("Dysprosium", "Dy", 162.5),
         "Er": Element("Erbium", "Er", 167.259),
         "Eu": Element("Europium", "Eu", 151.964),
         "F": Element("Fluorine", "F", 18.9984032),
         "Fe": Element("Iron", "Fe", 55.845),
         "Fr": Element("Francium", "Fr", 223),
         "Ga": Element("Gallium", "Ga", 69.723),
         "Gd": Element("Gadolinium", "Gd", 157.25),
         "Ge": Element("Germanium", "Ge", 72.64),
         "H": Element("Hydrogen", "H", 1.00794),
         "He": Element("Helium", "He", 4.002602),
         "Hf": Element("Hafnium", "Hf", 178.49),
         "Hg": Element("Mercury", "Hg", 200.59),
         "Ho": Element("Holmium", "Ho", 164.93032),
         "I": Element("Iodine", "I", 126.90447),
         "In": Element("Indium", "In", 114.818),
         "Ir": Element("Iridium", "Ir", 192.217),
         "K": Element("Potassium", "K", 39.0983),
         "Kr": Element("Krypton", "Kr", 83.798),
         "La": Element("Lanthanum", "La", 138.90547),
         "Li": Element("Lithium", "Li", 6.941),
         "Lu": Element("Lutetium", "Lu", 174.9668),
         "Mg": Element("Magnesium", "Mg", 24.305),
         "Mn": Element("Manganese", "Mn", 54.938045),
         "Mo": Element("Molybdenum", "Mo", 95.96),
         "N": Element("Nitrogen", "N", 14.0067),
         "Na": Element("Sodium", "Na", 22.98976928),
         "Nb": Element("Niobium", "Nb", 92.90638),
         "Nd": Element("Neodymium", "Nd", 144.242),
         "Ne": Element("Neon", "Ne", 20.1797),
         "Ni": Element("Nickel", "Ni", 58.6934),
         "Np": Element("Neptunium", "Np", 237),
         "O": Element("Oxygen", "O", 15.9994),
         "Os": Element("Osmium", "Os", 190.23),
         "P": Element("Phosphorus", "P", 30.973762),
         "Pa": Element("Protactinium", "Pa", 231.03588),
         "Pb": Element("Lead", "Pb", 207.2),
         "Pd": Element("Palladium", "Pd", 106.42),
         "Pm": Element("Promethium", "Pm", 145),
         "Po": Element("Polonium", "Po", 209),
         "Pr": Element("Praseodymium", "Pr", 140.90765),
         "Pt": Element("Platinum", "Pt", 195.084),
         "Pu": Element("Plutonium", "Pu", 244),
         "Ra": Element("Radium", "Ra", 226),
         "Rb": Element("Rubidium", "Rb", 85.4678),
         "Re": Element("Rhenium", "Re", 186.207),
         "Rh": Element("Rhodium", "Rh", 102.9055),
         "Rn": Element("Radon", "Rn", 222),
         "Ru": Element("Ruthenium", "Ru", 101.07),
         "S": Element("Sulfur", "S", 32.065),
         "Sb": Element("Antimony", "Sb", 121.76),
         "Sc": Element("Scandium", "Sc", 44.955912),
         "Se": Element("Selenium", "Se", 78.96),
         "Si": Element("Silicon", "Si", 28.0855),
         "Sm": Element("Samarium", "Sm", 150.36),
         "Sn": Element("Tin", "Sn", 118.71),
         "Sr": Element("Strontium", "Sr", 87.62),
         "Ta": Element("Tantalum", "Ta", 180.94788),
         "Tb": Element("Terbium", "Tb", 158.92535),
         "Tc": Element("Technetium", "Tc", 98),
         "Te": Element("Tellurium", "Te", 127.6),
         "Th": Element("Thorium", "Th", 232.03806),
         "Ti": Element("Titanium", "Ti", 47.867),
         "Tl": Element("Thallium", "Tl", 204.3833),
         "Tm": Element("Thulium", "Tm", 168.93421),
         "U": Element("Uranium", "U", 238.02891),
         "V": Element("Vanadium", "V", 50.9415),
         "W": Element("Tungsten", "W", 183.84),
         "Xe": Element("Xenon", "Xe", 131.293),
         "Y": Element("Yttrium", "Y", 88.90585),
         "Yb": Element("Ytterbium", "Yb", 173.054),
         "Zn": Element("Zinc", "Zn", 65.38),
         "Zr": Element("Zirconium", "Zr", 91.224)
    }
    return table

periodic_table = make_periodic_table()


def get_name(symbol):
    #Return the name of an element.
    return periodic_table[symbol].name

def get_atomic_mass(symbol):
    #Return the atomic mass of an element.
    return periodic_table[symbol].atomic_mass


class FormulaError(ValueError):
    #FormulaError is the type of error that parse_formula will raise if a formula is invalid.

    pass


def parse_formula(formula):
    #Convert a chemical formula for a molecule into a dictionary

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elems, symbol):
        return 0 if symbol not in elems else elems[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elems = {}  # A dictionary that holds symbol quantity pairs
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group, index = parse_r(formula, index + 1, level + 1)
                quant, index = parse_quant(formula, index)
                for symbol in group:
                    prev = get_quant(elems, symbol)
                    elems[symbol] = prev + group[symbol] * quant
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table:
                        index += 1
                    else:
                        # Unknown symbol for an element
                        raise FormulaError("invalid formula:", formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elems, symbol)
                elems[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    # Mismatched close parenthesis
                    raise FormulaError("invalid formula:", formula, index)
                level -= 1
                index += 1
                break
            else:
                # Illegal character: [^()0-9a-zA-Z] or decimal digit not preceded by an element symbol or close parenthesis
                raise FormulaError("invalid formula:", formula, index)
        if level > 0 and level >= start_level:
            # Mismatched open parenthesis
            raise FormulaError("invalid formula:", formula, start_index - 1)
        return elems, index

    elems, _ = parse_r(formula, 0, 0)
    return elems


def molar_mass(symbol_quantity_dict):
    #Compute and return the total molar mass of all the elements listed in symbol_quantity_dict.

    total_mass = 0

    for symbol, quantity in symbol_quantity_dict.items():
        atomic_mass = get_atomic_mass(symbol)
        total_mass += atomic_mass * quantity

    # Return the total mass.
    return total_mass

def mole_calc(grams, mol_mass):
    mol_total = grams / mol_mass
    return round(mol_total,5)



def main():
    true_mol = False
    while not true_mol:
        new_mol = input("Enter the chemical formula [eg. H2O]: ")
       

        try:
            new_parse = parse_formula(new_mol)

        except Exception as ex:
            print(f"{ex.args[1]} is invalid. Please input a valid molecule")
        else:
            true_mol = True
    
    new_mm = molar_mass(new_parse)
    print (f"The molar mass of the molecule {new_mol} is {round(new_mm,5)}.")
    true_grams = False
    while not true_grams:
        grams = input(f"Enter the mass of the chemical sample ({new_mol}) in grams: ")
        try:
            grams = float(grams)
        except Exception as ex:
            print("Please give a real value of grams.")
        else:
            true_grams = True

    moles = mole_calc(grams, new_mm)
    print(f"You have {round(moles,5)} moles of {new_mol}.")
    
main()