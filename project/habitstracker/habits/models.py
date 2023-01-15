from django.db import models


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Posts', models.DO_NOTHING)
    user = models.ForeignKey('UsersList', models.DO_NOTHING)
    publish_date = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class Habbits(models.Model):
    habbit_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UsersList', models.DO_NOTHING)
    habbit_type = models.BinaryField()
    habbit_desc = models.TextField(blank=True, null=True)
    habbit_name = models.TextField()
    habbit_days_target = models.TextField()  # This field type is a guess.
    success_activity = models.TextField()
    success_range = models.TextField()
    success_amount = models.TextField()  # This field type is a guess.
    success_unit = models.TextField()

    class Meta:
        managed = False
        db_table = 'habbits'


class HabbitsTracker(models.Model):
    habbit_tracker_id = models.AutoField(primary_key=True)
    habbit = models.ForeignKey(Habbits, models.DO_NOTHING, to_field=None)
    habbit_type = models.BinaryField()
    date = models.TextField()
    yes_no_value = models.BinaryField(blank=True, null=True)
    success_amount_value = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'habbits_tracker'


class Likes(models.Model):
    like_id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Posts', models.DO_NOTHING, to_field=None)
    user = models.ForeignKey('UsersList', models.DO_NOTHING)
    publish_date = models.TextField()
    like_value = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'likes'


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UsersList', models.DO_NOTHING)
    publish_date = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'posts'


class UsersList(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    occupation = models.TextField()
    email = models.TextField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'users_list'
