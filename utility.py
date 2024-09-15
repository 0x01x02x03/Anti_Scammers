import random, string


def fake_cc_gen():
    """Generates a fake credit card number between 4000000000000000 and 4999999999999999.

    This function uses Python's built-in random module to generate a random integer within the specified range.

    Returns:
        int: A fake credit card number.
    """
    return random.randint(4000000000000000, 4999999999999999)


def random_user_agents():
    """Generates a random user agent from a list of predefined user agents.

    The function reads the user agents from a file named "user-agents.txt" and selects one at random.

    Returns:
        str: A randomly selected user agent.
    """
    with open("user-agents.txt") as f:
        usuarios = f.read().splitlines()
    return random.choice(usuarios)


def random_trash_passes():
    """Generates a random trash pass number between 100 and 999.

    This function uses two nested calls to `random.randint` to generate a random integer within the specified range.

    Returns:
        int: A randomly generated trash pass number.
    """
    return random.randint(100, 999)


def longitud_random():
    """Generates a random length between 1 and 32 for strings.

    This function uses Python's built-in `random` module to generate a random integer within the range of 1 to 32.

    Returns:
        int: A randomly generated length for strings.
    """
    return random.randint(1, 32)


def random_four_chars():
    """Generates a random string of four characters.

    This function generates a random string consisting of four alphanumeric characters. The length of the string is randomly chosen between 1 and 32, and the characters are drawn from all uppercase letters, lowercase letters, and digits.

    Returns:
        str: A randomly generated string of four characters.
    """
    chars = string.ascii_letters + string.digits
    length = random.randint(1, 32)
    return "".join(random.choice(chars) for _ in range(length))


def random_characters():
    """Generates a random string of characters with a randomly chosen length between 1 and 32.

    The function uses `random.SystemRandom()` to ensure randomness across different platforms and `string.ascii_uppercase` and `string.digits` for character selection.

    Returns:
        str: A randomly generated string of characters with the specified length.
    """
    chars = string.ascii_uppercase + string.digits
    length = random.randint(1, 32)
    return "".join(random.SystemRandom().choice(chars) for _ in range(length))


def random_email():
    """Generates a random email address with the format of a string of random characters followed by "@live.com".

    The length of the random character string is randomly chosen between 1 and 32.
    Returns:
        str: A randomly generated email address in the form "randomchars@live.com".
    """
    return (
        "".join(random.choice(string.ascii_letters) for _ in range(longitud_random()))
        + "@live.com"
    )


def extract_domain(url):
    """Extracts the domain from a given URL string.

    This function removes the protocol (http or https) and the path length, leaving only the domain name.

    Args:
        url (str): The input URL string.

    Returns:
        str: The extracted domain name from the URL.
    """
    mod_string = url[: len(url) - 13]
    return mod_string[7:]


def target_headers(usuario, dominio):
    """Generates a dictionary of HTTP headers for targeting requests.

    This function constructs and returns a dictionary of HTTP headers suitable for web scraping or automated browsing tasks. It includes the Host header, User-Agent, Accept headers, Accept-Language, Accept-Encoding, Content-Type, Origin, DNT, Connection, Referer, and Upgrade-Insecure-Requests headers.

    Args:
        usuario (str): The user agent string representing the browser or scraping tool.
        dominio (str): The domain name of the target website.

    Returns:
        dict: A dictionary containing HTTP headers.
    """
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
    """Generates a dictionary of HTTP headers for targeting secondary requests.

    This function constructs and returns a dictionary of HTTP headers suitable for web scraping or automated browsing tasks, particularly when the request is not directly to the main domain but to a specific sub-page. It includes the Host header, User-Agent, Accept headers, Accept-Language, Accept-Encoding, Content-Type, Origin, DNT, Connection, Referer, and Upgrade-Insecure-Requests headers.

    Args:
        usuario (str): The user agent string representing the browser or scraping tool.
        dominio (str): The domain name of the target website.

    Returns:
        dict: A dictionary containing HTTP headers for secondary requests.
    """
    headers_2 = {
        "Host": dominio,  # "ffffggggggggg000.hostfree.pw",
        "User-Agent": usuario,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://" + dominio,  # "http://ffffggggggggg000.hostfree.pw"
        "DNT": "1",
        "Connection": "close",
        "Referer": "http://"
        + dominio
        + "/Crear-Pin.html",  # "http://ffffggggggggg000.hostfree.pw/Crear-Pin.html"
        "Upgrade-Insecure-Requests": "1",
    }
    return headers_2
