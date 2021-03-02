from PIL import Image

imageOriginal = Image.open("desert.jpg")
imageGreen = Image.open("cactus.jpg")

width, height = imageOriginal.size
print(f"Width = {width}, Height = {height}")

pixelsOriginal = imageOriginal.load()
pixelsGreen = imageGreen.load()

for y in range(0,600):
    for x in range(0,800):
        (r, g, b) = pixelsGreen[x, y]
        if g < 200:
            pixelsOriginal[x,y] = pixelsGreen[x,y]

imageOriginal.show()     


imageOriginal = Image.open("sunset.jpg")
imageBoat = Image.open("boat.jpg")

width, height = imageOriginal.size
print(f"Width = {width}, Height = {height}")

pixelsOriginal = imageOriginal.load()
pixelsBoat = imageBoat.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixelsBoat[x, y]
        if g < 100:
            pixelsOriginal[x,y] = pixelsBoat[x,y]

imageOriginal.save("new_boat.jpg")


imageOriginal = Image.open("earth.jpg")
imageSpace = Image.open("spaceshuttle.jpg")

width, height = imageOriginal.size
print(f"Width = {width}, Height = {height}")

pixelsOriginal = imageOriginal.load()
pixelsSpace = imageSpace.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixelsSpace[x, y]
        if g < 195:
            pixelsOriginal[x,y] = pixelsSpace[x,y]

imageOriginal.save("new_space.jpg")


imageOriginal = Image.open("field.jpg")
imageHarvest = Image.open("harvester.jpg")

width, height = imageOriginal.size
print(f"Width = {width}, Height = {height}")

pixelsOriginal = imageOriginal.load()
pixelsHarvest = imageHarvest.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixelsHarvest[x, y]
        if g < 155:
            pixelsOriginal[x,y] = pixelsHarvest[x,y]

imageOriginal.save("new_harvester.jpg")

imageOriginal = Image.open("desert.jpg")
imagehike = Image.open("hiker.jpg")

width, height = imageOriginal.size
print(f"Width = {width}, Height = {height}")

pixelsOriginal = imageOriginal.load()
pixelsHike = imagehike.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixelsHike[x, y]
        if g < 160:
            pixelsOriginal[x,y] = pixelsHike[x,y]

imageOriginal.save("new_hiker.jpg")

imageOriginal = Image.open("snowscape.jpg")
imagePenguin = Image.open("penguin.jpg")

width, height = imageOriginal.size
print(f"Width = {width}, Height = {height}")

pixelsOriginal = imageOriginal.load()
pixelsPenguin = imagePenguin.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixelsPenguin[x, y]
        if g < 200:
            pixelsOriginal[x,y] = pixelsPenguin[x,y]

imageOriginal.save("penguin.jpg")
    
