from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from ecommerce.utils import unique_slug_generator_for_category

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
    slug = models.SlugField(max_length=200, null=True, blank=True)
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

# --- Slug ---
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_for_category(instance)

pre_save.connect(slug_generator, sender=Category)