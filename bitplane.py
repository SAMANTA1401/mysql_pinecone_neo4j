import numpy as np

def bit_planes(image):
  """
  Computes the bit planes of an 8-bit image.

  Args:
    image: A NumPy array representing the image data.

  Returns:
    A list of NumPy arrays, where each element represents a bit plane of the image.
  """

  bit_planes = []
  for i in range(8):
    mask = 1 << (7 - i)  # Create a mask with the ith bit set to 1
    bit_plane = (image & mask) // mask  # Extract the ith bit plane
    bit_planes.append(bit_plane)
  return bit_planes

# Define the image data
image_data = np.array([
    50, 80, 100, 150, 20, 75, 200, 250,
    90, 125, 155, 255, 175, 210, 230, 110
])

# Compute and print the bit planes
bit_planes = bit_planes(image_data)
for i, plane in enumerate(bit_planes):
  print(f"Bit plane {i+1}:")
  print(plane)



# rgb 
# Define the coordinates of warm white and deep blue
warm_white = (0.55, 0.3)
deep_blue = (0.25, 0.15)

# Calculate the difference between the coordinates
diff_x = warm_white[0] - deep_blue[0]
diff_y = warm_white[1] - deep_blue[1]

# Calculate the vector length (magnitude)
vector_length = (diff_x**2 + diff_y**2)**0.5

# Normalize the vector to get unit vector
unit_vector = (diff_x / vector_length, diff_y / vector_length)

# Assume the starting point is the origin (0, 0)
origin = (0, 0)

# Calculate the coordinates of a point on the line segment between warm white and deep blue
point_on_line = (origin[0] + unit_vector[0], origin[1] + unit_vector[1])

# Calculate the percentage of red, green, and blue for the point on the line segment
# Assuming the color space is CIE 1931 XYZ, where X + Y + Z = 1
x = point_on_line[0]
y = point_on_line[1]
z = 1 - x - y

# Convert the percentages to a string with two decimal places
red_percentage = f"{x * 100:.2f}%"
green_percentage = f"{y * 100:.2f}%"
blue_percentage = f"{z * 100:.2f}%"

# Print the results
print(f"Red: {red_percentage}")
print(f"Green: {green_percentage}")
print(f"Blue: {blue_percentage}")