import sys

from PIL import Image

images = []

# Image.open(arg) doesn't load a flat array of pixel numbers — it returns a PIL Image object: a wrapper object that holds 
# the pixel data internally, plus metadata like the image's format (PNG, JPEG), size (width × height), and color mode 
# (RGB, RGBA, grayscale, etc.). It's less like "raw numbers" and more like "a smart container that knows how to interpret 
# and manipulate the image," with methods like .save(), .resize(), .convert() built onto it.

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# A GIF file, physically, is one file containing multiple "frames" bundled together with timing info. Pillow's design choice is:
# you don't call some separate "make a gif" function — you call .save() on one Image object, but you tell that call 
# "hey, don't just save yourself alone — bundle in these other images too, as additional frames." That's exactly what save_all=True
# and append_images=images[1:] do together:
# save_all=True tells Pillow's save mechanism "this isn't a single-frame save — treat this as a multi-frame file" 
# (this flag matters for formats like GIF and TIFF that support multiple frames; without it, .save() would just silently save the 
# one image it was called on, ignoring append_images entirely).
# append_images=images[1:] supplies the rest of the frames (images[1], images[2], ...) — everything except images[0], since images[0] 
# is already the image the method's being called on.
# loop = 0(plays forever), loop = n -> once as a base playthrough + 'n' number of times, and then stop.

images[0].save(
        "costumes.gif", save_all = True, append_images = images[1:], duration = 200, loop = 0
) 
