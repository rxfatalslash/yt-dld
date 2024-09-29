import yt_dlp
import os
import sys
import platform
import subprocess
import requests
import importlib.metadata

def install_reqs():
    # Requirements file
    reqs_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')

    try:
        # Extract each requirement in file
        with open(reqs_file, 'r') as file:
            reqs = file.read().splitlines()
    except FileNotFoundError:
        print(f"{reqs_file} not found")
        sys.exit(1)

    # Install each requirement
    for req in reqs:
        pkg_name = req.split('==')[0]
        try:
            importlib.metadata.version(pkg_name)
        except importlib.metadata.PackageNotFoundError:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', req])

def download_audio(url, dest):
    # System verification
    match platform.system():
        case 'Windows':
            ffmpeg = './resources/ffmpeg-7.0.2-win/ffmpeg.exe'
        case 'Linux':
            ffmpeg = './resources/ffmpeg-7.0.2-linux/ffmpeg'
        case _:
            print("Platform not supported")

    # yt-dlp tool options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'outtmpl': os.path.join(dest, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg,
    }

    try:
        # Download and convert file
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "File downloaded successfully"
    except Exception as e:
        return f"An error occurred while downloading: {e}"