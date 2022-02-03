
# Rule-based Inclusivity Detection

This project proposes a method for non-inclusiveness detection in Italian language, based on some heuristic rules.
For the development of the rules, two different approaches have been used.
- Pattern matching: the presence of a certain structural or grammatical pattern is checked.
- Lexicon based: basing on some given or built-in lexicons, the presence of certain words or expressions is checked.

In particular, the module is developed to work on italian lists of tweets.
It's possible to load a CSV of tweets already available or to scrape a list of tweets, given a user id, that will be saved in a CSV file.

For the extraction of the tweets from Twitter, given a user id, it's used the "search tweet" module of the project "hate tweet map" developed by Dario Amoroso d'Aragona.
The project has been developed under the supervision of SWAP Research Group (Semantic Web Access and Personalization) from the Department of Computer Science of Università di Bari "Aldo Moro".

## Authors

The developing team is composed of:
- [@AlessiaLa](https://www.github.com/AlessiaLa)
- [@danielagrassi](https://www.github.com/DanielaGrassi)


## Installation

The project doesn't require particular system configurations, since it only uses libraries that do not require strong computational power.

In this project repo there is a file containing all the needed dependencies for the application and a batch file to create the virtual environment and installing all the dependencies automatically.
To do this is sufficient to type in the IDE terminal:
```bash
  config.bat
```
and then type directly the commands to execute the application, at the end of the installation.
The script works via command line: it's possible to write the associated parameters to the configuration that we want to run.
The possible parameters are the following:
- userid: This parameter should be a Twitter user id
- path: This parameter should be a path to the csv containing a list of tweet
- n_tweet: This parameter should be the number of the tweet to scrape for a certain user
- explain: This parameter return the explanation of the score assigned to each tweet
- no_explain: This parameter doesn't return the explaination of the score assigned to each tweet
- verbose: This parameter records the log of the activities on a file "log.txt"


## Case of use
To use the system it's necessary to place in the folder of the repo.
Then, if the purpose (for example) is to scrape a list of 20 tweets by Matteo Salvini (twitter userid: matteosalvinimi) with the explanation of the scores it is sufficient to write:
```bash
  python <path to Rules.py> --userid matteosalvinimi --n_tweet 20 --explain 
```

If for example the purpose is to load an already given list of tweets in a CSV and calculate the inclusivity score, without explanation but logging the activities, the command will be:
```bash
  python <path to Rules.py> --path <path to csv> --no_explain --verbose
```
## Acknowledgements

 - Hate Tweet Map [https://darioamorosodaragona.gitlab.io/hatemap/] 
 - SWAP UniBa [https://github.com/swapUniba]
## Documentation

[A whole new (inclusive) world](https://linktodocumentation)

