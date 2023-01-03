import requests
import getting_lyrics


def asking_user():
    print('welcome to paraphrasing text.')
    print('Would you like to paraphrase poem or song?')
    genre = str(input('Press p for poem or s for song '))
    title = str(input('Now enter the title: '))
    # author = str(input('now enter the author: '))
    if genre == 's':
        text = requests.get('')
    if genre == 'p':
        text = getting_lyrics.verses(title)
    print('here is your original text')
    print(text)
    # percentage = int(input('enter the percentage of the text you want it to be paraphrased: '))


print(asking_user())
