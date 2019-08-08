# Generated by Django 2.1.7 on 2019-03-25 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=8, verbose_name=8)),
                ('book_name', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=15)),
                ('year', models.IntegerField(verbose_name=4)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=9, verbose_name=9)),
                ('user_name', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=15)),
                ('borrow_num', models.IntegerField(default=0)),
                ('overdue', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.User'),
        ),
    ]
