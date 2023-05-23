from ursina import Audio, Ursina

app = Ursina(broderless=False)

audio = Audio('explosion.wav')

def input(key):
    if key == 'space':
        audio.play()


app.run()
