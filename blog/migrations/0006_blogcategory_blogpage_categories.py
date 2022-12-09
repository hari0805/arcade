# Generated by Django 4.1.4 on 2022-12-09 11:53

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("blog", "0005_blogtagindexpage"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogCategory",
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
                ("name", models.CharField(max_length=255)),
                (
                    "icon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={"verbose_name_plural": "blog categories",},
        ),
        migrations.AddField(
            model_name="blogpage",
            name="categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="blog.blogcategory"
            ),
        ),
    ]
