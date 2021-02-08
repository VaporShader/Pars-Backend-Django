from django.db import models


class UserPosts(models.Model):
    Avatar = models.FileField(max_length=100, default="")
    Name = models.CharField(max_length=128, default="")
    Date = models.DateTimeField(blank=True, null=True)
    Title = models.CharField(max_length=128, default="")
    Media = models.FileField(max_length=100, default="")
    Text = models.TextField(default="")
    Likes = models.BigIntegerField(default=0)
    Dislikes = models.BigIntegerField(default=0)

    def __str__(self):
        return (self.Name + " - " + self.Title)
