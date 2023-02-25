import xmltodict
import requests

def get_podcast_data(url="https://feeds.soundcloud.com/users/soundcloud:users:698218776/sounds.rss"):
    r = requests.get(url)
    with open("data.xml", "wb") as f:
        f.write(r.content)
    
    return xmltodict.parse(r.content)

# def get_keys(dictionary):
#     if dictionary is None:
#         return None
#     keys = []
#     for (key, value) in dictionary.items():
#         keys.append(key)
#         if isinstance(value, dict):
#             if not (a:=get_keys(value)) is None:
#                 keys.extend(a)
#         # elif isinstance(value, list):
#         #     for item in value:
#         #         if not (a:=get_keys(item)) is None:
#         #             keys.extend(a)
#     return keys

# '@href', 'guid', '@isPermaLink', '#text', 'title', 'pubDate', 'link', 'itunes:duration', 'itunes:author', 'itunes:explicit', 'itunes:summary', 'itunes:subtitle', 'description', 'enclosure', '@type', '@url', '@length', 'itunes:image'
# print(get_podcast_data()["rss"]["channel"].keys())

# def get_podcasts(data):
#     podcasts = []
#     for podcast in data["rss"]["channel"]["item"]:
#         podcast_dict = {}
#         for (key, value) in podcast.items():
#             if key == "title":
#                 podcast_dict["title"] = value
#             elif key == "link":
#                 podcast_dict["link"] = value
#             elif key == "itunes:duration":
#                 podcast_dict["duration"] = value
#             elif key == "itunes:summary":
#                 podcast_dict["summary"] = value
#             elif key == "enclosure":
#                 podcast_dict["source"] = value["@url"]
#         podcasts.append(podcast_dict)
#     return podcasts

# print(get_keys(get_podcast_data()))
podcast_1 = get_podcast_data()["rss"]["channel"]["item"][0]
print(podcast_1)