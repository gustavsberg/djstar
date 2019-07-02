from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #auth
    thumb = models.ImageField(default='image.png', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body)>40:
            return self.body[:40] + '...'
        else:
            return self.body
