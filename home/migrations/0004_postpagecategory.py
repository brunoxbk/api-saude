# Generated by Django 4.2.11 on 2024-03-21 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_postpage_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='home.category')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='home.postpage')),
            ],
            options={
                'unique_together': {('page', 'category')},
            },
        ),
    ]