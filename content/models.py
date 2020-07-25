from django.db import models
from yesshow import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    STATUS = (
        ("W", "양도 대기"),
        ("C", "양도 완료"),
        ("P", "양도 진행중"),
    )
    status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)

    date = models.DateTimeField(auto_now=True)
    reserve_price = models.IntegerField()
    food_price = models.IntegerField()
    people = models.IntegerField()
    text = models.TextField()
    img = models.ImageField(upload_to='content/', blank=True, null=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    phone_number = models.CharField(max_length=100)
    text = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)