from django.urls import path
from .views import ArticleListView, AticleDetailVeiw



urlpatterns = [
    
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("articles/<int:pk>", AticleDetailVeiw.as_view(), name="articles_detail")
]
