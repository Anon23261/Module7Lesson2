import os
import subprocess
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_syntax_image():
    # Create a new image with a white background
    width = 800
    height = 600
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Draw title
    draw.text((50, 30), 'C++ Program Structure', fill='black', font=None, size=24)
    
    # Draw boxes
    boxes = [
        (50, 80, 'Header Files', '#include <iostream>\n#include <string>'),
        (50, 200, 'Main Function', 'int main() {\n    // code here\n    return 0;\n}'),
        (50, 350, 'Variables', 'int x = 5;\ndouble y = 3.14;\nstring s = "hello";')
    ]
    
    for y_pos, (x, y, title, content) in enumerate(boxes):
        # Draw box
        draw.rectangle((x, y, x + 300, y + 100), outline='black')
        # Draw title
        draw.text((x + 10, y + 10), title, fill='black')
        # Draw content
        lines = content.split('\n')
        for i, line in enumerate(lines):
            draw.text((x + 10, y + 40 + i*20), line, fill='black')
    
    # Save the image
    os.makedirs('media', exist_ok=True)
    image.save('media/cpp-syntax.jpg')

def create_dummy_video():
    # Create a simple video file using ffmpeg
    os.makedirs('media', exist_ok=True)
    subprocess.run([
        'ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=blue:s=320x240:d=5',
        '-vf', 'drawtext=text=\'C++ Control Flow\':fontcolor=white:fontsize=24:x=(w-text_w)/2:y=(h-text_h)/2',
        'media/cpp-control-flow.mp4'
    ])

def create_dummy_audio():
    # Create a simple audio file using ffmpeg
    os.makedirs('media', exist_ok=True)
    subprocess.run([
        'ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono',
        '-t', '5', '-q:a', '9', '-acodec', 'libmp3lame',
        'media/cpp-variables.mp3'
    ])

def main():
    print("Creating syntax diagram...")
    create_syntax_image()
    
    print("Creating control flow video...")
    create_dummy_video()
    
    print("Creating audio explanation...")
    create_dummy_audio()
    
    print("Media generation complete!")

if __name__ == "__main__":
    main()
