import os
import shutil
from PIL import Image

# Variables a configurar
original_image_path = '/home/frontera/Documents/Projects/condor_loop/corridor.jpg'  # Ruta del archivo de la imagen original
# Abrir la imagen original y obtener su tamaño
with Image.open(original_image_path) as img:
    original_video_size = img.size  # Tamaño del video original (ancho, alto)
print(original_video_size)
screen_size = (1920, 1080)  # Tamaño de la pantalla (ancho, alto)
crop_folder = '/home/frontera/Documents/Projects/condor_loop/sensorialis/IMG_20240731_144527495/videos'  # Carpeta que contiene los recortes de video
scaled_folder = '/home/frontera/Documents/Projects/condor_loop/sensorialis/IMG_20240731_144527495/scaled_video_crops'  # Carpeta para guardar los recortes de video con nombres actualizados

# Crear la carpeta para los recortes con nombres actualizados si no existe
os.makedirs(scaled_folder, exist_ok=True)

# Factor de escala
scale_x = screen_size[0] / original_video_size[0]
scale_y = screen_size[1] / original_video_size[1]

# Recorrer todos los archivos en la carpeta de recortes
for filename in os.listdir(crop_folder):
    if filename.endswith('.mp4'):  # Asumiendo que los recortes de video están en formato .mp4
        # Extraer las coordenadas del nombre del archivo
        parts = filename.split('_')
        crop_number = parts[1]
        x = int(parts[2])
        y = int(parts[3].split('.')[0])
        
        # Calcular la nueva posición escalada
        new_x = min(int(x * scale_x), screen_size[0] - 1)
        new_y = min(int(y * scale_y), screen_size[1] - 1)
        
        # Generar el nuevo nombre de archivo
        new_filename = f'crop_{crop_number}_{new_x}_{new_y}.mp4'
        
        # Ruta completa para el archivo original y el nuevo archivo
        original_path = os.path.join(crop_folder, filename)
        new_path = os.path.join(scaled_folder, new_filename)
        # Copiar el archivo original al nuevo destino con el nuevo nombre
        shutil.copy2(original_path, new_path)        

print("Todos los recortes de video han sido renombrados y guardados.")

