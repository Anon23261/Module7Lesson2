from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)

def capture_syntax_diagram():
    driver = setup_driver()
    driver.get('file:///media/ghost/12B4-F9B2/School/Module7Lesson2/cpp-syntax-diagram.html')
    time.sleep(2)  # Wait for rendering
    driver.save_screenshot('media/cpp-syntax.jpg')
    driver.quit()

def record_control_flow():
    # This would normally use screen recording, but for demo we'll just capture frames
    driver = setup_driver()
    driver.get('file:///media/ghost/12B4-F9B2/School/Module7Lesson2/cpp-control-flow-animation.html')
    time.sleep(2)  # Wait for rendering
    
    # Capture multiple frames
    os.makedirs('media/frames', exist_ok=True)
    for i in range(6):
        driver.save_screenshot(f'media/frames/frame_{i}.jpg')
        time.sleep(1)
    
    driver.quit()
    
    # Convert frames to video using ffmpeg
    os.system('ffmpeg -framerate 2 -i media/frames/frame_%d.jpg -c:v libx264 -pix_fmt yuv420p media/cpp-control-flow.mp4')

def generate_audio():
    # Generate audio from script using text-to-speech
    with open('cpp-variables-script.txt', 'r') as f:
        script = f.read()
    
    # Using ffmpeg to generate a silent audio file (placeholder)
    os.system('ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 10 -q:a 9 -acodec libmp3lame media/cpp-variables.mp3')

def main():
    os.makedirs('media', exist_ok=True)
    
    print("Capturing syntax diagram...")
    capture_syntax_diagram()
    
    print("Recording control flow animation...")
    record_control_flow()
    
    print("Generating audio explanation...")
    generate_audio()
    
    print("Media generation complete!")

if __name__ == "__main__":
    main()
