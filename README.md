# TweetMood   [![Build Status](https://travis-ci.org/kirillzabrodin/tweet_mood.svg?branch=master)](https://travis-ci.org/kirillzabrodin/tweet_mood)   [![codecov](https://codecov.io/gh/kirillzabrodin/tweet_mood/branch/master/graph/badge.svg)](https://codecov.io/gh/kirillzabrodin/tweet_mood)
An application for analysing the emotions in text

### [Team](https://github.com/kirillzabrodin/tweet_mood#team) |  [User stories](https://github.com/kirillzabrodin/tweet_mood#user-stories) |  [Getting started](https://github.com/kirillzabrodin/tweet_mood#getting-started) |  [Usage](https://github.com/kirillzabrodin/tweet_mood#usage) |  [Testing](https://github.com/kirillzabrodin/tweet_mood#testing) |   [Deployment](https://github.com/kirillzabrodin/tweet_mood#deployment) |   [Our approach](https://github.com/kirillzabrodin/tweet_mood#our-approach) |  [Contributing](https://github.com/kirillzabrodin/tweet_mood#contributing)

## Team

* [Chris Gilbert](https://github.com/chrisjgilbert)
* [Tom Pickering](https://github.com/topickering)
* [James de Winton](http://github.com/jamesdew12)
* [Kirill Zabrodin](https://github.com/kirillzabrodin)

## User Stories
```
As a User,
so I can pick up the moods of peoples words,
I would like to receive the emotions in someones words

As a User,
so I can pick what I content is being examined,
I would like to be able to choose the content that is analysed
```

## Getting started
Set up a project directory and clone the repo with ```git clone``` and the appropriate url.

You will need some API keys, both locally and in your Travis CI settings:
* A Django SECRET_KEY (found in settings.py) - this is automatically generated on a new Django set-up, and can be a random string.  Keep yours hidden(for example, in this project settings.py points to a local environmental variable)
* An API for Watson (found in tweetmood/watson.py) - see [] for more information on Watson

Make sure you have python 3 and pip 3 installed. If you have python 2 installed change python to python3 in the code below. Do the same for pip.

Run ```pip install -r requirements.txt```

Run ```python ./manage.py runserver```

This defaults to port 8000, so open ```localhost:8000``` in your browser.

## Usage

## Testing

The testing framework uses:
* pytest (including pytest-django and pytest-cov for coverage)
* selenium

As selenium is used, make sure you have Firefox installed.

Run ```pytest```

To see a test coverage table run ```open htmlcov/index.html```

## Deployment

## Our Approach

## Contributing
