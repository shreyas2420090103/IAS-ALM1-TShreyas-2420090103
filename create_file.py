import os

text = "This is a sample 10 KB text file for SDES encryption and server client file transfer. "

target_size = 10 * 1024  # 10 KB

with open("files/server_10kb.txt", "w") as f:
    while f.tell() < target_size:
        f.write(text)

size = os.path.getsize("files/server_10kb.txt")

print("10 KB text file created successfully.")
print("File size:", size, "bytes")
print("File size in KB:", size / 1024)
