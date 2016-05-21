'''
MIT License Copyright(c) 2016 Balys Valentukevicius

Configuration for Twitter client and Haiku generator
'''

import os

class Config(object):
    def __init__(self):
        # Twitter
        self.twitter_consumer_key="xxxxxxxx"
        self.twitter_consumer_secret="xxxxxxxx"
        self.twitter_access_token_key="xxxxxxxx"
        self.twitter_access_token_secret="xxxxxxxx"

        # Markovify
        self.markovify_input_dir = "./input/"
        self.markovify_max_overlap_total = 25
        self.markovify_max_overlap_ratio = 0.8

        # Haiku
        self.haiku_avg_char_per_syl = 6
        self.haiku_first_syl_count = 5
        self.haiku_second_syl_count = 7
        self.haiku_third_syl_count = 5

        self.generation_frequency = 60 * 60 * 4
