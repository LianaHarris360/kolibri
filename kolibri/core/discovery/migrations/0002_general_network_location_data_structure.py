# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-06 09:49
import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("discovery", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="DynamicNetworkLocation",
            fields=[],
            options={"proxy": True, "indexes": []},
            bases=("discovery.networklocation",),
        ),
        migrations.CreateModel(
            name="StaticNetworkLocation",
            fields=[],
            options={"proxy": True, "indexes": []},
            bases=("discovery.networklocation",),
        ),
        migrations.AlterModelOptions(
            name="networklocation", options={"ordering": ["added"]}
        ),
        migrations.AddField(
            model_name="networklocation",
            name="dynamic",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="networklocation",
            name="nickname",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="networklocation",
            name="added",
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name="networklocation",
            name="id",
            field=models.CharField(
                default=uuid.uuid4,
                editable=False,
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
