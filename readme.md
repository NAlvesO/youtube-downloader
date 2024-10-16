# Manual de Uso do Downloader de Vídeos do YouTube

Este projeto é um downloader de vídeos do YouTube, que permite baixar vídeos em formato MP4, áudios em formato MP3, e playlists inteiras em MP3.

## Requisitos

- Python 3.6 ou superior
- `yt-dlp`
- `InquirerPy`
- **ATENÇÃO:** É NECESSÁRIO A BIBLIOTECA **FFmpeg** para a conversão de áudio. Sem ela, o download de áudio não funcionará.

## Instalação

### 1. Clone o Repositório

## Primeiro, clone este repositório em sua máquina local:

```
git clone https://github.com/codingwithvm/youtube-downloader

```

### 2. Instale as Dependências

Execute o seguinte comando para instalar as dependências necessárias:

```
pip install yt-dlp InquirerPy
```

### 3. Instale o FFmpeg

#### **Windows:**
1. Baixe o FFmpeg em [FFmpeg Downloads](https://ffmpeg.org/download.html).
2. Extraia o conteúdo do arquivo ZIP.
3. Adicione o caminho da pasta `bin` do FFmpeg ao `PATH` do seu sistema:
   - Pesquise por "Variáveis de Ambiente" no menu Iniciar.
   - Na seção "Variáveis do sistema", selecione "Path" e clique em "Editar".
   - Adicione o caminho da pasta `bin` do FFmpeg (ex: `C:\ffmpeg\bin`).

#### **Linux:**
```
sudo apt update
sudo apt install ffmpeg
```

#### **macOS:**
```
brew install ffmpeg
```

## Uso

### 1. **Execute o programa:**

   No terminal, navegue até o diretório do projeto e execute:

   ```
   python3 youtube_downloader.py
   ```
   ou
   ```
   python youtube_downloader.py
   ```

### 2. **Escolha a opção desejada:**
   - `Baixar vídeo em MP4`: Baixa um vídeo específico.
   - `Baixar áudio em MP3`: Baixa apenas o áudio de um vídeo específico.
   - `Baixar playlist em MP3`: Baixa todos os vídeos de uma playlist como arquivos MP3.

### 3. **Insira o URL do vídeo ou playlist:**
   - Após escolher a opção, você será solicitado a inserir o URL do vídeo ou playlist do YouTube.

### 4. **Escolha a resolução (apenas para vídeos):**
   - Se você escolheu baixar um vídeo, será solicitado que você selecione a resolução desejada entre as opções disponíveis.

### 5. **Aguarde o download:**
   - O programa fará o download do vídeo ou áudio na pasta `downloads` do diretório atual.