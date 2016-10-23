from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Þetta er síðan fyrir ökuþóra, hér læturðu vita ef þú ert að bjóða upp á far.</h1>")
