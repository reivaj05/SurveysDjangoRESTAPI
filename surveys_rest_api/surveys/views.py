from django.http import HttpResponse

# Create your views here.


def index(request):
    html = "<html><body>testing</body></html>"
    return HttpResponse(html)
