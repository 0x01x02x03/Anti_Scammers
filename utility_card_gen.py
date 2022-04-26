#!/usr/bin/env python

import datetime
from random import randint
import random
from random import randrange


# nombres
def Nombre():

    VNom = [
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

    return VNom[randrange(0, len(VNom))]


def Apellidos():

    VApell = [
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

    return VApell[randrange(0, len(VApell))]


def Ciudad():

    VCiudad = [
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
    return VCiudad[randrange(0, len(VCiudad))]


def Localidad():

    VLocalidad = [
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

    return VLocalidad[randrange(0, len(VLocalidad))]


def Provincia():

    VProvincia = [
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

    return VProvincia[randrange(0, len(VProvincia))]


def Domicilio():

    VDomicilio = [
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

    return VDomicilio[randrange(0, len(VDomicilio))]


def compara(i, aleat, dni):

    for j in range(i):

        if aleat != dni[j]:

            return True

        elif aleat == dni[j]:

            return False


def Dni(num):

    dni = []

    dni.append(randrange(10, 10001))

    for i in range(num):

        aleat = randrange(10, 10001)

        a = compara(i, aleat, dni)

        if a == True:

            dni.append(aleat)

        elif a == False:

            i = i - 1

    return dni


# creamos numeros aleatorios de celulares
def create_phone():
    # Segundo dígito
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # Tercer dígito
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # Últimos ocho dígitos
    suffix = random.randint(9999999, 100000000)
    # Fusionar número de teléfono
    return "1{}{}{}".format(second, third, suffix)
    # Generar número de teléfono móvil


# print(celular)


# CHECKER BASADO EN ALGORITMO LUHN
def cardLuhnChecksumIsValid(card_number):
    """checks to make sure that the card passes a luhn mod-10 checksum"""

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not ((count & 1) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return (sum % 10) == 0


# GENERA UNA BASE DE BIN XXXXXXXXXXXXXXXX


def ccgen(bin_format):
    out_cc = ""
    if len(bin_format) == 16:
        # Iteration over the bin
        for i in range(15):
            if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                out_cc = out_cc + bin_format[i]
                continue
            if bin_format[i] in ("x"):
                out_cc = out_cc + str(randint(0, 9))

        # Generate checksum (last digit) -- IMPLICIT CHECK
        for i in range(10):
            checksum_check = out_cc
            checksum_check = checksum_check + str(i)

            if cardLuhnChecksumIsValid(checksum_check):
                out_cc = checksum_check
                break
            else:
                checksum_check = out_cc

    return out_cc


# Write on a file that takes a list for the argument
def save(generated):
    now = datetime.datetime.now()
    file_name = "cc-gen_output_{0}.txt".format(
        str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    )
    f = open(file_name, "w")
    for line in generated:
        f.write(line + "\n")
    f.close


# Random ccv gen
def ccvgen():
    ccv = ""
    num = randint(10, 999)

    if num < 100:
        ccv = "0" + str(num)
    else:
        ccv = str(num)

    return ccv


# codigo postal
def codigo_postal_gen():
    postal = ""
    num = randint(1000, 9999)

    if num < 1000:
        postal = "0" + str(num)
    else:
        postal = str(num)

    return postal


def email_gen():
    random.seed()
    correoz = ["@gmail.com", "@hotmail.com", "@live.com", "@yahoo.com"]
    email = Nombre() + Apellidos() + random.choice(correoz)
    return email


# Random exp date
def dategen():
    now = datetime.datetime.now()
    date = ""
    month = str(randint(1, 12))
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
    date = month + "|" + year

    return date
