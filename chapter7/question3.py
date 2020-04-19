import unittest
from typing import List
import time
import sys
import io
from contextlib import redirect_stdout
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Wallet:
    def __init__(self, credit: int = 0):
        self.creadit = credit

    def pay(self, value):
        if value > self.creadit:
            return ValueError()
        else:
            self.creadit -= value
            return value


class Person:
    def __init__(self, wallet: Wallet):
        self.wallet = wallet

    def pay(self, target):
        return target.receipt(self.wallet.pay(target.credit_value))


class Customer(Person):
    pass


class Music:
    def __init__(self, title: str, url=""):
        self.title = title
        self.url = url


class Playlist:
    def __init__(self, musics: List[Music] = []):
        self.musics = musics

    def __str__(self):
        return "\n".join(f"{i}) {music.title}" for i, music in enumerate(self.musics))

    def get_music(self, key):
        return self.musics[key]


class JukeBox:
    credit_value: int = 1

    def __init__(self, play_list: Playlist):
        self.play_list = play_list
        self.gain = 0
        self.driver = None
        self.playing = False

    @property
    def now_playing(self):
        if not self.driver:
            return False

        try:
            self.driver.find_element_by_class_name("playing-mode")
        except NoSuchElementException:
            return False
        else:
            return True

        return False

    def receipt(self, credit_value):
        self.gain += self.credit_value
        return self.play_list

    def play(self, music: Music):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(music.url)

        try:
            WebDriverWait(self.driver, 15).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "html5-video-container")
                )
            )
        except TimeoutException as e:
            raise e
        else:
            self.playing = True

    def stop_play(self):
        if self.driver:
            self.driver.close()
            self.playing = False


class JukeBoxSession:
    def __init__(self, customer: Customer, jukebox: JukeBox):
        self.customer = customer
        self.jukebox = jukebox

    def ask_paying(self):
        while True:
            print(
                f"Welcome to jukebox. Please insert {self.jukebox.credit_value} credit.",
                f"Credit in your wallet: {self.customer.wallet.creadit}",
                sep="\n",
                end="\n\n",
            )
            print(
                f"1) Insert {self.jukebox.credit_value} for credit",
                f"2) Exit.",
                sep="\n",
                end="\n\n",
            )
            stdin = input("Please input number: ")
            if stdin == "1":
                return True
            elif stdin == "2":
                return False
            else:
                print("Command is Invalid.")

    def select_music(self):
        play_list = self.jukebox.play_list
        print(
            "Playlist is here. Please select music for play.",
            play_list,
            sep="\n\n",
            end="\n\n",
        )
        music_key = int(input("Please input music number: "))
        return play_list.get_music(music_key)

    def play_music(self, music):
        self.jukebox.play(music)
        print(f"now playing : {music.title}")

        while self.jukebox.now_playing:
            time.sleep(1)

        self.jukebox.stop_play()

    def thanks(self):
        print("thank you for using this jukebox!")

    def end(self):
        print("Bye Bye ...")
        exit()


class TestJukeBox(unittest.TestCase):
    def setUp(self):
        self.jukebox = JukeBox()
        self.play_list = Playlist()
        self.play_list.musics = [Music("Sample Music", "sample_url")]
        self.jukebox.music_menu = self.play_list
        self.customer = Customer(wallet=Wallet(credit=2))

    def test_it(self):
        play_list = self.customer.pay(self.jukebox)
        assert play_list == self.play_list


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.play_list = Playlist()
        self.play_list.musics = [Music("Sample Music")]

    def test_str(self):
        assert str(self.play_list) == "0) Sample Music"


def main():
    play_list = Playlist(
        musics=[
            Music(
                title="亡き王女の為のセプテット", url="https://www.youtube.com/watch?v=3mKStUbmZ_w",
            ),
            Music(
                title="幽雅に咲かせ、墨染の桜 ～Border of Life",
                url="https://www.youtube.com/watch?v=PWs5pm0zy6k",
            ),
            Music(
                title="竹取飛翔　～ Lunatic Princess",
                url="https://www.youtube.com/watch?v=r0M4bSkD_zY",
            ),
            Music(
                title="六十年目の東方裁判～Fate of Sixty Years",
                url="https://www.youtube.com/watch?v=zlT4XgiH4gM",
            ),
            Music(
                title="神さびた古戦場～Suwa Foughten Field",
                url="https://www.youtube.com/watch?v=lLWgwq-iMyM",
            ),
            Music(
                title="霊知の太陽信仰　～ Nuclear Fusion ～",
                url="https://www.youtube.com/watch?v=cUzZwl9vq8Y",
            ),
        ]
    )
    jukebox = JukeBox(play_list=play_list)
    customer = Customer(wallet=Wallet(credit=1000))
    session = JukeBoxSession(customer=customer, jukebox=jukebox)


    paying = session.ask_paying()
    print("\n")

    if not paying:
        session.end()

    music = session.select_music()
    print("\n")

    session.play_music(music)
    print("\n")

    session.thanks()


if __name__ == "__main__":
    main()
    # unittest.main()
