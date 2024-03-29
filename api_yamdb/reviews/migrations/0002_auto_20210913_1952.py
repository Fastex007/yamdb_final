# Generated by Django 2.2.16 on 2021-09-13 19:52

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['pub_date'], 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name': 'genre', 'verbose_name_plural': 'genres'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['pub_date'], 'verbose_name': ('review',), 'verbose_name_plural': 'reviews'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['name'], 'verbose_name': 'title', 'verbose_name_plural': 'titles'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='review'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='reviews'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(help_text='Оценка от 1 до 10', validators=[django.core.validators.MaxValueValidator(10, 'Оценка от 1 до 10'), django.core.validators.MinValueValidator(1, 'Оценка от 1 до 10')], verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.Title', verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles', to='reviews.Genre', verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='year'),
        ),
    ]
