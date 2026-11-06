from pyscript import document, display

# Dictionary information about elements
# Element Name: Element Detail, Atomic Number, Atomic Mass
non_metals = {"H": ('Hydrogen', 1, 1.008),
        "He": ('Helium', 2, 4.0026),
        "Li": ('Lithium', 3, 6.94),
        "Be": ('Beryllium', 4, 9.012),
        "B": ('Boron', 5, 10.81),
        "C": ('Carbon', 6, 12.01),
        "N": ('Nitrogen', 7, 14.01),
        "O": ('Oxygen', 8, 16.00),
        "F": ('Fluorine', 9, 19.00),
        "Ne": ('Neon', 10, 20.18),
        "P": ('Phosphorus', 11, 30.97),
        "S": ('Sulfur', 12, 32.06),
        "Cl": ('Chlorine', 13, 35.45),
        "Ar": ('Argon', 14, 39.95),
        "Se": ('Selenium', 15, 78.96),
        "Br": ('Bromine', 16, 79.90),
        "Kr": ('Krypton', 17, 83.80),
        "I": ('Iodine', 18, 126.90),
        "Xe": ('Xenon', 18, 131.29),
        "At": ('Astatine', 19, 210),
        "Rn": ('Radon', 20, 222),
        "Ts": ('Tennessine', 21, 294),
        "Og": ('Oganesson', 22, 294)}

# function to search your element
def check_element(e):
    #Get the input from HTML

    Element1 = document.getElementById("element1").value.strip().capitalize()
    # retrieve information forom the dictionary
    result = non_metals.get(Element1, ('Element not found', "-", "-"))
    # Display the result in HTML
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("atomic_number").innerText = result[1]
    document.getElementById("atomic_mass").innerText = result[2]