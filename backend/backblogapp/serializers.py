from rest_framework import serializers
from.models import post

class postserializers(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = ['id', 'title', 'content', 'slug' ]



        # get_recent_blogs = http//127.0.0.1:8003/blogs/recent
        # specific_blogs = http//127.0.0.1:8003/blogs/:slug






    #     "http://127.0.0.1:5173",
    # "http://127.0.0.1:5174",
    # "http://localhost:5173",
