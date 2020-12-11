# Generated by Django 3.1.3 on 2020-12-02 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('picture', models.URLField()),
                ('consoles', models.ManyToManyField(blank=True, related_name='games', to='catalog.Console')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.player')),
            ],
        ),
    ]
