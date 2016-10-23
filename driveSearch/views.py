from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Þetta er leitarsíðan. Hér leitarðu að ferðum.</h1>")