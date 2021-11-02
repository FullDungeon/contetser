from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# открытие главной страницы
def index(request):
    template = loader.get_template('index/index.html')
    context = {
        "site_name":      "Contester 0.1",
        "page_title":     "Главная",
    }

    return HttpResponse(template.render(context))

@csrf_exempt
def testcall(request):
   return HttpResponse(request.POST['text']) 