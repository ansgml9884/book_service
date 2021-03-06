# Generated by Django 2.1.7 on 2019-03-27 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('user_id', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name=9)),
                ('user_name', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=15)),
                ('borrow_num', models.IntegerField(default=0)),
                ('overdue', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name=8),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.User_info'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.User_info'),
        ),
    ]
