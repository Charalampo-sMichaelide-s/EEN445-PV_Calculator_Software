from PIL import Image

path = "./Images/cut-logo.png"
image = Image.open(path)
width, height = 300, 120
resized_image = image.resize((width, height))
resized_image.save(path)