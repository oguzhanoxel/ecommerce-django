from django.db import models

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
        )
    category_name = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='categories',
        null=True,
        blank=True,
    )    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name