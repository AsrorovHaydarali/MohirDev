from django.db import models
from django.urls import reverse
from users_app.models import CustomUser

# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment from {self.author.username}: {self.comment[:100]}"

    def get_absolute_url(self):
        return reverse("comment_detail", args=[str(self.pk)])
