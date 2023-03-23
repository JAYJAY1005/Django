from django.db import models
from django.contrib.auth.models import User
from webapp import settings

# 질문란
class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
    # 작성한 질문이 제목으로 보여지게 함
    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'question'

# 댓글란
class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.question

    class Meta:
        db_table = 'answer'