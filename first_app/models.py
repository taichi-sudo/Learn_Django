from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '記事'
