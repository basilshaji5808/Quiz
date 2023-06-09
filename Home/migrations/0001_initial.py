# Generated by Django 4.1.1 on 2023-03-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Django',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dot_Net',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Java',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JavaScript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node_JS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PHP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
