from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
    )
    content = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()

    post_id = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
