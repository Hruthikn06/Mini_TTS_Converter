import pyttsx3
import os


def set_speech_properties(engine):
    voices = engine.getProperty('voices')
    print("Select voice: 0 = Male, 1 = Female")
    voice_choice = input("Enter choice (0/1): ")
    if voice_choice in ["0", "1"]:
        engine.setProperty('voice', voices[int(voice_choice)].id)
    rate = input("Enter speech rate (default 200): ")
    if rate.isdigit():
        engine.setProperty('rate', int(rate))
    volume = input("Enter volume (0.0 to 1.0, default 1.0): ")
    try:
        vol = float(volume)
        if 0 <= vol <= 1:
            engine.setProperty('volume', vol)
    except:
        pass

def text_to_speech(text, engine):
    save_option = input("Do you want to save the audio? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter filename (without extension): ")
        engine.save_to_file(text, f"{filename}.mp3")
        engine.runAndWait()
        print(f"Audio saved as {filename}.mp3")
        os.system(f"start {filename}.mp3")
    else:
        engine.say(text)
        engine.runAndWait()
    engine.stop()

engine = pyttsx3.init()

while True:
    print("\nMini TTS Converter")
    print("1. Set speech properties")
    print("2. Enter text to speak")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        set_speech_properties(engine)
    elif choice == "2":
        text_input = input("Enter text: ")
        temp_engine = pyttsx3.init()
        temp_engine.setProperty('voice', engine.getProperty('voice'))
        temp_engine.setProperty('rate', engine.getProperty('rate'))
        temp_engine.setProperty('volume', engine.getProperty('volume'))
        text_to_speech(text_input, temp_engine)
    elif choice == "3":
        print("Exiting Mini TTS Converter. Goodbye!")
        engine.stop()
        break
    else:
        print("Invalid choice. Try again.")
