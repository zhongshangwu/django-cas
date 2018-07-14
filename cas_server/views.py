from django.http.response import HttpResponse
from django.views import View
# Create your views here.


class DemoView(View):
    """Demo view"""

    def get(self, request):
        return HttpResponse("ok")
