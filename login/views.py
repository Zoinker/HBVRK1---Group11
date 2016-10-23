from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Þetta er login síðan. Hér velurðu hvort þú vilt leita að ferð eða bjóða upp á ferð</h1>")