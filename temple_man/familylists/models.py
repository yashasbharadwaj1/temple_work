from django.db import models
from django.urls import reverse

class Family(models.Model):
    options = (
        ('sankastaharaganapati', 'sankasta hara'),
        ('satyanarayana', 'satyanarayana'),
        ('regulars','regular')
    )     
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=250)
    category = models.CharField(max_length=60, choices=options, default='draft')
   
    def get_absolute_url(self):
        return reverse('family', args=[self.slug])

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title


