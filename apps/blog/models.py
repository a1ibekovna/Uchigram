from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to = "category_icons/")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"(self.name)"
    
class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    image = models.ImageField(upload_to="publications/", null=True, blank=True)
    content = models.TextField()
    is_archived = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='publications')
    create = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return f"{self.user.username}"