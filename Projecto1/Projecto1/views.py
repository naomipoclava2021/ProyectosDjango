
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo (request):#primera vista

    p1 = Persona("Juan", "Diaz")
    #nombre ="Juan"
    #apellido = "Serrano"
    fecha_actual = datetime.datetime.now()



    doc_externo = open("C:/Users/milag/OneDrive/Escritorio/ProyectosDjango/Projecto1/Projecto1/Plantillas/miPlantilla.html")

    
    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha": fecha_actual})

    documento = plt.render(ctx)

    return HttpResponse(documento)

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

    
