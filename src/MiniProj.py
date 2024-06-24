import speech_recognition as sr

# Function to recognize speech using SpeechRecognition library
def recognize_speech():
    recognizer = sr.Recognizer()
    # Adjust for ambient noise
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)
        
    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)  
        # Convert to lowercase for case-insensitive comparison
        return text.lower()  
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

# Main function for authentication
def authenticate():
    # Recognize speech
    print("Please say the password:")
    user_input = recognize_speech()
    if user_input is None:
        return
    
    print("You said: "+user_input)
    # Check if the recognized password matches the required password
    required_password = "hello"
    if user_input == required_password:
        print("Authentication successful!")
        key=0
        while key!=3:
            key=int(input("\nWelcome\n1.Change Password\n2.Test Password\n3.Logout\n"))
            
            if key==1:
                print("Please say the new password:")
                required_password=recognize_speech()
                print("Password Reset Successful\nNew Password: "+required_password)
            
            elif key==2:
                print("Please say the password:")
                user_input=recognize_speech()
                if user_input == required_password:
                    print("You said: "+user_input)
                    print("Password Verified")
                else:
                    print("You said: "+user_input)
                    print("Password Not Verified")

            else:
                break

    else:
        print("Authentication failed. Incorrect password.")

# Call the authentication function
authenticate()
