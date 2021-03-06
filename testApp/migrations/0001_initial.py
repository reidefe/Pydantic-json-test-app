# Generated by Django 3.1.7 on 2021-03-16 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=90, verbose_name="TestApp name")),
                ("data", models.JSONField(verbose_name="TestApp json data")),
            ],
            options={
                "verbose_name": "",
                "verbose_name_plural": "",
                "db_table": "",
            },
        ),
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=90)),
                ("year", models.DateTimeField()),
                ("duration", models.DecimalField(decimal_places=2, max_digits=10)),
                ("data", models.JSONField()),
                (
                    "actor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="testApp.actor"
                    ),
                ),
            ],
            options={
                "verbose_name": "DefaultApp",
                "verbose_name_plural": "Defa   title = ultApps",
            },
        ),
    ]
