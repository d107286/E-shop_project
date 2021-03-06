# Generated by Django 2.1.8 on 2019-10-07 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_number', models.CharField(max_length=32)),
                ('goods_name', models.CharField(max_length=32)),
                ('goods_price', models.FloatField()),
                ('goods_count', models.IntegerField()),
                ('goods_location', models.CharField(max_length=32)),
                ('goods_safe_date', models.IntegerField()),
                ('goods_pro_time', models.DateField(auto_now=True)),
                ('goods_status', models.IntegerField()),
                ('goods_description', models.TextField(default='好吃还不贵')),
                ('picture', models.ImageField(upload_to='seller/img')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_type', models.CharField(max_length=32)),
                ('goods_description', models.TextField()),
                ('picture', models.ImageField(default='buyer/images/banner05.jpg', upload_to='buyer/images')),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=32, null=True)),
                ('adress', models.TextField(blank=True, null=True)),
                ('User_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Valid_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_content', models.CharField(max_length=32)),
                ('code_user', models.EmailField(max_length=254)),
                ('code_time', models.DateTimeField(auto_now=True)),
                ('code_state', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Seller.LoginUser'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Seller.GoodsType'),
        ),
    ]
