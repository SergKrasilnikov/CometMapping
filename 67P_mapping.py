from PIL import Image, ImageDraw
import pandas as pd

# Step 1: Load the map image
map_image_path = 'path/to/your/map_image.jpg'
map_image = Image.open(map_image_path)

# Step 2: Read the Excel file
excel_file_path = 'path/to/your/excel_file.xlsx'
df = pd.read_excel(excel_file_path)

# Step 3: Plot coordinates on the image
draw = ImageDraw.Draw(map_image)
for index, row in df.iterrows():
    longitude = row['Longitude']  # Assuming 'Longitude' is the column name in Excel
    latitude = row['Latitude']  # Assuming 'Latitude' is the column name in Excel

    # Calculate pixel positions on the map based on longitude and latitude
    # You'll need to define a function to map from coordinates to pixel positions
    # Example (assuming a linear mapping for demonstration purposes):
    x = (longitude + 180) * (map_image.width / 360)
    y = (90 - latitude) * (map_image.height / 180)

    # Draw a point or marker at (x, y) on the map image
    draw.ellipse([(x - 2, y - 2), (x + 2, y + 2)], fill='red', outline='red')  # Example: small red circles

# Step 4: Save the modified image
modified_image_path = 'path/to/save/modified_map_image.jpg'
map_image.save(modified_image_path)

print(f"Modified map image saved at: {modified_image_path}")
