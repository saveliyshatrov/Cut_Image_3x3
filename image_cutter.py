from PIL import Image

im = Image.open('CAR.JPG')
width, height = im.size   #show size of Image
print('height:', height)
print('width:', width)
left = [0,1008,2016]
top = [0,1008,2016]
right = [1008,2016,3024]
bottom = [1008,2016,3024]

counter = 1
if __name__ == "__main__":
    for u in range(len(left)):
        for z in range(len(left)):
            im1 = im.crop((left[z], top[u], right[z], bottom[u]))
            im1 = im1.save("{}.png".format(counter))
            print('Image:{}'.format(counter))
            counter += 1 