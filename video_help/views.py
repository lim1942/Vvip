from django.http import HttpResponseNotFound, HttpResponse

def index(request):
    resp = HttpResponse()
    resp.write('23322weewew')
    return resp
