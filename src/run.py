from instapy import InstaPy
from instapy import smart_run

from dotenv import load_dotenv

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
    'surf', 'surfing', 'surfer',
]

session = InstaPy(
    username=username,
    password=password,
    headless_browser=True
)

with smart_run(session):
    session.set_do_comment(enabled=True,  percentage=25)
    session.set_comments(comments)
    session.like_by_tags(hashtags, amount=10)
    session.interact_by_users(['_williambuck_'])