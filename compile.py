from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


folder_path = "./videos"
output_path = "video_comprimido.mp4"

video_clips = []
    
# Percorre todos os arquivos na pasta
for filename in os.listdir(folder_path):
    if filename.endswith(".mpeg"):  # Verifica se é um arquivo de vídeo (formato pode variar)
        filepath = os.path.join(folder_path, filename)
        clip = VideoFileClip(filepath)
        video_clips.append(clip)

# Combina os clipes de vídeo em um único vídeo
final_clip = concatenate_videoclips(video_clips)

# Salva o vídeo combinado no caminho de saída
final_clip.write_videofile(output_path, codec="libx264")
