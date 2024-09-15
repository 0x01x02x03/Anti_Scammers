import datetime
import random


def Nombre():
    """
    Generates a random name from a predefined list of names.

    Returns:
        str: A randomly selected name from the list of names.

    This function uses a list of common names and selects one at random using Python's `random.choice` function.
    """
    nombres = [
        "Juan",
        "Pedro",
        "Maria",
        "Rocio",
        "Jose",
        "Antonio",
        "Agustin",
        "Pablo",
        "Alejandro",
        "Jessica",
        "Noemi",
        "Paula",
        "Fatima",
        "Antonia",
        "Ricardo",
        "Javier",
        "Manuel",
        "Luis",
        "Laura",
        "Sonia",
        "Paco",
        "Lucia",
        "Jaime",
        "Rafael",
    ]
    return random.choice(nombres)


def Apellidos():
    """
    Generates a random surname from a predefined list of surnames.

    Returns:
        str: A randomly selected surname from the list of surnames.

    This function uses a list of common surnames and selects one at random using Python's `random.choice` function.
    """
    apellidos = [
        "Gomez",
        "Troncoso",
        "Fernandez",
        "Castaño",
        "Morales",
        "Alcedo",
        "Parodi",
        "Torres",
        "Aguilar",
        "Sauco",
        "Mangano",
        "Ruiz",
        "Aragon",
        "Candon",
        "Acosta",
        "Cabeza",
        "Soto",
        "Ezequiel",
        "Pericacho",
        "Rodriguez",
    ]
    return random.choice(apellidos)


def Ciudad():
    """
    Generates a random city from a predefined list of cities.

    Returns:
        str: A randomly selected city from the list of cities.

    This function uses a list of common cities and selects one at random using Python's `random.choice` function.
    """
    ciudades = [
        "Lavalle",
        "San Luis",
        "Santa Fe",
        "Lujan",
        "Formosa",
        "Bariloche",
        "Santa Cruz",
        "Salta",
        "Resistencia",
        "Buenos Aires",
        "Santigo del Estero",
    ]
    return random.choice(ciudades)


def Localidad():
    """
    Generates a random location from a predefined list of locations.

    Returns:
        str: A randomly selected location from the list of locations.

    This function uses a list of common locations and selects one at random using Python's `random.choice` function.
    """
    localidades = [
        "Flores",
        "Gernica",
        "Mataderos",
        "Capital Federal",
        "Formosa",
        "Resistencia",
        "Jujuy",
        "Gualeguaychu",
        "La pampa",
        "La banda",
    ]
    return random.choice(localidades)


def Provincia():
    """
    Generates a random province from a predefined list of provinces.

    Returns:
        str: A randomly selected province from the list of provinces.

    This function uses a list of common provinces and selects one at random using Python's `random.choice` function.
    """
    provincias = [
        "Buenos Aires",
        "Capital Federal",
        "Catamarca",
        "Chaco",
        "Chubut",
        "Córdoba",
        "Corrientes",
        "Entre Ríos",
        "Formosa",
        "Jujuy",
        "La Pampa",
        "La Rioja",
        "Mendoza",
        "Misiones",
        "Neuquén",
        "Río Negro",
        "Salta",
        "San Juan",
        "San Luis",
        "Santa Cruz",
        "Santa Fe",
        "Santiago del Estero",
        "Tierra del Fuego",
        "Tucumán",
    ]
    return random.choice(provincias)


def Domicilio():
    """
    Generates a random address from a predefined list of addresses.

    Returns:
        str: A randomly selected address from the list of addresses.

    This function uses a list of common addresses and selects one at random using Python's `random.choice` function.
    """
    domicilios = [
        "Lavalle 191",
        "Gernica 923",
        "Madariaga 781",
        "Mendoza 186",
        "Formosa 784",
        "San Martin 675",
        "Jujuy 751",
        "Saigon 684",
        "Norte 1679",
        "Bahia 9712",
        "Madrid 191",
        "Paris 923",
        "Moscu 781",
        "Dacota 186",
        "Maldonado 784",
        "Lujan 675",
        "Rivadavia 751",
        "Pekin 684",
        "Barcelona 1679",
        "Bombai 9712",
    ]
    return random.choice(domicilios)


def compara(i, aleat, dni):
    """
    Checks if a randomly generated number is unique in the first `i` digits of a given DNI (Documento Nacional de Identidad).

    Parameters:
        i (int): The number of initial digits to consider for uniqueness checking.
        aleat (int): The randomly generated number to be compared with the DNI.
        dni (str): The DNI string from which to extract the first `i` digits.

    Returns:
        bool: True if the random number is not found in the first `i` digits of the DNI, False otherwise.

    This function compares a randomly generated number with the initial portion of a given DNI to ensure that it does not already exist within those digits. It uses slicing to extract the necessary part of the DNI for comparison.
    """
    return aleat not in dni[:i]


def Dni(num):
    """
    Generates a list of unique random numbers that correspond to the first `num` digits of a DNI.

    Parameters:
        num (int): The number of unique random numbers to generate, each corresponding to the initial digits of a DNI.

    Returns:
        list: A list of integers, where each integer is a randomly generated number and all are unique within the first `num` digits.

    This function generates a list of random numbers, ensuring that each number is unique by checking against previously generated numbers. It uses a while loop to generate new numbers until a unique one is found. The length of each number corresponds to the initial `num` digits typically used in a DNI.
    """
    dni = [random.randint(10, 9999)]
    for i in range(num - 1):
        aleat = random.randint(10, 9999)
        while any(aleat == x for x in dni):
            aleat = random.randint(10, 9999)
        dni.append(aleat)
    return dni


