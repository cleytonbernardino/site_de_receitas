from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    class Meta:
        ordering = ['-pk']
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    preparation_time = models.IntegerField()
    preparation_unit = models.CharField(max_length=20)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=20)
    is_html = models.BooleanField(default=False)
    preparation_steps = models.TextField()
    cover = models.ImageField(
        upload_to='midia/%Y/%m/%d/', null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.title
