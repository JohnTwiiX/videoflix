import os
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django_rq import get_queue
from .models import Video
from .tasks import convertVideos

@receiver(post_save, sender=Video)
def auto_convert_file_on_save(sender, instance, created, **kwargs):
    print('Signal empfangen: auto_convert_file_on_save')
    if created:
        print('Neues Video erstellt, Konvertierung wird gestartet')
        queue = get_queue('default', autocommit=True)
        queue.enqueue(convertVideos, instance)


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.video_file:
        video_file_path = instance.video_file.path
        if os.path.isfile(video_file_path):
            os.remove(video_file_path)

    if instance.video_file_480p:
        video_file_path_480p = instance.video_file_480p.path
        if os.path.isfile(video_file_path_480p):
            os.remove(video_file_path_480p)

    if instance.video_file_720p:
        video_file_path_720p = instance.video_file_720p.path
        if os.path.isfile(video_file_path_720p):
            os.remove(video_file_path_720p)

    if instance.cover_file:
        cover_file_path = instance.cover_file.path
        if os.path.isfile(cover_file_path):
            os.remove(cover_file_path)
