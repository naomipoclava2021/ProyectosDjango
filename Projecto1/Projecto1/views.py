from django.http import HttpResponse
import datetime


def saludo (request):#primera vista
    parafo = """<html>
    <body>
    <p>Esto es un parafo</p>
    <p> Soy naomi milagro poclava esta es mi pagina web </p>
    </body>
    </html>"""

    titulo = '<html><body><h1>Pagina hecha en Diango</h1></body></html>'
    return HttpResponse(parafo)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de django, chau amigos")


def fecha(request):
    fecha_actual = datetime.datetime.now()
    titulo = """
    <html>
    <body>
        <h2> 
            Fecha y hora actuales %s
        </h2>
    </body>
    </html>"""% fecha_actual
    return HttpResponse(titulo)

def calculaEdad(request, edad,agno):
    #edadActual =18
    periodo= agno -2019
    edadFutura = edad +periodo
    documento = "<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)

    
