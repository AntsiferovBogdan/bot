MyBot
=====
MyBot is a bot for Telegram which make you happy by sending sweety photos.

Installing
----------
Create virtual environment, activate it and then install requirements:

.. code-block:: text

    pip install -r requirements.txt

Put photos in directory 'images'. Photo's name should include 'cat' at the beginning and '.jpg' at the ending. For example: 'cat2020.jpg'.

Set Up
------
Create settings.py, add next settings:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://YOUR_SOCKS5_PROXY:1080',
        'urllib3_proxy_kwargs': {'username': 'LOGIN', 'password': 'PASSWORD'}}

    API_KEY = ('API_KEY FROM BOTFATHER')

    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:', ':boy:', ':girl:',
                ':mouse:',':frog:',':tiger:',':new_moon_with_face:',':crown:',':alien:']

Launching
---------

In active virtual environment enter:

.. code-block:: text

    python3 bot.py