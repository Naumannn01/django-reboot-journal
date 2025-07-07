from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    subject=models.CharField(max_length=100,blank=True,null=True)
    content=models.TextField()
    reviewed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
