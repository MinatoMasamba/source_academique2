# Generated by Django 5.1.2 on 2024-10-31 06:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('maman', models.FileField(blank=True, null=True, upload_to='cours/')),
                ('promotion', models.CharField(choices=[('L1', 'Licence 1'), ('PREPA', 'Préparatoire')], max_length=5)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cours',
                'verbose_name_plural': 'Cours',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('fichier', models.FileField(upload_to='examens/')),
                ('promotion', models.CharField(choices=[('L1', 'Licence 1'), ('PREPA', 'Préparatoire')], max_length=5)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_donnee', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Interro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('fichier', models.FileField(upload_to='interros/')),
                ('promotion', models.CharField(choices=[('L1', 'Licence 1'), ('PREPA', 'Préparatoire')], max_length=5)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_donnee', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('fichier', models.FileField(upload_to='notes/')),
                ('promotion', models.CharField(choices=[('L1', 'Licence 1'), ('PREPA', 'Préparatoire')], max_length=5)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('fichier', models.FileField(upload_to='tp/')),
                ('promotion', models.CharField(choices=[('L1', 'Licence 1'), ('PREPA', 'Préparatoire')], max_length=5)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_donnee', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.CharField(choices=[('L1', 'Licence 1'), ('PREPA', 'Préparatoire')], max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('numero_whatsapp', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cours',
                'verbose_name_plural': 'Cours',
            },
        ),
    ]
