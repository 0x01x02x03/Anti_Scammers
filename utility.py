import random, string


def fake_cc_gen():
    return random.randint(4000000000000000, 4999999999999999)


def random_user_agents():
    usuarios = open("user-agents.txt").read().splitlines()
    miUsuario = random.choice(usuarios)
    return miUsuario


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


def random_email():
    return (
        "".join(random.choice(string.ascii_letters) for _ in range(longitud_random()))
        + "@live.com"
    )


def extract_domian(url):
    mod_string = url[: len(url) - 13]
    return mod_string[7:]


def target_headers(usuario, dominio):
    headers = {
        "Host": dominio,  # "ffffggggggggg000.hostfree.pw",
        "User-Agent": usuario,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://" + dominio,  # "http://ffffggggggggg000.hostfree.pw"
        "DNT": "1",
        "Connection": "close",
        "Referer": "http://" + dominio + "/",  # "http://ffffggggggggg000.hostfree.pw/"
        "Upgrade-Insecure-Requests": "1",
    }
    return headers


def target_headers_secondary(usuario, dominio):
    headers_2 = {
        "Host": dominio,  # "ffffggggggggg000.hostfree.pw",
        "User-Agent": usuario,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://" + dominio,  # "http://ffffggggggggg000.hostfree.pw",
        "DNT": "1",
        "Connection": "close",
        "Referer": "http://"
        + dominio
        + "/Crear-Pin.html",  #  "http://ffffggggggggg000.hostfree.pw/Crear-Pin.html",
        "Upgrade-Insecure-Requests": "1",
    }
    return headers_2
