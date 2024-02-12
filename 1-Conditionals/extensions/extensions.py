#  extensions .gif .jpg .jpeg .png .pdf .txt .zip

y = input("Name of a file: ")
y = y.lower()

if y.endswith(".gif"):
    print("image/gif")

elif y.endswith(".jpg"):
    print("image/jpg")

elif y.endswith(".jpeg"):
    print("image/jpeg")

elif y.endswith(".png"):
    print("image/png")

elif y.endswith(".pdf"):
    print("application/pdf")

elif y.endswith(".txt"):
    print("application/txt")

elif y.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")
