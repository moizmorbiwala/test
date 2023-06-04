import streamlit as st
import speech_recognition as sr
import pyperclip

def transcribe_audio(language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak into your microphone...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=language)
            st.write("Transcription:")
            st.write(text)
            st.button("Copy Transcription", on_click=copy_to_clipboard, args=(text,))
        except sr.UnknownValueError:
            st.write("Unable to transcribe the audio.")
        except sr.RequestError:
            st.write("Error occurred during transcription. Please try again.")

def copy_to_clipboard(text):
    pyperclip.copy(text)
    st.write("Transcription copied to clipboard!")

def main():
    st.title("Real-Time Voice Transcription App")
    st.write("Click the 'Start Transcription' button and speak into your microphone.")
    
    language = st.selectbox("Select Language", ("English", "Spanish", "French"))

    transcript_button = st.button("Start Transcription")
    stop_button = st.button("Stop Transcription")

    if transcript_button:
        if language == "English":
            transcribe_audio("en-US")
        elif language == "Spanish":
            transcribe_audio("es-ES")
        elif language == "French":
            transcribe_audio("fr-FR")
    elif stop_button:
        st.write("Transcription stopped.")

    st.empty()  # Add an empty space

if __name__ == '__main__':
    main()
