# Generated by Django 2.2.3 on 2019-08-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_email_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='email',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Mesazhi'),
        ),
    ]
