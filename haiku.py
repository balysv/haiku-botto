'''
MIT License Copyright(c) 2016 Balys Valentukevicius

Generates haiku and post them to Twitter. See self.config.py
for self.configuration options.
'''

import config
import markovify
import twitter
import sylco
import threading
import os
from random import randint

class HaikuBotto(object):
    def __init__(self):
        self.config = config.Config()
        self.api = twitter.Api(
            consumer_key=self.config.twitter_consumer_key,
            consumer_secret=self.config.twitter_consumer_secret,
            access_token_key=self.config.twitter_access_token_key,
            access_token_secret=self.config.twitter_access_token_secret
        )

    '''
    Begin looping haiku generation and Twitter posts
    '''
    def start(self):
        haiku = self.generate_haiku()
        # self.api.PostUpdate(haiku)
        threading.Timer(self.config.generation_frequency, self.start).start()

    '''
    1. Create a Markovify text model from all inputs
    2. Generate a random text snippet using markov chains
    3. Proceed if syllable count is correct, otherwise go to (2)
    4. Concat all haiku lines
    '''
    def generate_haiku(self):

        all_text = "";
        for i in os.listdir(self.config.markovify_input_dir):
            with open(self.config.markovify_input_dir + i) as f:
                all_text += f.read()
        text_model = markovify.Text(all_text)

        print("looking for first...")
        first = None
        while first == None or sylco.getsyls(first) != self.config.haiku_first_syl_count:
            first = text_model.make_short_sentence(
                self.config.haiku_first_syl_count * self.config.haiku_avg_char_per_syl,
                tries=100,
                max_overlap_ratio=self.config.markovify_max_overlap_ratio,
                max_overlap_total=self.config.markovify_max_overlap_total
            )

        print("looking for second...")
        second = None
        while second == None or sylco.getsyls(second) != self.config.haiku_second_syl_count:
            second = text_model.make_short_sentence(
                self.config.haiku_second_syl_count * self.config.haiku_avg_char_per_syl,
                tries=100,
                max_overlap_ratio=self.config.markovify_max_overlap_ratio,
                max_overlap_total=self.config.markovify_max_overlap_total
            )

        print("looking for third...")
        third = None
        while third == None or third == first or sylco.getsyls(third) != self.config.haiku_third_syl_count:
            third = text_model.make_short_sentence(
                self.config.haiku_third_syl_count * self.config.haiku_avg_char_per_syl,
                tries=100,
                max_overlap_ratio=self.config.markovify_max_overlap_ratio,
                max_overlap_total=self.config.markovify_max_overlap_total
            )

        haiku = ''.join([
            first.replace(".", ""), "\n",
            second.replace(".", ""), "\n",
            third.replace(".", "")
        ])

        print("")
        print("***********************")
        print("-----------------------")
        print(haiku)
        print("-----------------------")
        print("***********************")

        return haiku
