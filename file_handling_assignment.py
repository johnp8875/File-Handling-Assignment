try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is John Ugbaje Pius. My Contact Number is\n")
        file.write("0556843198\n")
        file.write("It has been an excellent journey on PLP so far.\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("This is the beginning of greater things to come. Soonest I will be earning a monthly minimum of \n")
        file.write("2000\n")
        file.write("I can't wait for it to happen\n")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("Task completed.")