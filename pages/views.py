# from django.http import HttpResponse
from django.views.generic import TemplateView

# def homePageView(request):
#     return HttpResponse("안녕하세요 :)")

class HomePageView(TemplateView):
    template_name = "home.html"

class LocationPageView(TemplateView):       #페이지별 클래스를 새로 만들어야함
    template_name = "location.html"

class TermsPageView(TemplateView):
    template_name = "terms.html"