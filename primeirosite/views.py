from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse('Olá, mundo!')

def qual_dia(request):
    dia_formatado = datetime.datetime.now().strftime('%d/%m/%Y')
    html = "<html><body>Hoje é dia %s.</body></html>" % dia_formatado
    return HttpResponse(html)