from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class Post(models.Model):
    class STATUS(models.TextChoices):
        DRAFT = "DRAFT"
        PUBLIC = "PUBLIC"
        ARCHIVED = "ARCHIVED"

    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    author = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=STATUS.choices,
        default=STATUS.PUBLIC,
        max_length=10
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"Post: {self.uuid} published by {self.author.username}"
