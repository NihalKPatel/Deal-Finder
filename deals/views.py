from django.http import HttpResponse


#HomePage
def index(request):
    return HttpResponse('Homepage')
