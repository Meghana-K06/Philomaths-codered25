import pyttsx3

def read_text_file_aloud(file_path):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        # Open the text file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Speak the content
        engine.say(content)
        engine.runAndWait()
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your text file
file_path = "C:\\Users\\megha\\OneDrive\\Desktop\\code red\\OSR\\extracted_text.txt"  # Replace with your file path
read_text_file_aloud(file_path)
