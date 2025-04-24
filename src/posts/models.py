from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) 
    author = models.CharField(max_length=20)
    text = models.TextField(blank=False, null=False)

    # Returns the correct url extension to view specific posts
    def get_url(self):
        return reverse("post-path", kwargs={'post_id': self.id}) #f"/post/{self.id}"