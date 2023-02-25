from mutagen.mp3 import MP3
from PIL import Image
import imageio
from moviepy import editor
import os
import requests
import xmltodict
import json
import re

class PodcastMaker(object):
    def __init__(self):
        print("PodcastMaker initialized")
        self.image_path = os.path.join(os.getcwd(), "images")
        self.video_path = os.path.join(os.getcwd(), "videos")
        self.audio_path = os.path.join(os.getcwd(), "audio")
        
    def make(self, name, audio_path="audio.mp3", images_path="images"):
        try:
            audio_path = os.path.join(self.audio_path, audio_path)
            video_path = self.video_path
            images_path = self.image_path

            audio = MP3(audio_path)

            audio_length = audio.info.length

            list_of_images = []
            for image_file in os.listdir(images_path):
                if image_file.endswith('.png') or image_file.endswith('.jpg'):
                    image_path = os.path.join(
                        images_path,
                        image_file)
                    image = Image.open(image_path).resize(
                        (400, 400),
                        Image.ANTIALIAS
                        )
                    list_of_images.append(image)

            duration = audio_length/len(list_of_images)

            imageio.mimsave('images.gif', list_of_images, duration=1/duration)

            video = editor.VideoFileClip("images.gif")
            audio = editor.AudioFileClip(audio_path)
            final_video = video.set_audio(audio)
            os.chdir(video_path)
            final_video.write_videofile(fps=60, codec="libx264", filename=name+".mp4")
            # pdb.set_trace()
        except Exception as e:
            print(e)
            print(f"Error making video {audio_path}")
        
    def write_data(self, data, file_path):
        file_path = file_path.replace("?", "")
        file_path = os.path.join(os.getcwd(), file_path + ".json")
        with open(file_path, "w") as f:
            json.dump(data, f)
        return file_path
        
    def get_podcast_data(self, url="https://feeds.soundcloud.com/users/soundcloud:users:698218776/sounds.rss"):
        r = requests.get(url)
        with open("data.xml", "wb") as f:
            f.write(r.content)
        
        return xmltodict.parse(r.content)
        # return [{'title': '00 Trailer', 'link': 'https://soundcloud.com/microbinfie/trailer', 'duration': '00:00:51', 'summary': 'The Micro Binfie poscast is available at SoundCloud (https://soundcloud.com/microbinfie)\n\nor you can subscribe via iTunes: https://podcasts.apple.com/au/podcast/microbinfie-podcast/id1479852809\n\nor Spotify: https://podcasters.spotify.com/podcast/2zuzT8EVxbU0yOGFDVareK\n\nor your favourite podcast software.', 'enclosure': {'@url': 'https://feeds.soundcloud.com/stream/682433045-microbinfie-trailer.mp3'}}]
    
    def save_podcast(self, url, file_path=os.path.join(os.getcwd(), "audio.mp3")):
        file_path = file_path.replace("?", "")
        file_path = os.path.join(os.getcwd(), file_path + ".mp3")
        r = requests.get(url)
        print(url)
        with open(file_path, "wb") as f:
            f.write(r.content)
        return file_path
    
    def get_podcasts(self, data):
        podcasts = []
        for podcast in data["rss"]["channel"]["item"]:
            podcast_dict = {}
            for (key, value) in podcast.items():
                if key == "title":
                    podcast_dict["title"] = podcast["title"].replace(":", " -")
                    podcast_dict["title"] = podcast["title"].replace("?", "")
                    podcast_dict["title"] = value
                elif key == "link":
                    podcast_dict["link"] = value
                elif key == "itunes:duration":
                    podcast_dict["duration"] = value
                elif key == "itunes:summary":
                    podcast_dict["summary"] = value
                elif key == "enclosure":
                    podcast_dict["source"] = value["@url"]
            podcasts.append(podcast_dict)
        return podcasts
    
    def save_all_podcasts(self, data, path="audio"):
        os.chdir(path)
        for podcast in self.get_podcasts(data):
            self.save_podcast(podcast["source"], podcast["title"])
            self.write_data(podcast, podcast["title"])
            print(f"Saved {podcast['title']}")
        os.chdir("..")
        return [os.path.join(os.getcwd(), path, i["title"] + ".mp3") for i in self.get_podcasts(data)]
    
    def make_all_podcasts(self, paths):
        for path in paths:
            try:
                title = path.split("\\")[-1].split(".")[0]
                self.make(f"{title}", path, self.image_path)
            except Exception as e:
                print(e)
                print(f"Error making video {path}")
            
if __name__ == "__main__":
    if (a:=input("Type: 'make', 'descriptions'\n")) == "make":
        pm = PodcastMaker()
        # data = pm.get_podcast_data()
        # paths = pm.save_all_podcasts(data)
        paths = [i if i.endswith(".mp3") else None for i in os.listdir("C:\\Users\\peque\\OneDrive\\Documents\\GitHub\\python-scripts\\podcasts\\tests\\audio")]
        for path in paths:
            if path is None:
                paths.remove(path)
        pm.make_all_podcasts(paths)
        print("Done!")
    elif a == "descriptions":
        pm = PodcastMaker()
        data = pm.get_podcast_data()
        for podcast in pm.get_podcasts(data):
            """Needs to clear URLs from description ('summary') and print them to a file"""
            description = podcast["summary"]
            description = re.sub(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", "LINK", description)
            
            with open("descriptions.txt", "a") as f:
                try:
                    f.write(f"{podcast['title']}: {description}\n")
                except Exception as e:
                    print(e)
                    print(f"Error writing description of {podcast['title']}: {description}")
            print(f"{podcast['title']}: {description}")