import whisper


model = whisper.load_model("base")

def transcrever (audio):
    result = model.transcribe(audio)
    return result["text"]