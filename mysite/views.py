from django.http import HttpResponse,Http404
import datetime
from django.template import Context, Template
import datetime

def homepage(request):
    now = datetime.datetime.now()
    html = "<html><body>It is  now %s </body></html>" % now
    return HttpResponse(html)





