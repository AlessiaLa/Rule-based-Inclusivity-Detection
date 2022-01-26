
# Rule-based Inclusivity Detection

This project proposes a method for non-inclusiveness detection in Italian language, based on some heuristic rules.
Two approaches are used in developing the rules:
- Pattern matching: the presence of a certain structural or grammatical pattern is checked.
- Lexicon based: basing on some lexicons, the presence of certain expressions is checked.

In particular, the module is developed to work on italian lists of tweets.
It's possible to load a CSV of tweets already available or to scrape a list of tweets, given a user id, that will be saved in a CSV file.

For the extraction of the tweets from Twitter, given a user id, it's used the "search tweet" module of the project "hate tweet map" developed by Dario Amoroso d'Aragona.
## Authors

- [@AlessiaLa](https://www.github.com/AlessiaLa)
- [@danielagrassi](https://www.github.com/DanielaGrassi)


## Acknowledgements

 - Hate Tweet Map [https://darioamorosodaragona.gitlab.io/hatemap/] 
