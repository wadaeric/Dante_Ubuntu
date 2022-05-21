from curses import keyname
import pyttsx3
import speech_recognition as sr


# Voz del asistente
class SpeechModule:
    def __init__(self):
        
        # controlador para el sistema operativo linux:
        self.engine = pyttsx3.init()

        # Establecemos la velocidad del habla en 125
        self.engine.setProperty('rate', 125)

        # Establecemos el volumen que va desde 0.0 a 1.0 en booleano
        self.engine.setProperty('volume', 1.0)

        # Cargamos la voces disponibles
        voices = self.engine.getProperty('voices')

        # Y asignamos la numero 0
        self.engine.setProperty('voice', voices[0].id)

    # Definimos la funciona para hablar, a la cual
    # le pasaremos un texto
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

class VoiceRecognitionModule:
    def __init__(self, key=None):
        
        # En caso de ser software comercial se tiene que pagar una key
        self.key = key
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            # El audio sera lo que se escuche por el microfono
            audio = self.r.listen(source)

            try:
                # se le pasa el audio al sistema de reconocimiento de google en idioma español
                text = self.r.recognize_google(audio,key=self.key, language="Es-es")
                # y se devuelve lo que este haya entendido en formato de texto
                print(text)
                return text
            except:
                siento = "Lo siento no he entendido, puedes repetir"
                return siento
