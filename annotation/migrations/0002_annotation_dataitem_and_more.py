# Generated by Django 5.2 on 2025-05-27 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0001_initial'),
        ('dataitem', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='dataitem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dataitem.dataitem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='annotation',
            name='last_modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_modifiede_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='text',
            field=models.TextField(),
        ),
    ]
