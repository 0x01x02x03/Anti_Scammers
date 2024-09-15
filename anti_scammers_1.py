import requests as req
from utility import *

url = "http://ffffggggggggg000.hostfree.pw/conexion.php"
dominio = "ffffggggggggg000.hostfree.pw"


def troll_spammers(url, dominio):
    usuario = random_user_agents()
    headers = target_headers(usuario, dominio)
    headers_2 = target_headers_secondary(usuario, dominio)
    longitud = longitud_random()

    pasadas_totales = random_trash_passes()
    for i in range(pasadas_totales):
        if i == 0:
            print("Vamos a hacer un total de " + str(pasadas_totales) + " pasadas")

        req.post(
            url,
            headers=headers,
            data="uno="
            + str(random_email(longitud))
            + "&dos="
            + str(random_characters(longitud)),
            verify=False,
        )
        req.post(
            dominio + "/conexion.php",
            headers=headers_2,
            data="tres="
            + str(random_four_chars())
            + "&cuatro="
            + str(random_four_chars()),
            verify=False,
        )
        print("[+] Enviando pasada n°: " + str(i + 1))
        if i == pasadas_totales:
            print("[+] Enviadas todas las pasadas")

    print(
        """Este script está hecho para hacer spam a un scam que trata de robar cuentas simulando ser sitio legal de microsoft.
    Mediante este script se genera datos aleatorios en cada ejecucion, tanto numerico como alfanumerico.
    Pero no solamente esto, sino tambien la duracion de cada tanda de datos, sumado a que el User-Agent de cada POST es aleatorio.
    Disfruta el trafico de datos extra amigo, estoy seguro que tu base de datos solo tendra datos 100% reales, no fake.\n\n"""
    )
    input("[+] Presiona cualquier tecla para iniciar el envio de saludos...")


troll_spammers(url, dominio)
