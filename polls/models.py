from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    body = models.TextField(verbose_name='Вопрос')

    def __str__(self):
        return self.body


    # QUESTION_TYPES = (
    #     (1, 'Open-ended'),
    #     (2, 'Single choice'),
    #     (3, 'Multiple choice'),
    # )
    # type = models.IntegerField(verbose_name='Тип вопроса',choices=QUESTION_TYPES)

class Answer(models.Model):
    question = models.ForeignKey (Question, related_name='answers', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Ответ')
    user = models.ForeignKey(User, related_name='user_answers', on_delete=models.CASCADE) #todo fix it (make it so, if user deleted, his data stays)

    def __str__(self):
        return f"'{self.question}' answered '{self.body[:20]}' by {self.user}"







class Poll(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    started_at = models.DateTimeField(verbose_name='Начат',auto_now=False, auto_now_add=False,blank=True, null=True)
    questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.title



