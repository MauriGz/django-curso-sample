# Generated by Django 4.2.6 on 2023-11-22 23:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("learning", "0005_estudiante_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="estudiante",
            name="bio",
            field=models.TextField(blank=True, null=True, verbose_name="Biografía"),
        ),
        migrations.AddField(
            model_name="estudiante",
            name="dob",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Fecha de Nacimiento"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="estudiante",
            name="github",
            field=models.URLField(blank=True, null=True, verbose_name="GitHub"),
        ),
        migrations.AddField(
            model_name="estudiante",
            name="interest",
            field=models.TextField(blank=True, null=True, verbose_name="Intereses"),
        ),
        migrations.AlterField(
            model_name="estudiante",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatar"),
        ),
    ]