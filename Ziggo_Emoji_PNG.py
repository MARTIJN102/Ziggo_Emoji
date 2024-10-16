import os
import requests

output_folder = 'Ziggo_Emoji/emojis_png'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

base_url = "https://ziggo.engagement.dimelo.com/images/emojione/png/1f"

start = 0
num_images = 999

for i in range(start, start + num_images):
    
    number_str = f"{i:03d}" # Change 3 to 4 if you want to search for more than 999 images
    url = f"{base_url}{number_str}.png"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        image_path = os.path.join(output_folder, f"{number_str}.png")
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {image_path}")
    else:
        print(f"Image not found for: {url}")
