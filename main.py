from PIL import Image, ImageDraw, ImageFont
import elements as e
        
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
        
        # Draw nucleus as purple fill, 35px radius circle
        image_draw.ellipse((232, 232, 268, 268), fill=(128, 0, 128))
        
        # draw electrons on orbit rings from line 31 with rule of 8 electrons per ring
        for i in range(element.number):
            # calculate the x and y coordinates of the electron
            x = 250 + (50 * (i // 8 + 1)) * (1 if i % 2 == 0 else -1)
            y = 250 + (50 * (i // 8 + 1)) * (1 if i % 4 < 2 else -1)
            # draw the electron as a green circle
            image_draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(0, 128, 0))            
        image.save(f'{element.symbol}.png')
        
        
    
    
    
if __name__ == "__main__":
    main()