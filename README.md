# TweetMood   [![Build Status](https://travis-ci.com/kirillzabrodin/tweet_mood.svg?branch=master)](https://travis-ci.com/kirillzabrodin/tweet_mood)   [![codecov](https://codecov.io/gh/kirillzabrodin/tweet_mood/branch/master/graph/badge.svg)](https://codecov.io/gh/kirillzabrodin/tweet_mood)
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
Set up a project directory and clone the repo with `git clone this_project_url`.

You will need some API keys, both locally and in your Travis CI settings:
* A 'TWEETMOOD_SECRET_KEY' (used in settings.py) - this is automatically generated on a new Django set-up, and can be a random string. This is used for administration so keeping this secret is important.

* An API key for Watson (used in tweetmood/watson.py) saved as 'WATSON_TONE_ANALYZER'. This can be gotten from [the bluemix website](https://console.bluemix.net/).

Make sure you have python 3 and pip 3 installed. If you have python 2 installed change python to python3 in the code below. Do the same for pip.

Run `pip install -r requirements.txt`.

Run `python ./manage.py runserver`. You can run the migrations as suggested if Django suggests it.

This defaults to port 8000, so open `localhost:8000` in your browser.

## Usage

At the moment whatever you type in will be analysed and the prominent mood displayed. Further progress will be shared shortly.

## Testing

The testing framework uses:
* pytest (including pytest-django and pytest-cov for coverage)
* selenium

As selenium is used, make sure you have Firefox installed.

Run `pytest`. Usually running `python manage.py collectstatic --noinput` is required to pass the tests.

To see a test coverage table run `open htmlcov/index.html`

The app uses a third-party API. Where required the tests mock calls to the API.

## Deployment

The application is deployed on [Heroku](https://tweet-mood.herokuapp.com/). The first load might take a while, but it will boot up eventually. This can be used without any API keys necessary.

## Our Approach

Read our [manifesto](https://github.com/kirillzabrodin/tweet_mood/wiki/Manifesto) to learn about our approach.

## Contributing

Feel free to pull request any features you would like to add, however 100% code coverage is required as well as approvals from two of the founding members for it to be added.

## Issues

Open up an issue [here](https://github.com/kirillzabrodin/tweet_mood/issues) and we will try to get back to you as soon as possible.
