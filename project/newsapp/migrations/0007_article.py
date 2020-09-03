# Generated by Django 3.1 on 2020-09-02 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0006_auto_20200831_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок cтатьи - 80 символов', max_length=80)),
                ('description', models.TextField(help_text='Детальное описание')),
                ('creation_date', models.DateField(help_text='Дата создания')),
                ('update_date', models.DateField(help_text='Дата обновления')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.news')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
