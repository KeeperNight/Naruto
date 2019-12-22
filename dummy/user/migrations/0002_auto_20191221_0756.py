# Generated by Django 3.0.1 on 2019-12-21 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_stat', models.CharField(blank=True, choices=[('C', 'Completed'), ('R', 'Reading...'), ('CC', 'Yet to complete'), ('NS', 'Not Started')], max_length=4)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='books',
            field=models.ManyToManyField(through='user.Read', to='book.Book'),
        ),
    ]