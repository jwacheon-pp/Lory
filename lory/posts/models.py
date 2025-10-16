from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class PostManager(models.Manager):
    def create_post(self, **extra_fields):
        post = self.model(**extra_fields)
        post.save()
        return post
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    creator = models.ForeignKey(
        User,                    
        on_delete=models.CASCADE, 
        related_name="posts"      
    )
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    objects = PostManager()

    def __str__(self):
        return f"{self.title} by {self.creator_id}"

    class Meta:
        db_table = "Post"
        ordering = ["-created_at"]