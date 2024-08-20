from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    cover_file = serializers.SerializerMethodField()
    video_file = serializers.SerializerMethodField()
    video_file_720p = serializers.SerializerMethodField()
    video_file_480p = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'createdTime', 'cover_file', 'video_file', 'video_file_720p', 'video_file_480p']

    def get_cover_file(self, obj):
        return self.get_relative_url(obj.cover_file)

    def get_video_file(self, obj):
        return self.get_relative_url(obj.video_file)

    def get_video_file_720p(self, obj):
        return self.get_relative_url(obj.video_file_720p)

    def get_video_file_480p(self, obj):
        return self.get_relative_url(obj.video_file_480p)

    def get_relative_url(self, file_field):
        if file_field:
            return file_field.url
        return None
