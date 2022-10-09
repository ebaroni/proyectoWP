from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
#html_base= """
#    <h1>Mi Web Personal</h1>
#    <ul>
#        <li><a href="/home/">Portada</a></li>
#        <li><a href="/about/">Acerca de mi</a></li>
#        <li><a href="/portfolio/">Portfolio</a></li>
#        <li><a href="/contacto/">Contacto</a></li>
#    </ul>
#"""

def home(request):
    return render(request, "core/home.html")
    #return HttpResponse(html_base +
    #    """<h2>Portada</h2>
    #      <p>Esta es la portada</p>""")

def about(request):
    return render(request, "core/about.html")
#    return HttpResponse(html_base +  
#        """<h2>Acerca de mi</h2>
#            <p>Soy Esteban</p> """)


def portfolio(request):
    return render(request, "core/portfolio.html")
#    return HttpResponse(html_base + 
#        """<h2>Este es mi Portfolio</h2>
#            <p>Proyectos""")

def contact(request):
    return render(request, "core/contact.html")
#    return HttpResponse(html_base + 
#       """<h2>Estos son mis datos de contacto</h2>
#            <p>Mail</p>
#            <p>Nombre y Apellido</p>""")

