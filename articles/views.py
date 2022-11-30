from django.views.generic import ListView, DeleteView       #
from .models import Article



class ArticleListView(ListView):     #내장템플릿쓸때는 편수 적용
    model = Article                     #생성수정 등이 화면에 나와야하는 동적이기때문에
    template_name = "article_list.html"


class AticleDetailVeiw(DeleteView):
    model = Article
    template_name = "article_detail.html"

    

#생성 수정 삭제 조회 등을 만들어야함 CRUD 크루드 어플리케이션