from PIL import Image

file_in = "colo.png"
img = Image.open(file_in).convert('RGB')

file_out = "test1.bmp"
img.save(file_out)
