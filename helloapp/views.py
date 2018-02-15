from django.shortcuts import render
from django.views import View

class Index(View):
    template_name = 'pages/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class VisitTestPage(View):
    template_name = 'pages/visit.html'

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass