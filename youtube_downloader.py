import os
import yt_dlp
from InquirerPy import inquirer

def download_video(youtube_url, format_id, output_path):
    ydl_opts = {
        'format': format_id,
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        print(f"[green]Baixado:[/green] {info_dict['title']}")

def download_audio(youtube_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        print(f"[green]Baixado:[/green] {info_dict['title']}")

def download_and_convert_to_mp3(youtube_url, output_path):
    # Cria a pasta de saída se não existir
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # A função extract_info baixa todos os vídeos da playlist se a URL for de uma playlist
            info_dict = ydl.extract_info(youtube_url, download=True)
            print(f"[green]Baixados:[/green] {info_dict['title']}")
    except Exception as e:
        print(f"[red]Um erro ocorreu:[/red] {str(e)}")

def main():
    action = inquirer.select(
        message="Escolha uma opção:",
        choices=["Baixar vídeo em MP4", "Baixar áudio em MP3", "Baixar playlist em MP3"],
    ).execute()

    youtube_url = input("Insira o URL do vídeo ou playlist do YouTube: ")
    
    if action == "Baixar playlist em MP3":
        download_and_convert_to_mp3(youtube_url, './downloads')
    elif action == "Baixar áudio em MP3":
        download_audio(youtube_url, './downloads')
    else:
        # Baixar informações do vídeo
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            formats = info_dict['formats']
            
            # Filtrar apenas os formatos MP4 disponíveis
            available_resolutions = {}
            for f in formats:
                if f['ext'] == 'mp4' and f['vcodec'] != 'none':  # Certifica-se de que a extensão seja mp4
                    resolution = f.get('format_note', f['format_id'])  # Use format_id se format_note estiver ausente
                    
                    # Filtrar apenas resoluções que têm 'p' no formato
                    if 'p' in resolution:
                        available_resolutions[resolution] = f  # Armazena o dicionário completo do formato

        # Cria uma lista das opções disponíveis
        available_choices = []
        for res, f in available_resolutions.items():
            available_choices.append(f"{res} - {f['format_id']} - {f['width']}x{f['height']} pixels")

        # Usando InquirerPy para permitir a navegação interativa
        resolution_choice = inquirer.select(
            message="Escolha a resolução do vídeo:",
            choices=available_choices,
        ).execute()

        # Extrai o format_id da escolha da resolução
        chosen_format_id = resolution_choice.split(' - ')[1]  # Obtém o format_id
        download_video(youtube_url, chosen_format_id, './downloads')

if __name__ == "__main__":
    main()
