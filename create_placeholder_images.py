#!/usr/bin/env python3
"""
Script to create placeholder images for the TactileVLA website.
This helps visualize the website layout before adding actual content.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_placeholder_image(width, height, text, filename, bg_color=(240, 240, 240), text_color=(100, 100, 100)):
    """Create a placeholder image with text."""
    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()
    
    # Calculate text position (center)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save image
    img.save(filename)
    print(f"Created: {filename}")

def main():
    """Create all placeholder images."""
    # Create assets directory if it doesn't exist
    os.makedirs("assets/figures", exist_ok=True)
    os.makedirs("assets/videos", exist_ok=True)
    
    # Hero image (main cover)
    create_placeholder_image(800, 600, "TactileVLA\nHero Image", 
                           "assets/figures/tactilevla_hero.png", 
                           bg_color=(200, 220, 240), text_color=(50, 50, 100))
    
    # Architecture diagram
    create_placeholder_image(1000, 600, "TactileVLA\nArchitecture", 
                           "assets/figures/tactilevla_architecture.png", 
                           bg_color=(240, 240, 200), text_color=(100, 100, 50))
    
    # Experiment GIFs
    for i in range(1, 7):
        create_placeholder_image(300, 200, f"Experiment {i}", 
                               f"assets/figures/experiment{i}.gif", 
                               bg_color=(220, 240, 220), text_color=(50, 100, 50))
    
    # Create a simple video placeholder (actually a static image)
    create_placeholder_image(640, 480, "Demo Video 1", 
                           "assets/videos/tactilevla_demo1.mp4", 
                           bg_color=(240, 220, 240), text_color=(100, 50, 100))
    
    create_placeholder_image(640, 480, "Demo Video 2", 
                           "assets/videos/tactilevla_demo2.mp4", 
                           bg_color=(220, 240, 240), text_color=(50, 100, 100))
    
    create_placeholder_image(640, 480, "Demo Video 3", 
                           "assets/videos/tactilevla_demo3.mp4", 
                           bg_color=(240, 240, 220), text_color=(100, 100, 50))
    
    print("\nPlaceholder images created successfully!")
    print("Note: Video files are actually static images for preview purposes.")
    print("Replace them with actual videos when available.")

if __name__ == "__main__":
    main() 