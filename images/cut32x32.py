from PIL import Image
import os

# Charger l'image
image_path = "C:\\Users\\5INFO\\Desktop\\5info\\JS\\survival-game\\images\\pngegg.png" 
img = Image.open(image_path)

# Dimensions des tuiles
tile_width, tile_height = 112, 136

# Dossier de sortie
output_dir = "tiles"
os.makedirs(output_dir, exist_ok=True)

# Découpe de l'image
img_width, img_height = img.size
for y in range(0, img_height, tile_height):
    for x in range(0, img_width, tile_width):
        if x > 0:
            tile = img.crop(((x + (x/6)), y, x + tile_width, y + tile_height))

        tile = img.crop((x, y, x + tile_width, y + tile_height))
        tile_filename = f"tile_{y//tile_height}_{x//tile_width}.png"
        tile.save(os.path.join(output_dir, tile_filename))

print("Découpage terminé. Les tuiles sont dans le dossier 'tiles'.")