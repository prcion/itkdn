from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class New(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to = 'post_images')
    nr = models.PositiveIntegerField()
    def __str__(self):
        return str(self.title)
    def __lt__(self, arg):
        return self.date > arg.date

class News(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to = 'post_images')
    nr = models.PositiveIntegerField()
    post = models.SmallIntegerField()
    def __str__(self):
        return str(self.title)
    def __lt__(self, arg):
        return self.date > arg.date
