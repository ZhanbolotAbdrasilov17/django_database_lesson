from django.db import models

class UpImages(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название графы')
    image = models.ImageField(upload_to='up_images/', blank=True, null=True)
    main_text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Картинки верхней части'
        verbose_name = 'Картинка верхней части'