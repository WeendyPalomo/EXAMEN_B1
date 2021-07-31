import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################
ckey = "zSUhUGY1T9PbQp5C0w1VxNRMS"
csecret = "i1FgzlERH54Deh1iTbf6KRWGyGPCHKuvwWV67kwLLLa2pawGIU"
atoken = "1419416357922344967-466Jgek0fyjUksKqWPSIQemDk2Vhtn"
asecret = "VfZziMEMTzRm0vNOTiWJ8LwB1kWI4uBLIAqe1VGe3F78Y"


class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:

            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

################# COUCHDB #################
server = couchdb.Server('http://admin:StEvEn20@127.0.0.1:5984/')
try:
    db = server.create('twitter_juegosolimpicos')
except:
    db = server['twitter_juegosolimpicos']

################# LOCATIONS #################
twitterStream.filter(track=['juegos olimpicos', 'Tokio 2020'])