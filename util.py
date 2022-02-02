def pre_process_tweets_response(tweet: dict, includes: dict) -> dict:
    """
    This method take an input a dict representing a tweet (in the Twitter original format) and create a dict containing the usefull information of the tweet reorganized usign different criteria and if necessary renaming the fields.

    Here there is an example of the result of this processing:


    .. code:: json

        {
        "_id": "1411354087682097159",
        "raw_text": "@suncapaldi che cazzo di ragionamento è; io seguo il calcio ma anche se non lo seguissi guarderei i mondiali e gli europei",
        "author_id": "1176108556057227271",
        "author_name": "elisa⁹⁴🦕|| -427; -1",
        "author_username": "CH3RRV91",
        "created_at": "2021-07-03T16:00:10.000Z",
        "lang": "it",
        "possibly_sensitive": false,
        "referenced_tweets": [{
            "id": "1411242299993083909",
            "type": "replied_to"
        }],
        "twitter_entities": {
            "mentions": ["suncapaldi"]
        },
        "geo": {
            "user_location": "h, l, n, z, l ➳in 1d’s arms home (n.) louis yellow (n.) harry sun (n.) niall happy place (n.) zayn safe place (n.) liam fati, ale e fab"
        },
        "metrics": {
            "retweet_count": 0,
            "reply_count": 0,
            "like_count": 0,
            "quote_count": 0
        },
        "processed": false,
        }

    :param tweet: the tweet in Twitter original format
    :type tweet: dict
    :param includes: the includes dict returned by Twitter
    :type includes: dict
    :return: a dict representing a tweet with the useful information
    :rtype: dict

    """

    ent = {}
    post = {'_id': tweet['id'], 'raw_text': tweet['text'], 'author_id': tweet['author_id']}
    retweeted = False
    user_location = None
    for u in includes['users']:
        if u['id'] == post['author_id']:
            post['author_name'] = u['name']
            post['author_username'] = u['username']
            user_location = u.get("location")
            break
    post['created_at'] = tweet['created_at']
    post['lang'] = tweet['lang']
    if "possibly_sensitive" in tweet:
        post["possibly_sensitive"] = tweet["possibly_sensitive"]
    if 'referenced_tweets' in tweet:
        ref_tweets = []
        for rft in tweet['referenced_tweets']:
            ref_tweets.append({'id': rft['id'], 'type': rft['type']})
            if rft['type'] == 'retweeted':
                retweeted = True
                ref_id = rft['id']
                post['complete_text'] = False
                for p in includes['tweets']:
                    if p['id'] == ref_id:
                        post['raw_text'] = p['text']
                        post['complete_text'] = True
                        __extract_context_annotation(post, p)
                        __extract_entities(ent, p)
                        __extract_mentions(ent, p)
                        break
        post["referenced_tweets"] = ref_tweets
    if not retweeted:
        __extract_entities(ent, tweet)
        __extract_context_annotation(post, tweet)

    __extract_mentions(ent, tweet)
    post['twitter_entities'] = ent
    geo = {}
    if 'geo' in tweet:
        geo['geo_id'] = tweet['geo']['place_id']
        for p in includes['places']:
            if p['id'] == geo['geo_id']:
                geo['country'] = p['country']
                geo['city'] = p['full_name']
                break
        post["geo"] = geo
    else:
        if user_location is not None:
            geo = {"user_location": user_location}
            post["geo"] = geo

    post['metrics'] = tweet['public_metrics']

    post['processed'] = False
    return post


def __extract_context_annotation(post, tweet):
    if 'context_annotations' in tweet:
        post['twitter_context_annotations'] = tweet['context_annotations']


def __extract_entities(ent, tweet):
    if 'entities' in tweet:
        if 'hashtags' in tweet['entities']:
            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['tag'])
            ent['hashtags'] = hashtags

        if 'urls' in tweet['entities']:
            urls = []
            for url in tweet['entities']['urls']:
                urls.append(url['url'])
            ent['urls'] = urls
        if 'annotations' in tweet['entities']:
            annotations = []
            for ann in tweet['entities']['annotations']:
                annotations.append(
                    {'type': ann['type'], 'normalized_text': ann['normalized_text'], 'probability': ann['probability']})
            ent['annotation'] = annotations


def __extract_mentions(ent, tweet):
    if 'entities' in tweet:
        if 'mentions' in tweet['entities']:
            mentions = []
            for mention in tweet['entities']['mentions']:
                mentions.append(mention['username'])
            if 'mentions' in ent:
                ent['mentions'] += mentions
            else:
                ent['mentions'] = mentions


def pre_process_user_response(usr: dict) -> dict:
    """
    This method take an input a dict representing an user (in the Twitter original format) and create a dict containing the usefull information of the user reorganized usign different criteria and if necessary renaming the fields.

    Here there is an example of the result of this processing:


    .. code:: json

        {
        "_id": "714034850",
        "name": "TeeJ",
        "username": "VolsTeeJ",
        "public_metrics": {
            "followers_count": 457,
            "following_count": 326,
            "tweet_count": 32541,
            "listed_count": 5
        },
        "location": "Rocky Top, TN"
        }

    :param usr: the user in Twitter original format
    :type usr: dict
    :return: a dict representing a user with the useful information
    :rtype: dict

    """

    user = {'_id': usr["id"], "name": usr["name"], "username": usr["username"], "public_metrics": usr["public_metrics"],
            "location": usr.get("location", None)}
    return user
