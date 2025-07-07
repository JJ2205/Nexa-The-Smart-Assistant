import text_to_speech
import speech_to_text
import speech_recognition
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if user_data:  # Ensure user_data is not None
        if "what is your name" in user_data:
            text_to_speech.text_to_speech("My name is NEXA AI!")
            return "My name is NEXA AI"
        elif "hello" in user_data or "hi" in user_data:
            text_to_speech.text_to_speech("Heyy, How can I help?")
            return "Heyy, How can I help?"

        elif "good morning" in user_data:
            text_to_speech.text_to_speech("Good morning my pumpkin, how you doing?")
            return "Good morning my pumpkin, how you doing?"

        elif "what is the time now?" in user_data:
            current_time = datetime.datetime.now()
            Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
            text_to_speech.text_to_speech(Time)
            return Time

        elif "shutdown" or "close" in user_data:
            text_to_speech.text_to_speech("Ok sir")
            return "Ok sir"

        elif "play music" in user_data:
            webbrowser.open("https://open.spotify.com/track/2fPU00ra07r08w5xM7NkRx?uid=b3dfceee27585cbd4823&uri=spotify:track:2fPU00ra07r08w5xM7NkRx")
            text_to_speech.text_to_speech("Enjoy sir")

        elif "open google" in user_data:
            webbrowser.open("https://www.google.com/")
            text_to_speech.text_to_speech("Opening Google")

        elif "open youtube" in user_data:
            webbrowser.open("https://www.youtube.com/")
            text_to_speech.text_to_speech("Opening Youtube")

        elif "weather" in user_data:
            ans=weather.weather()
            text_to_speech.text_to_speech(ans)
            return ans
        
        elif "hey nexa what do you know about rohith krishna" in user_data:
            text_to_speech.text_to_speech("Rohith Krishna is the sexiest boy of all time. Even as an ai i feel sexual attraction towards him")
            return "Rohith Krishna is the sexiest boy of all time. Even as an ai i feel sexual attraction towards him"
        else:
            text_to_speech.text_to_speech("sorry, not able to understand")
            return "Sorry, not able to understand"
    else:
        text_to_speech.text_to_speech("I didn't hear anything, please try again.")
        return "I didn't hear anything, please try again."
