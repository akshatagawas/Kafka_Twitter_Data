from tweepy.streaming import Stream
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import time

# Move StdOutListener definition before imports
class StdOutListener(Stream):
    def __init__(self, time_limit=time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        super(StdOutListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            # Encode data before sending
            producer.send(kafka_topic, data.encode('utf-8'))
            print(data)
            return True
        else:
            exit(0)  # Use `else` for cleaner exit

    def on_error(self, status):
        print(status)

access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
kafka_endpoint = "ip-20-0-32-4.ap-east-1.compute.internal:9092"
kafka_topic = "new_topic"
twitter_hash_tag = "Elections"
time_limit = 10

kafka = KafkaClient(kafka_endpoint)
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=twitter_hash_tag)
