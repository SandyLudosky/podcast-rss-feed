import pathlib
import feedparser
import requests
import openai

from pydub import AudioSegment
from pydub.silence import split_on_silence
import ssl

import utils

def get_podcast(rss):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
        podcast_feed = feedparser.parse(rss)
        print("The number of podcast entries is ", len(podcast_feed.entries))
        title = podcast_feed.entries[0].title
        for item in podcast_feed.entries[0].links:
            if (item['type'] == 'audio/mpeg'):
                print("The episode URL is ", item.href)
                return {"url": item.href, "title": title}


def downloadFile(item):
    r = requests.get(item["url"], allow_redirects=True)
    open("media/" + item["title"] + ".mp3", 'wb').write(r.content)


def transcribe(file_path):
    # Chunk up the audio file
    sound_file = AudioSegment.from_mp3(file_path)
    audio_chunks = split_on_silence(
        sound_file, min_silence_len=1000, silence_thresh=-40)
    count = len(audio_chunks)
    print("Audio split into " + str(count) + " audio chunks \n")

    # Divide the audio chunks into smaller chunks and transcribe
    transcript = utils.divide_in_chunks(audio_chunks)
    # Delete all files in the current directory that start with "chunk" and end with ".wav"
    utils.delete_chunks(count)

    return transcript


def run():
    # rss = input("Enter the RSS feed URL:")
    # item = get_podcast(rss)
    # downloadFile(item)
    # transcript = transcribe("media/" + item["title"] + ".mp3")
    # print(transcript)
    # return transcript
    transcript = transcribe("media/audio.mp3")
    return transcript


