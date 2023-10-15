from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='books/profile_images', null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Author: {self.first_name} {self.last_name}"


class Books(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    cover_img = models.ImageField(upload_to="books/covers")
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book: {self.title} {self.author}"