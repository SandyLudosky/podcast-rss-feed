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

        for item in podcast_feed.entries[0].links:

            if (item['type'] == 'audio/mpeg'):
                print("The episode URL is ", item.href)
                return {
                    "url": item.href,
                    "duration": podcast_feed.entries[0].itunes_duration,
                    "title": podcast_feed.entries[0].title,
                    "description": podcast_feed.entries[0].description,
                    "author": podcast_feed.entries[0].author,
                    "date": podcast_feed.entries[0].published,
                    "type": podcast_feed.entries[0],
                    "image": podcast_feed.entries[0].image.href,
                }


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

    # Delete all files in the current directory that start with "chunk" and
    # end with ".wav"
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


# file_path = "audio.mp3"

def runAPI(rss_url):
    item = get_podcast(rss_url)
    file_path = downloadFile(item)
    transcript = transcribe(file_path)
    summary = summarize(transcript)
    return {"summary": summary, "item": item}


def run():
    rss = input("Enter the RSS feed URL:")
    item = get_podcast(rss)
    file_path = downloadFile(item)
    transcript = transcribe(file_path)
    summary = summarize(transcript)
    return {"summary": summary, "item": item}

# uncomment the following line to run the script
# run()
