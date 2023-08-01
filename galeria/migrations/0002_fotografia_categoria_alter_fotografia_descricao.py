# Generated by Django 4.2 on 2023-05-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]