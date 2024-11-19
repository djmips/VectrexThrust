import math

magnitude = 127
num_vectors = 32
angle_step = -math.tau / num_vectors

vectors = []
for i in range(num_vectors):
    angle = i * angle_step
    x = int(magnitude * math.cos(angle))
    y = int(magnitude * math.sin(angle))
    vectors.append((x, y))

# Print in a format similar to your assembly table
for i in range(0, len(vectors), 8):  # 8 pairs per line
    line = " ".join(f"{x},{y}," for x, y in vectors[i:i+8]).rstrip(',')
    print(f" db {line}")

