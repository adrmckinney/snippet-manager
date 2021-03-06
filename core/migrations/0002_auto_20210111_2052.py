# Generated by Django 3.1.5 on 2021-01-11 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snippet_title', models.CharField(max_length=100)),
                ('snippet_code', models.TextField()),
                ('snippet_description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ManyToManyField(related_name='snippets', to='core.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='core.snippet'),
        ),
    ]
