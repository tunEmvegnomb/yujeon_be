# Generated by Django 4.0.6 on 2022-07-05 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('image', models.ImageField(upload_to='uploads')),
                ('artimage', models.URLField(default='', verbose_name='유화이미지')),
                ('desc', models.TextField(verbose_name='작품설명')),
                ('cost', models.IntegerField(default=3, verbose_name='가격')),
                ('is_mine', models.BooleanField(verbose_name='소유여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('is_exposure', models.BooleanField(verbose_name='노출여부')),
                ('on_sale', models.BooleanField(default=True, verbose_name='판매여부')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('like', models.ManyToManyField(blank=True, related_name='좋아요', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='소유자')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='게시글')),
            ],
        ),
    ]
