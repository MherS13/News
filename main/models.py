from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

# News model


class News(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='imgs/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
