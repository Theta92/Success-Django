# Generated by Django 4.2.3 on 2023-07-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('studentreg', '0003_student_gender_alter_module_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='courses_allowed',
            field=models.ManyToManyField(related_name='modules', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='date_of_registration',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='student_photos/'),
        ),
    ]