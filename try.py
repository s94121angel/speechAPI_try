
import azure.cognitiveservices.speech as speechsdk
import time

import csv


def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription="a037fe6923d54e8c8e3c11070aaa5620", region="eastus")
    speech_config.speech_recognition_language="zh-tw"
    
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    i=0
    list = []
    while i<101:
        print("請說出第"+str(i)+"筆指令")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        start = time.time()
        
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
        i+=1
        end = time.time()
        print (end - start)
        resault = end - start
        list.append(resault)
    print(list)
    with open('GFG.csv', 'w') as f:
        write = csv.writer(f)
        
        write.writerow(list)
recognize_from_microphone()