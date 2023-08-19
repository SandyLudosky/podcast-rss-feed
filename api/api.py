import feedparser
import requests
import openai
import os

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
    episode_name = "_".join(item["title"].split(
        " ")).lower().replace(":", "").replace("‘", "").replace("’", "").replace(",", "") + ".mp3"

    open("media/" + episode_name, 'wb').write(r.content)
    print("file " + episode_name + " downloaded at media/")
    return episode_name


def transcribe(file_path):
    # Chunk up the audio file
    print("transcribing " + file_path)
    sound_file = AudioSegment.from_mp3("media/audio.mp3")
    audio_chunks = split_on_silence(
        sound_file, min_silence_len=1000, silence_thresh=-40)
    count = len(audio_chunks)
    print("Audio split into " + str(count) + " audio chunks \n")

    # Divide the audio chunks into smaller chunks and transcribe
    transcript = utils.divide_in_chunks(audio_chunks)
    # Delete all files in the current directory that start with "chunk" and end with ".wav"
    utils.delete_chunks(count)
    return transcript


def summarize(transcript):
    print("summarizing transcript")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professionnal writer"},
            {"role": "user", "content": "summarize the following text:" + transcript},
        ]
    )

    return completion.choices[0].message.content


def run(rss_url):
    # rss = input("Enter the RSS feed URL:")
    # item = get_podcast(rss_url)
    # file_path = downloadFile(item)
    file_path = "audio.mp3"
    transcript = transcribe("media/" + file_path)
    summary = summarize(transcript)
    return summary
    # transcript = transcribe("media/audio.mp3")
    # return transcript
