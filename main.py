from PIL import Image, ImageDraw, ImageFont
import elements as e
import math as m
        
def main():
    # create an array of elements containing the first 20 elements in the periodic table
    elements = e.elements
    
    # Create bohr model for each element
    for element in elements:
        # Create a new image with dimensions 500x550 and a white background
        image = Image.new("RGB", (500, 550), (255, 255, 255))

        # add black border to the image
        image_draw = ImageDraw.Draw(image)
        image_draw.rectangle((0, 0, 500, 550), outline=(0, 0, 0), width=3)
        
        # add the element name to the image
        font = ImageFont.truetype("arial.ttf", size=50)
        image_draw.text((6, 475), element.name, (0, 0, 0), font=font)

        # add atomic number and atomic mass to the top left of image
        font = ImageFont.truetype("arial.ttf", size=30)
        image_draw.text((6, 6), f"{element.number}", (0, 0, 0), font=font)
        image_draw.text((6, 36), f"{element.mass}", (0, 0, 0), font=font)

        
        # add proton, neutron, and electron count
        font = ImageFont.truetype("arial.ttf", size=15)
        text = f'Protons: {element.number} | Neutrons: {m.trunc(element.mass - element.number)} | Electrons: {element.number}'
        image_draw.text((10, 530), text, (0, 0, 0), font=font)

        # Add the element symbol to the image
        font = ImageFont.truetype("arial.ttf", size=100)
        image_draw = ImageDraw.Draw(image)
        x_axis = (410 if len(element.symbol) == 1 else 365)
        image_draw.text((x_axis, 450), element.symbol, (0, 0, 0), font=font)

        # add box around the element symbol
        image_draw.rectangle((360, 447, 497, 547), outline=(0, 0, 0))
        
        # Create energy level rings based on element period
        for i in range(element.period):
            image_draw.ellipse((250 - (50 * (i + 1)), 250 - (50 * (i + 1)), 250 + (50 * (i + 1)), 250 + (50 * (i + 1))), outline=(0, 0, 0))
        
        # Draw nucleus as red fill, 35px radius circle
        image_draw.ellipse((232, 232, 268, 268), fill=(200, 0, 0))
        
        for i in range(1, element.number + 1, 1):  
            if i < 3:
                drawElectronsRing1(i, image_draw)
                
            if 2 < i < 11:
                drawElectronsRing2(i, image_draw)

            if 10 < i < 19:
                drawElectronsRing3(i, image_draw)
            
            if 18 < i < 37:
                drawElectronsRing4(i, image_draw)

        
        image.save(f'{element.symbol}.png')
        
        
    
def drawElectronsRing1(num, imageDraw, imageWidth=500, imageHeight=500):
    def f(x): return m.sqrt(pow(50, 2) - pow(x, 2))

    x = (imageWidth / 2) - 5
    y = (
        f(num) + (imageHeight / 2) - 5 if isEven(num)
        else (imageHeight / 2) - f(num) - 5
    )

    imageDraw.ellipse((x, y, x + 10, y + 10), fill=(8, 0, 153))


def drawElectronsRing2(num, imageDraw, imageWidth=500, imageHeight=500):
    num -= 2
    def f(x):
            val = (pow(100, 2) - pow(x, 2))
            return m.sqrt(val)

    # Coord values for electron
    x = 0
    y = 0

    if num <= 3:
        # def g(x): return 100 * m.cos((m.pi/2) * x) <--- Doesn't work
        def g(x): return (100 * x) - 200
        x = (imageWidth/2) + g(num) - 5
        y = f(g(num)) + (imageHeight/2) - 5
    
    if num == 4:
        x = 245
        y = 145

    if 4 < num <= 8:
        def g(x):
            val = 60 * m.cos(m.pi * x)
            return val

        if num < 7:            
            x = (imageWidth/2) + g(num) - 5
            y = f(g(num)) + (imageHeight/2) - 5
        
        if num > 6:           
            x = (imageWidth/2) + g(num) - 5
            y = (f(g(num)) * -1) + (imageHeight/2) - 5

    return imageDraw.ellipse((x, y, x + 10, y + 10), fill=(5, 74, 189))


def drawElectronsRing3(num, imageDraw, imageWidth=500, imageHeight=500):
    num -= 10
    def f(x):
            val = (pow(150, 2) - pow(x, 2))
            return m.sqrt(val)

    # Coord values for electron
    x = 0
    y = 0

    if num <= 3:
        def g(x): return (150 * x) - 300

        x = (imageWidth/2) + g(num) - 5
        y = f(g(num)) + (imageHeight/2) - 5
    
    if num == 4:
        x = 245
        y = 95

    if 4 < num <= 8:
        def g(x):
            val = 120 * m.cos(m.pi * x)
            return val

        if num < 7:            
            x = (imageWidth/2) + g(num) - 5
            y = f(g(num)) + (imageHeight/2) - 5
        
        if num > 6:           
            x = (imageWidth/2) + g(num) - 5
            y = (f(g(num)) * -1) + (imageHeight/2) - 5

    return imageDraw.ellipse((x, y, x + 10, y + 10), fill=(3, 142, 221))


def drawElectronsRing4(num, imageDraw, imageWidth=500, imageHeight=500):
    num -= 18
    def f(x):
            val = (pow(200, 2) - pow(x, 2))
            return m.sqrt(val)

    # Coord values for electron
    x = 0
    y = 0

    if num <= 3:
        def g(x): return (200 * x) - 400

        x = (imageWidth/2) + g(num) - 5
        y = f(g(num)) + (imageHeight/2) - 5
    
    if num == 4:
        x = 243
        y = 45

    if 4 < num <= 8:
        def g(x):
            val = 140 * m.cos(m.pi * x)
            return val

        if num < 7:            
            x = (imageWidth/2) + g(num) - 5
            y = f(g(num)) + (imageHeight/2) - 5
        
        if num > 6:           
            x = (imageWidth/2) + g(num) - 5
            y = (f(g(num)) * -1) + (imageHeight/2) - 5

    imageDraw.ellipse((x, y, x + 10, y + 10), fill=(0, 212, 255))


def isEven(num):
    return num % 2 == 0


if __name__ == "__main__":
    main()