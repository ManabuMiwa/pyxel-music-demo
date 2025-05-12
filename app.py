import pyxel
import songs.s00 as song

class App:
    def __init__(self):
        pyxel.init(256, 240)
        if hasattr(song, "channel_params"):
            self.init_channels()
        for index, mml in enumerate(song.mml_data):
            pyxel.sounds[index].mml(mml)
        pyxel.musics[0].set(*song.music)
        pyxel.run(self.update, self.draw)

    def init_channels(self):
        channels = []
        for gain, detune in song.channel_params:
            channel = pyxel.Channel()
            channel.gain = gain
            channel.detune = detune
            channels.append(channel)
        pyxel.channels.from_list(channels)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.play_pos(1) == None:
            pyxel.playm(0)

    def draw(self):
        pyxel.cls(1)
        pyxel.text(16, 100, song.title, 6)
        pyxel.text(16, 110, pyxel.play_pos(0).__repr__(), 7)
        pyxel.text(16, 130, "Press Q to quit", 7)

if __name__ == "__main__":
    App()
