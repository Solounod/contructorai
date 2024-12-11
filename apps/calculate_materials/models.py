from django.db import models
from django.utils.text import slugify
##from django.contrib.auth import get_user_model
##
##
##User = get_user_model()
##
### Create your models here.
##class UserPrompt(models.Model):
##    user_promps = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prompts')
##    prompt_input = models.TextField()
##    response_output = models.TextField(null=True, blank=True)

class PrompMainAi(models.Model):
    promp_main = models.TextField(
        verbose_name='Prompt'
    )
    title = models.CharField(
        verbose_name='Titulo',
        max_length=100
        )
    slug_promp = models.SlugField(
        max_length=100,
        verbose_name='Slug',
        unique=True,
        )
    date_create = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        verbose_name='Fecha creacion'
    )
    update_datetime = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name='Fecha modificacion'
    )


    def save(self, *args, **kwarg):
        if not self.slug_promp:
            self.slug_promp = slugify(self.title)
        super().save(*args, **kwarg)

    def __str__(self):
        return f"{self.title} - {self.slug_promp}"
