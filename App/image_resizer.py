from PIL import Image

image = Image.open("./Images/pv-map-marker.png")
width, height = 64, 64
resized_image = image.resize((width, height))
resized_image.save("./Images/pv-map-marker.png")