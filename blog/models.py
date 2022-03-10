from PIL import Image
from django.db import models
from django.urls import reverse, reverse_lazy
_MAX_SIZE = 300

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

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        if self.header_image:
            filepath = self.header_image.path
            width = self.header_image.width
            height = self.header_image.height
            max_size = max(width, height)
            if max_size > _MAX_SIZE:
                image = Image.open(filepath)

                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS
                )
                image.save(filepath)

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