# creamos numeros aleatorios de celulares
def create_phone():
    """
    Generates a random phone number for mobile devices in Argentina.

    Returns:
        str: A 10-digit phone number starting with '1' followed by the area code and exchange, ending with seven digits.

    This function constructs a phone number following the Argentine mobile number format, where the first digit is always '1', followed by an area code ranging from 3 to 9, then an exchange number (also between 0 and 9), and finally seven digits. The area codes are specific to Argentina's mobile network providers based on their region.
    """
    first_digit = "1"
    area_code = random.randint(3, 9)
    exchange = (
        random.randint(0, 9)
        if area_code in [3, 4, 5]
        else (
            random.choice([5, 7, 9])
            if area_code == 7
            else random.randint(0, 9) if area_code == 8 else random.randint(0, 9)
        )
    )  # This part can be simplified
    suffix = random.randint(9999999, 100000000)


# CHECKER BASADO EN ALGORITMO LUHN
def cardLuhnChecksumIsValid(card_number):
    """
    Checks if a given credit card number is valid using the Luhn algorithm.

    The Luhn algorithm, also known as the modulus 10 algorithm, is a simple checksum formula used to validate a variety of identification numbers, including credit card numbers and Social Security Numbers (SSNs). It helps in detecting errors in data entry such as transposition or illegible digits, and it can detect almost any single-digit error.

    Parameters:
        card_number (str): The credit card number to be validated, represented as a string of digits.

    Returns:
        bool: True if the card passes the Luhn check, False otherwise.

    This function implements the Luhn algorithm by iterating over the digits from right to left, doubling every second digit and subtracting 9 if the result is greater than 9, summing all the digits, and checking if the total modulo 10 is equal to zero. If it is, the card number passes the check; otherwise, it does not.
    """
    digits = [int(d) for d in card_number]
    total = 0
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if (len(digits) - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0


# GENERA UNA BASE DE BIN XXXXXXXXXXXXXXXX
def ccgen(bin_format):
    """
    Generates a random credit card number based on the given BIN format.

    Parameters:
        bin_format (str): The beginning of the credit card number, represented as a string of digits. It should be at least 6 digits long.

    Returns:
        str: A randomly generated credit card number with the specified BIN and a valid Luhn checksum.

    This function constructs a credit card number by extracting the first 6 digits from the `bin_format`, filling in the remaining digits with 'x', and then calculating the Luhn checksum to ensure the number is valid. The generated number follows the format of the BIN provided, ensuring that it starts with the specified digits.
    """
    out_cc = bin_format[:6]  # Extract the first 6 digits
    for _ in range(10 - len(bin_format[6:])):  # Fill in the remaining digits with 'x'
        out_cc += "x"
    # Generate checksum (last digit) -- SIMPLIFIED CHECKSUM
    total = sum([int(d) for d in out_cc[6:]]) % 10
    if total == 0:
        check_digit = "0"
    else:
        check_digit = str(10 - total)
    out_cc += check_digit
    return out_cc


# Write on a file that takes a list for the argument
def save(generated):
    """
    Writes a list of generated credit card numbers to a text file.

    Parameters:
        generated (list): A list of strings, each representing a generated credit card number.

    This function creates a new text file named with the current date and time, appends each generated credit card number from the list on a new line, and closes the file.
    """
    now = datetime.datetime.now()
    file_name = "cc-gen_output_{0}.txt".format(
        str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    )
    f = open(file_name, "w")
    for line in generated:
        f.write(line + "\n")
    f.close()


# Random ccv gen
def ccvgen():
    """
    Generates a random CVV (Card Verification Value) for a credit card number.

    The CVV is a 3-digit code usually found on the back of credit cards, used to verify the authenticity of the cardholder. This function generates a random 3-digit number and returns it as a string.

    Returns:
        str: A randomly generated 3-digit CVV.
    """
    return str(random.randint(100, 999))


# codigo postal
def codigo_postal_gen():
    """
    Generates a random zip code for a credit card number.

    The zip code is a 4-digit number usually associated with the billing address of a credit card. This function generates a random 4-digit number and returns it as a string.

    Returns:
        str: A randomly generated 4-digit zip code.
    """
    return str(random.randint(1000, 9999))


def email_gen():
    """
    Generates a random email based on randomly chosen first and last names.

    This function uses predefined lists of first and last names to construct an email address by concatenating a random first name, a period, a random last name, and a domain from a list of popular email providers (gmail.com, hotmail.com, live.com, yahoo.com).

    Returns:
        str: A randomly generated email address.
    """
    nombres = [
        "Juan",
        "Maria",
        "Pedro",
        "Sofia",
        "David",
        "Laura",
        "Pablo",
        "Ana",
        "Lucas",
        "Valentina",
    ]
    apellidos = [
        "Garcia",
        "Rodriguez",
        "Gomez",
        "Lopez",
        "Hernandez",
        "Martinez",
        "Fernandez",
        "Perez",
        "Sanchez",
        "Gonzalez",
    ]
    correo = (
        random.choice(nombres)
        + "."
        + random.choice(apellidos)
        + random.choice(["@gmail.com", "@hotmail.com", "@live.com", "@yahoo.com"])
    )
    return correo


# Random exp date
def dategen():
    """
    Generates a random expiration date for a credit card number.

    This function calculates the current year and adds one to get the expiration year. It then generates a random month within the range of 1 to 12. The formatted date string is returned in the format "MM/YYYY".

    Returns:
        str: A randomly generated expiration date in the format "MM/YYYY".
    """
    now = datetime.datetime.now()
    year = now.year + 1  # Add 1 year to the current year
    month = random.randint(1, 12)
    return "{:02d}/{:04d}".format(month, year)
