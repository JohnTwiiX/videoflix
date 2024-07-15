import subprocess
import os

def convertVideos(source):
    print("In convertVideos Funktion")
    new_file_name_480p = source.video_file.path + '_480p.mp4'
    new_file_name_720p = source.video_file.path + '_720p.mp4'
    convert480p(source, new_file_name_480p)
    convert720p(source, new_file_name_720p)

def convert480p(source, new_file_name):
    print("In convert480p Funktion")
    cmd = [
        'ffmpeg',
        '-i', source.video_file.path,
        '-s', 'hd480',
        '-c:v', 'libx264',
        '-crf', '23',
        '-c:a', 'aac',
        '-strict', '-2',
        new_file_name
    ]
    print(f"Ausführen von Befehl: {' '.join(cmd)}")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    print(f"ffmpeg Ausgabe: {stdout}")
    print(f"ffmpeg Fehler: {stderr}")

    if process.returncode == 0:
        print("Konvertierung erfolgreich")
        source.video_file_480p.name = 'videos/' + os.path.basename(new_file_name)
        source.save()
    else:
        print("Fehler bei der Konvertierung:", stderr)

def convert720p(source, new_file_name):
    print("In convert720p Funktion")
    cmd = [
        'ffmpeg',
        '-i', source.video_file.path,
        '-s', 'hd720',
        '-c:v', 'libx264',
        '-crf', '23',
        '-c:a', 'aac',
        '-strict', '-2',
        new_file_name
    ]
    print(f"Ausführen von Befehl: {' '.join(cmd)}")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    print(f"ffmpeg Ausgabe: {stdout}")
    print(f"ffmpeg Fehler: {stderr}")

    if process.returncode == 0:
        print("Konvertierung erfolgreich")
        source.video_file_720p.name = 'videos/' + os.path.basename(new_file_name)
        source.save()
    else:
        print("Fehler bei der Konvertierung:", stderr)
