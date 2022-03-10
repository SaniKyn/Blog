from django.db import models
from django.urls import reverse, reverse_lazy


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    date = models.DateTimeField(auto_now_add=True, null=True)
    body = models.TextField()

    def __str__(self):
        return '\n'.join((self.title, f'{self.author.username} | {self.date}', '\n', self.body[:140]))

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.post} ⸱ {self.body}"

    def get_absolute_url(self):
        return reverse_lazy("post_detail", args=[str(self.post.id)])
