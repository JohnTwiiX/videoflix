import subprocess
import os
import concurrent.futures

def convertVideos(source):
    new_file_name_480p = source.video_file.path + '_480p.mp4'
    new_file_name_720p = source.video_file.path + '_720p.mp4'
    converted480p = convert480p(source)
    converted720p = convert720p(source)

    if converted480p:
        source.video_file_480p.name = 'videos/' + \
            os.path.basename(new_file_name_480p)
        source.save()
    if converted720p:
        source.video_file_720p.name = 'videos/' + \
            os.path.basename(new_file_name_720p)
        source.save()

def convert480p(source):
    print("In convert480p Funktion")
    new_file_name = source.video_file.path + '_480p.mp4'
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

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(subprocess.run, cmd, capture_output=True, text=True)
        run = future.result()

    if run.returncode == 0:
        print("Konvertierung erfolgreich")
        return True
    else:
        print("Fehler bei der Konvertierung:", run.stderr)

def convert720p(source):
    print("In convert720p Funktion")
    new_file_name = source.video_file.path + '_720p.mp4'
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

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(subprocess.run, cmd, capture_output=True, text=True)
        run = future.result()

    if run.returncode == 0:
        print("Konvertierung erfolgreich")
        return True
    else:
        print("Fehler bei der Konvertierung:", run.stderr)

