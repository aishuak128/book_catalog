# Generated by Django 4.2.5 on 2023-09-05 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author'),
        ),
        migrations.DeleteModel(
            name='LookupAuthorBook',
        ),
    ]
