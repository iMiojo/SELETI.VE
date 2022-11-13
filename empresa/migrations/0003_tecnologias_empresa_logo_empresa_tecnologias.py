# Generated by Django 4.1.3 on 2022-11-08 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_empresa_nicho_mercado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnologia', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo_empresa'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='tecnologias',
            field=models.ManyToManyField(to='empresa.tecnologias'),
        ),
    ]
