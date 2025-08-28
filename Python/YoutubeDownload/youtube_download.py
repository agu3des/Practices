from pytubefix import Youtube
from pytubefix.cli import on_progress
from pathlib import Path

url = ""
destino = Path("videos_youtube")
destino.mkdir(exist_ok=True)

yt = Youtube(url, on_progress_callback=on_progress)
print(f'Título: {yt.title}\nDuração: {yt.length}s')

yt.streams.get_highest_resolution().download(output_path=destino)
print(f"Download concluído! Vídeo salvo em: {destino}")