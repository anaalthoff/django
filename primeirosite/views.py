from django.http import HttpResponse
import datetime
import locale

def index(request):
    return HttpResponse('Olá, mundo!')

def qual_dia(request):
    dia_formatado = datetime.datetime.now().strftime('%d/%m/%Y')
    html = "<html><body>Hoje é dia %s.</body></html>" % dia_formatado
    return HttpResponse(html)

def qual_dia_sera(request, dias):
    novo_dia = datetime.datetime.now() + datetime.timedelta(days = dias)
    dia_formatado = novo_dia.strftime('%d/%m/%Y')
    html = "<html><body>Em %s dias será dia %s.</body></html>" % (dias, dia_formatado)
    return HttpResponse(html)

# 1. Crie uma nova view, semelhante à view "qual_dia" mas que retorne o dia da semana e o formato da data por extenso, por exemplo: "Hoje é dia 28 de março de 2025, uma sexta-feira."
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def dia_da_semana(request):
    agora = datetime.datetime.now()
    data_formatada = agora.strftime('%d de %B de %Y')
    dia_semana = agora.strftime('%A')

    html = f"<html><body>Hoje é dia {data_formatada}, {dia_semana}.</body></html>"
    return HttpResponse(html)

# 2. Faça uma cópia desta view e adapte, para que informe que dia da semana foi x anos atrás
def dia_anos_passados(request, anos):
    agora = datetime.datetime.now()
    anos = int(anos)

    data_passada = agora.replace(year=agora.year - anos)

    data_formatada = data_passada.strftime('%d de %B de %Y')
    dia_semana = data_passada.strftime('%A')

    html = f"<html><body>Há {anos} anos, era dia {data_formatada}, {dia_semana}.</body></html>"
    return HttpResponse(html)

