"""
Problem Statement:
Create a base class Media with a method play().
Derive Audio, Video, and Podcast.
Override play() according to the media type.
"""

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


media = [Audio(), Video(), Podcast()]

for item in media:
    item.play()