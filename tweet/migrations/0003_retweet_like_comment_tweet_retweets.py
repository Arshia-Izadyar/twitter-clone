# Generated by Django 4.2 on 2023-10-09 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tweet", "0002_alter_tweet_image_alter_tweet_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="Retweet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "original_tweet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tweet.tweet"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "original_tweet")},
            },
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
                (
                    "tweet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="tweet.tweet",
                        verbose_name="Tweet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="./uploads",
                        verbose_name="Image",
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True, null=True, upload_to="./files", verbose_name="Video"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
                (
                    "parent_comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="tweet.comment",
                        verbose_name="Parent Comment",
                    ),
                ),
                (
                    "tweet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="tweet.tweet",
                        verbose_name="Tweet",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="tweet",
            name="retweets",
            field=models.ManyToManyField(
                through="tweet.Retweet", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
