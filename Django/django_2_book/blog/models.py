from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """Model for blog posts"""

    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))

    # Odpowiada Varcharowi
    title = models.CharField(max_length=250)
    # Etykieta z literami, cyframi - oraz _ używana do tworzenie przyjaznym SEO url'i postów
    # tworzone na podstawie daty publikacji dzięki unique_for_date
    # wartości będą unikatowe nawet dla tych samych dat
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    # related_name dodaje nazwę odwróconej relacji od User do Post
    # WARN napisał że dopisze o tym później
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # Odpowiada text'owi
    body = models.TextField()
    # Data publikacji - zmienia się
    publish = models.DateTimeField(default=timezone.now)
    # auto_add_now doda datę przy stworzeniu i zignoruje wszystkie próby zmiany
    created = models.DateTimeField(auto_now_add=True)
    # auto_now sprawia że pole aktualizuje się automatycznie przy zapisywaniu obiektu
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )

    class Meta:
        # Ostatnio publikowane posty jako pierwsze
        ordering = ("-publish",)

    def __str__(self):
        return self.title
