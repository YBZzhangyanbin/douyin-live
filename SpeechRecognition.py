
import speech_recognition as sr
if __name__ == '__main__':
    recognizer = sr.Recognizer()
    # 用于存储识别结果的文本
    with sr.AudioFile('/Users/zhangyanbin/Documents/douyin/douyin-live/并购风云.wav') as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='zh-CN')
            print(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")