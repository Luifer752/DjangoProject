from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='books/profile_images', null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Books(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    cover_img = models.ImageField(upload_to="books/covers")
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book: {self.title} {self.author}"


class Genre(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ['title'] # sorted by field

    def __str__(self):
        return f"Genre: {self.title}"
