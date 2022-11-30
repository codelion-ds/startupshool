from django.db import models  #내장되어 있는 모델
from django.urls import reverse

class Article(models.Model):
    #글의 제목 내용 첨부파일등 많은 내용
    title = models.CharField(max_length=255)        #반듯이 들어가야하는 옵션 길이값제한
    content = models.TextField()                    #캐릭터보다 긴 원문이나 글 내용에 적합
    author = models.ForeignKey(                     #만들어진 회원 데이터 가져오기, 포링키 외부 키 가져오기.
        "auth.User",
        on_delete=models.CASCADE                    #유저를 지우면 그 관련 글들을 전부 삭제, 반대는 PROTECT
    )
    def __str__(self):                              #인스턴트에서 출력시 자기 자신의 제목 출력
        #return self.title
        return f"{self.title}  - {self.author}"     #작성자 + 글 파이썬 함수 참조하기                  

    def get_absolute_url(self):                     #자기 자신의 주소를 반환하게 하는 함수
        return reverse("article_detail", kwargs={"pk": self.pk})  #pk=프라이머리키 고유번호 누구나 있어야하는 , 알아서 생김
    



# 데이터를 생성 수정 변경 하는 파일
# Create your models here.
