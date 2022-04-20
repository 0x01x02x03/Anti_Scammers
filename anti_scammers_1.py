import random, string, requests as req

url = "http://ffffggggggggg000.hostfree.pw/conexion.php"


def random_user_agents():
    lines = open("user-agents.txt").read().splitlines()
    myline = random.choice(lines)
    return myline


def random_email():
    return (
        "".join(random.choice(string.ascii_letters) for _ in range(longitud_random()))
        + "@live.com"
    )


def random_trash_passes():
    numero_aleatorio = random.randint(random.randint(1, 499), random.randint(500, 999))
    return numero_aleatorio


def longitud_random():
    long_random = random.randint(1, 32)
    return long_random


def random_four_chars():
    long_random = random.randint(1000, 9999)
    return long_random


def random_characters():
    return "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(longitud_random())
    )


usuario = random_user_agents()


def headers_primary(usuario):
    headers = {
        "Host": "ffffggggggggg000.hostfree.pw",
        "User-Agent": usuario,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://ffffggggggggg000.hostfree.pw",
        "DNT": "1",
        "Connection": "close",
        "Referer": "http://ffffggggggggg000.hostfree.pw/",
        "Upgrade-Insecure-Requests": "1",
    }

    return headers


headers = headers_primary(usuario)


def headers_secondary(usuario):
    headers_2 = {
        "Host": "ffffggggggggg000.hostfree.pw",
        "User-Agent": usuario,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://ffffggggggggg000.hostfree.pw",
        "DNT": "1",
        "Connection": "close",
        "Referer": "http://ffffggggggggg000.hostfree.pw/Crear-Pin.html",
        "Upgrade-Insecure-Requests": "1",
    }

    return headers_2


headers_2 = headers_secondary(usuario)


def troll_spammers():
    pasadas_totales = random_trash_passes()
    for i in range(pasadas_totales):
        if i == 0:
            print("Vamos a hacer un total de " + str(pasadas_totales) + " pasadas")

        req.post(
            url,
            headers=headers,
            data="uno=" + str(random_email()) + "&dos=" + str(random_characters()),
            verify=False,
        )
        req.post(
            "http://ffffggggggggg000.hostfree.pw/conexion.php",
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

troll_spammers()
