
import pathlib
import whisper

model = whisper.load_model("base")


def divide_in_chunks(audio_chunks):
    transcript = ""
    count = len(audio_chunks)
    print("Audio split into " + str(count) + " audio chunks \n")
    c = 0
    for i, chunk in enumerate(audio_chunks):
        # If you have a long audio file, you can enable this to only run for a subset of chunks
        if i < 10 or i > count - 10:
            out_file = "chunk{0}.wav".format(c)
            print("\r\nExporting >>", out_file, " - ", i, "/", count)
            chunk.export(out_file, format="wav")
            result = model.transcribe(out_file)
            transcriptChunk = result["text"]
            print(transcriptChunk)
            c = c + 1
            # Append transcript in memory if you have sufficient memory
            transcript += " " + transcriptChunk
    return transcript


def delete_chunks(count):
    print("Deleting chunks")
    for i in range(count):
        file_name = f"chunk0{i}.wav"
        file_name = f"chunk{i}.wav"
        if pathlib.Path(file_name).exists():
            file_path = pathlib.Path(file_name)
            file_path.unlink()
