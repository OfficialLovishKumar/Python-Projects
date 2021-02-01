from PIL import Image, ImageColor, ImageFont, ImageDraw
import random

def randomColorGenerator():
    colorList = ["red", "blue", "orange", "green"]
    return colorList[random.randint(0, len(colorList) - 1)]

color = randomColorGenerator()

def main():
    # Initializing Image
    imgColor = ImageColor.getcolor(color, 'RGB')
    imgSize = (200, 200)
    img = Image.new('RGB', imgSize, imgColor)
    
    username = input("Enter your name : ")
    
    filePath = f"/home/anonymous/Programming/Python Projects/Profile-Image-Maker/Images/{username}.png"
    
    # Adding Text On Image
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/home/anonymous/Programming/Python Projects/Profile-Image-Maker/Avenir-Medium.ttf", 36)
    draw.text((87, 80), username[0].capitalize(), (255, 255, 255), font=font)

    # Saving Image
    img.save(filePath)

if __name__ == "__main__":
    main()
