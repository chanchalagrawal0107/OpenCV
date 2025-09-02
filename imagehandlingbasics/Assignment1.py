import cv2
filename = input("Enter the filename(with extension): ")
image = cv2.imread(filename)

if image is not None:
    print("Image loaded successfully")

    while True:
        print("What do you want to do with the image?\n")
        print("1. View dimensions\n")
        print("2. convert to gray scale and display\n")
        print("3. Convert to grayscale and save\n")
        print("4. Save aisehi\n")
        print("5. Exit\n")

        choice = input("Enter the choice from (1-4): ")

        if choice == "1":
            h, w, c = image.shape
            print(f"Image loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")

        elif choice == "2":
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            cv2.imshow("Gray image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif choice == "3":
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            save_name = input("Enter the filename to save with alongwith the extension: ")
            cv2.imwrite(save_name, gray)
            print(f"Gray scale image saved as: {save_name}")

        elif choice == "4":
            save_name = input("Enter the name with which you wish to save the image with the extension: ")
            cv2.imwrite(save_name, image)
            print(f"image saved as: {save_name}")

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice")

else:
    print("Image not loaded")

