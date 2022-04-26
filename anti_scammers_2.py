import requests as req
from utility import *
from utility_card_gen import *
from headers_utility import *

# Definiciones para el trolleo
ccs_regaladas = 0
celulares = 0
parientes = 0

# Datos a usar contra nuestros amiguitos
nombre = Nombre()
apellido = Apellidos()
dni = create_phone()
celular = create_phone()
email = email_gen()
domicilio = Domicilio()
codigo_postal = codigo_postal_gen()
provincia = Provincia()
localidad = Localidad()
ciudad = Ciudad()
# print(dategen())
tarjeta = ccgen("559975xxxxxxxxxx")
# print(tarjeta)
mes = str(randint(10, 12))
# print(mes)
now = datetime.datetime.now()
ano = str(now.year + randint(1, 12))
# print(ano)
cvv_ = ccvgen()

url_1 = "http://104.168.52.143/Finance/bmo-mobile/myonportal.php"  # primer post
url_2 = "http://104.168.52.143/Finance/bmo-mobile/move.php"  # segundo post
url_2_2 = "http://104.168.52.143/Finance/bmo-mobile/information.html"
url_3 = "http://104.168.52.143/Finance/bmo-mobile/processing.php"  # tercer post
url_3_2 = "http://104.168.52.143/Finance/bmo-mobile/finish.html"
url_3_3 = "http://104.168.52.143/onlinebanking/includes/pm_fp.html"

dominio = "104.168.52.143"


usuario = random_user_agents()


headers = target_headers(usuario, dominio)

# headers_2 = target_headers_secondary(usuario, dominio)
cc = fake_cc_gen()
str_1 = (
    "siBankCard=" + str(tarjeta) + "&asd=&regSignInPassword=" + str(random_characters())
)

str_2 = (
    str_1
    + "&q1=What+is+the+first+name+of+your+father%27s+oldest+sibling%3F&a1="
    + nombre
    + "&q2=What+is+the+first+name+of+your+oldest+niece%3F&a2="
    + apellido
    + "&q3=What+is+the+first+name+of+your+oldest+nephew%3F&a3="
    + ciudad
    + "&x=42&y=7"
)

str_3 = "DN=" + domicilio + "&AP=" + str(random_four_chars()) + "&CVV=" + str(ccvgen())


def troll_spammers():
    pasadas_totales = random_trash_passes()
    for i in range(pasadas_totales):
        if i == 0:
            print("Vamos a hacer un total de " + str(pasadas_totales) + " pasadas")

        req.post(
            url_1,
            headers=headers_1,
            data=str_1 + str("&x=47&y=9"),
            verify=False,
        )
        req.post(
            url_2,
            headers=headers_2,
            data=str_2,
            verify=False,
        )
        req.post(
            url_3,
            headers=headers_3,
            data=str_3,
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
