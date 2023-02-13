from django.db import models

# Create your models here.
# Post라는 class를 만들고, 속성으로 제목, 내용, 작성일, 수정일
# Object Related Mapping (ORM) - 대부분의 웹 프레임워크가 제공하는 기능 
# 모델에 class 형태로 데이터의 구조를 집어넣으면 
# 중간에서 table 형태(SQL 쿼리로 변환해서)로 저장해주는 것
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 처음 만들어진 시간
    crated_at = models.DateTimeField(auto_now_add=True) # , auto_now_add=False,
    # update가 된 시간으로 계속 갱신됨
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f'[{self.pk}] {self.title}'

