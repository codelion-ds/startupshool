from django.urls import path
from .views import HomePageView, LocationPageView, TermsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("location/", LocationPageView.as_view(), name="location"),
    path("terms/", TermsPageView.as_view(), name="terms")
]
