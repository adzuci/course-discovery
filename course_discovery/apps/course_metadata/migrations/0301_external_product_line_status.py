# Generated by Django 3.2.16 on 2022-11-02 16:59

from django.db import migrations, models
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0300_product_seo_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalmetadata',
            name='product_status',
            field=models.CharField(choices=[('archived', 'Archived'), ('published', 'Published')], default='published', max_length=50, validators=[djchoices.choices.ChoicesValidator({'archived': 'Archived', 'published': 'Published'})]),
        ),
    ]