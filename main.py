import os
import pyfirmata
import speech_recognition as sr

command = 'clear'
if (os.name in ['nt', 'dos']):
    command = 'cls'
os.system(command)
    

r = sr.Recognizer()
mic = sr.Microphone()
board = pyfirmata.Arduino("COM3") # Arduino kartınızın portunu yazın. Örneğin, COM3 veya /dev/ttyACM0.

while True:
    print("Dinliyorum...")
    with mic as source:
        audio = r.listen(source)
        try:
            deger = r.recognize_google(audio, language='tr-TR')
            print(f"Cevap: {deger}")
            words = deger.split()
            if words[0].lower() in ["pin", "led"]:
                if words[2].lower() in ["aç", "ac", "yuksek", "yüksek"]:
                    board.digital[int(words[1])].write(1)
                elif words[2].lower() in ["kapat", "kapa", "dusuk", "düşük"]:
                    board.digital[int(words[1])].write(0)
                else:
                    print(f"Anlaşılamadı: {deger}")
            else:
                print(f"Anlaşılamadı: {deger}")
        except sr.UnknownValueError:
            print("Tekrar deneniyor...")
        except Exception as e:
            print(f"Anlaşılamadı: {deger}")
    print()