# Generated by Django 4.1.7 on 2023-03-08 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='', upload_to='profile_pics/None')),
                ('bio', models.TextField()),
                ('style', models.CharField(blank=True, choices=[('Hiphop', 'Hiphop'), ('FreeStyle', 'FreeStyle'), ('Contemporary', 'Contemporary'), ('lock&pop', 'lock&pop')], max_length=50, null=True)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('dancer', 'dancer')], max_length=50)),
                ('team', models.CharField(blank=True, choices=[('admin', 'admin'), ('dancer', 'dancer')], default='KalaNidhi', max_length=50)),
                ('slug', models.SlugField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]