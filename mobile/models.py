from django.db import models


class Email(models.Model):
    class Meta:
        db_table = 'email'
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'

    email = models.EmailField(unique=True, verbose_name='E-mail', null=False, blank=False)
    message = models.TextField(verbose_name='Mesazhi', blank=True, null=True)
    date = models.DateField(verbose_name='Data', auto_now_add=True)
    time = models.TimeField(verbose_name='Ora', auto_now_add=True)
    is_read = models.BooleanField(default=False)

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.email
