from django.db import models


class solution(models.Model):
    question = models.TextField(max_length=200)
    solution = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
