from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    class Meta:
      verbose_name = "پست"
      verbose_name_plural = "پست ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})





class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    body = models.TextField(verbose_name="متن پیام")
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

    class Meta:
      verbose_name = "نظر"
      verbose_name_plural = "نظر ها"




class Newsletter(models.Model):
    email = models.EmailField(unique=True ,verbose_name="ایمیل")

    class Meta:
      verbose_name = "خبرنامه"
      verbose_name_plural = "خبرنامه ها"

    def __str__(self):
        return str(self.email)






class Contact(models.Model):
    name = models.CharField(max_length=80, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    body = models.TextField(verbose_name="متن پیام")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
      verbose_name = "تماس"
      verbose_name_plural = "تماس ها"

    def __str__(self):
        return str(self.name)






# Endd models
