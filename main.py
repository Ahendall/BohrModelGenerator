from PIL import Image, ImageDraw, ImageFont
import elements as e
import math as m
        
def main():
    # create an array of elements containing the first 20 elements in the periodic table
    elements = e.elements
    
    # Create bohr model for each element
    for element in elements:
        # Create a new image with dimensions 500x500 and a white background
        image = Image.new("RGB", (500, 500), (255, 255, 255))
        
        # add the element name to the image
        font = ImageFont.truetype("arial.ttf", size=40)
        image_draw = ImageDraw.Draw(image)
        image_draw.text((10, 445), element.name, (0, 0, 0), font=font)
        
        
        # Add the element symbol to the image
        font = ImageFont.truetype("arial.ttf", size=100)
        image_draw = ImageDraw.Draw(image)
        x_axis = (410 if len(element.symbol) == 1 else 365)
        image_draw.text((x_axis, 390), element.symbol, (0, 0, 0), font=font)
        
        # Create energy level rings based on period with following radius rule:
        # ring 1: 50px
        # ring 2: 100px
        # ring 3: 150px
        # ring 4: 200px
        for i in range(element.period):
            image_draw.ellipse((250 - (50 * (i + 1)), 250 - (50 * (i + 1)), 250 + (50 * (i + 1)), 250 + (50 * (i + 1))), outline=(0, 0, 0))
        
        # Draw nucleus as red fill, 35px radius circle
        image_draw.ellipse((232, 232, 268, 268), fill=(200, 0, 0))
        
        for i in range(element.number):
            if i < 3:
                drawElectronsRing1(i, image_draw)



            
        
        
        
        # Save the image as a png file with the element name as the file name
                   
        image.save(f'{element.symbol}.png')
        
        
    
def drawElectronsRing1(num, imageDraw, imageWidth=500, imageHeight=500):
    def f(x): return m.sqrt(pow(50, 2) - pow(x, 2))

    x = (imageWidth / 2) - 5
    y = (
        f(num) + (imageHeight / 2) - 5 if isEven(num)
        else (imageHeight / 2) - f(num) - 5
    )

    imageDraw.ellipse((x, y, x + 10, y + 10), fill=(0, 128, 128))

def drawElectronsRing2(num, imageDraw, imageWidth=500, imageHeight=500):
    def f(x): return m.sqrt(pow(100, 2) - pow(x, 2))
    def g(x): return 100 * m.cos((m.pi/2) * x)

    if num <= 3:
        x = (imageWidth / 2) - 5
        y = (
            (imageHeight / 2) + (f(g(num)) * -1) if isEven(num)
            else f(g(num))
        )


def isEven(num): return num % 2 == 0
if __name__ == "__main__":
    main()