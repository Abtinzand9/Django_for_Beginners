from django.db import models
from django.urls import reverse
# Create your models here.
class Blog (models.Model):
    title = models.models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete =models.CASCADE,
    )
    body = models.TextField()
    def __str__(self):
        self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

