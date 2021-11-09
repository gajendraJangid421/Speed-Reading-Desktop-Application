
import speech_recognition as s

sr = s.Recognizer()

print('Start reading')

with s.Microphone() as m:
    audio = sr.listen(m)
    query = sr.recognize_google(audio, language='eng-in')
    print(query)

# f = open("read.txt","r")
# count = 0
# for line in f:
#     words = line.split(" ")
#     count += len(words)
# f.close()
# print(count)
