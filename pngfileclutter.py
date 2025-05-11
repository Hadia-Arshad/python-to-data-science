import os

folder = r'C:\Users\taj\Arshad'  # Change this to your folder
count = 1

for file in os.listdir(folder):
    if file.endswith('.png'):
        old_path = os.path.join(folder, file)
        new_name = f"{count}.png"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")
        count += 1
