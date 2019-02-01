# TweetMood   [![Build Status](https://travis-ci.com/kirillzabrodin/tweet_mood.svg?branch=master)](https://travis-ci.com/kirillzabrodin/tweet_mood)   [![codecov](https://codecov.io/gh/kirillzabrodin/tweet_mood/branch/master/graph/badge.svg)](https://codecov.io/gh/kirillzabrodin/tweet_mood)   [![Maintainability](https://api.codeclimate.com/v1/badges/c36bb6965805cd5f41af/maintainability)](https://codeclimate.com/github/kirillzabrodin/tweet_mood/maintainability)   [![Codacy Badge](https://api.codacy.com/project/badge/Grade/53289efff5ef47be9ec24611b0a09f27)](https://www.codacy.com/app/kirillzabrodin/tweet_mood?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kirillzabrodin/tweet_mood&amp;utm_campaign=Badge_Grade)   [![Known Vulnerabilities](https://snyk.io/test/github/kirillzabrodin/tweet_mood/badge.svg)](https://snyk.io/test/github/kirillzabrodin/tweet_mood)
An application for analysing the emotions in tweets from around London.

### [Team](https://github.com/kirillzabrodin/tweet_mood#team) |  [User stories](https://github.com/kirillzabrodin/tweet_mood#user-stories) |  [Getting started](https://github.com/kirillzabrodin/tweet_mood#getting-started) |  [Usage](https://github.com/kirillzabrodin/tweet_mood#usage) |  [Testing](https://github.com/kirillzabrodin/tweet_mood#testing) |   [Deployment](https://github.com/kirillzabrodin/tweet_mood#deployment) |   [Our approach](https://github.com/kirillzabrodin/tweet_mood#our-approach) |  [Contributing](https://github.com/kirillzabrodin/tweet_mood#contributing)

## Team

* [Chris Gilbert](https://github.com/chrisjgilbert)
* [Tom Pickering](https://github.com/topickering)
* [James de Winton](http://github.com/jamesdew12)
* [Kirill Zabrodin](https://github.com/kirillzabrodin)

## User Stories
```
As a User,
so I can pick up the moods of London,
I would like to pick a twitter topic for London

As a User,
so I can pick what I content is being examined,
I would like to be able to choose the content that is analysed

As a User,
so I can see what people feel about my topic,
I would like to be able to see the analysis
```

## Getting started
Clone the repo with `git clone this_project_url`.

You will need some API keys, locally, in your Travis CI and/or Heroku settings:

* A [Django SECRET_KEY](https://github.com/kirillzabrodin/tweet_mood/blob/master/mysite/settings.py) - this is automatically generated on a new Django set-up, and can be a random string.  Keep yours hidden as it gives admin rights for the project.

* An API key for [Watson](https://github.com/kirillzabrodin/tweet_mood/blob/master/tweetmood/watson.py) - this can be gotten from [the bluemix website](https://console.bluemix.net/).

* You will also need a [Twitter key](https://github.com/kirillzabrodin/tweet_mood/blob/tweepy/tweetmood/tweeterpy.py) and any other required credentials for making requests to the twitter API. Those will go into your environment as the twitter documentation instructs you.

Make sure you have python 3 and pip 3 installed. If you have python 2 installed as well change python to python3 in the code below. Do the same for pip by changing it to pip3.

Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

Run `python ./manage.py runserver` or `python3 ./manage.py runserver`

This defaults to port 8000, so open `localhost:8000` in your browser.

Please note that the app will take a short while to deploy as Holmes (see below) will take approximately 10-15 seconds to train on deployment.

## Usage

At the moment whatever you type in will be analysed and the prominent mood displayed. Further progress will be shared shortly.

### Holmes and Watson

Holmes and Watson are two distinct sentiment analysers - find more information on them [here](https://github.com/kirillzabrodin/tweet_mood/blob/docs_folder/documents/HolmesAndWatson.md).

## Testing

The testing framework uses:
* pytest (including pytest-django and pytest-cov for coverage)
* selenium
* jasmine

As selenium is used, make sure you have Firefox installed.

Run `pytest`. Usually running `python manage.py collectstatic --noinput`/`python3 manage.py collectstatic --noinput` and `python -m textblob.download_corpora`/`python3 -m textblob.download_corpora` is required to pass the tests.

To run the view JavaScript Jasmine tests, `open tweetmood/static/js/SpecRunner.html`

To see a test coverage table run `open htmlcov/index.html`

To see code quality run `radon cc tweetmood/*.py -a`.

To use the linter run `pylama`.

The app uses a third-party API. Where required the tests mock calls to the API.

## Deployment

The application is deployed on [Heroku](https://tweet-mood.herokuapp.com/). The first load might take a while, but it will boot up eventually. This can be used without any API keys necessary.

## Our Approach

Read our [manifesto](https://github.com/kirillzabrodin/tweet_mood/wiki/Manifesto) to learn about our approach. Our Trello board is [here](https://trello.com/b/fG7kmZBO/api-tweet).

[[https://github.com/kirillzabrodin/tweet_mood/blob/README/documents/trello_board.png|alt=trello_board]]

## Contributing

Feel free to pull request any features you would like to add, however 100% code coverage is required as well as approvals from two of the founding members for it to be added.

## Issues

Open up an issue [here](https://github.com/kirillzabrodin/tweet_mood/issues) and we will try to get back to you as soon as possible.
