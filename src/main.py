from instapy import InstaPy
from instapy import smart_run

from dotenv import load_dotenv

from datetime import date

import random
import os

load_dotenv()

username = os.getenv("INSTA_USERNAME")
password = os.getenv("INSTA_PASSWORD")

comments = [
    u'⚡️🗡⚡️',
    u'⚡️🤙🏼⚡️',
    u'⚡️🏄⚡️',
]

hashtags = [
    'surf', 'surfing', 'surfer', 'surfboard'
]

session = InstaPy(
    username=username,
    password=password,
    headless_browser=True
)

with smart_run(session):
    session.set_relationship_bounds(
        enabled=True,
        potency_ratio=None,
        delimit_by_numbers=True,
        max_followers=5000,
        min_followers=50,
        min_posts=10
    )
    session.set_user_interact(
        amount=5,
        randomize=True,
        percentage=50
    )
    session.interact_user_followers(
        [
            'ride_list',
            'metal_jimmy',
            'kellyslater',
            'froghouse',
        ],
        amount=10,
        randomize=True
    )
    session.set_do_comment(enabled=True,  percentage=50)
    session.set_comments(comments)
    session.like_by_tags(hashtags, amount=25)
    session.follow_user_followers(
        ['ride_list'],
        amount=10,
        randomize=False,
        sleep_delay=60,
    )


with open("runs.log", "a") as f:
    f.write("Ran on {}".format(date.today()))
