from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

url = "https://www.youtube.com/watch?v=Cd8-OOlliaY&list=RDCd8-OOlliaY&start_radio=1"
destino = Path("videos_youtube")
destino.mkdir(exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)
print(f'Título: {yt.title}\nDuração: {yt.length}s')

yt.streams.get_highest_resolution().download(output_path=destino)
print(f"Download concluído! Vídeo salvo em: {destino}")