Holmes is an example of a NaiveBayesClassifier, imported from [TextBlob](https://textblob.readthedocs.io/en/dev/index.html#) / [NLTK](http://www.nltk.org/) and subject to supervised machine learning in order to classify inputted text as positive or negative.

Classifiers work by calculating the probability of inputted text belonging to a particular class.  In order to make this calculation, the classifier must be 'trained' by being passed examples of text which belongs in the desired classes: for example, tweets which have already been classified as positive or negative.  Larger training sets result in more accurate classification, but training and analysing can take longer.

By default, Holmes is trained on a sample of 1,000 tweets (500 positive, 500 negative).  These tweets were taken from the huge library available from Stanford University's [Sentiment140 project](http://help.sentiment140.com/for-students/).  The raw data from the Sentiment140 library can be formatted for use by Holmes by using the program in 'tweetmood/holmes_data/csv_formatting.py' - input the relevant file paths then run:
```
python tweetmood/holmes_data/csv_fomatting.py
```
or
```
python3 tweetmood/holmes_data/csv_fomatting.py
```

Holmes can be trained on different data sets.  This repository contains a larger formatted tweet sample set: replacing
```
with open('tweetmood/holmes_data/reformatted_small_train.csv', 'r') as train:
```
in 'tweetmood/holmes.py' with
```
with open('tweetmood/holmes_data/reformatted_train.csv', 'r') as train:
```
will train Holmes on a data set of 10,000 tweets - please note this additional training takes more time when deploying the app.

To test the accuracy of Holmes once training has been completed, Holmes can be tested against a sample test data set:
```
with open('tweetmood/holmes_data/formatted_test.csv', 'r') as test:
  classifier.accuracy(test))
```

Watson is a deep learning question answering system developed by IBM's DeepQA project. Watson was originally developed to answer questions for the American gameshow 'Jeopardy' - in a televised broadcast Watson took on and beat the reigning champion (check it out on [YouTube](https://www.youtube.com/watch?v=wZxq01DcvGA)).

Watson has since expanded and has many applications.  Tweetmood uses the Tone Analyzer function of Watson, which performs sentiment analysis on text and returns various scores, including scores for Joy, Anger, Fear, Sadness and Disgust.  Find out more about Watson [here](https://www.ibm.com/watson/).
