# Generated by Django 4.2.10 on 2024-03-07 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_viewprofile"),
        ("content", "0005_storyviewer_timestamp_alter_viewer_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Viewer",
            new_name="ViewerPost",
        ),
    ]