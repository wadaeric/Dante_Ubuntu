# Dante_Ubuntu
Proyecto dante asistente para GNU/Linux, en concreto la distribución de Ubuntu 20.04 64bits

# Dependencias
pip install pyttsx3

pip install SpeechRecognition

pip install pywhatkit 

Luego, en la consola de GNU/Linux:

sudo apt install python3-tk python3-dev


# Instalar PyAudio en GNU/Linux
sudo apt install libasound-dev

Descargamos el archivo portaudio desde: http://sources.buildroot.net/portaudio/pa_stable_v190700_20210406.tgz


Descomprimimos el archivo con el comando:
tar -zxvf

acdedemos al directorio creado y ejecutamos:
./configure && make

sudo make install

y por ultimo:
pip install pyaudio
