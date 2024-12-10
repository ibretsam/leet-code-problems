"""
355. Design Twitter
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see 
the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function 
will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed 
must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet 
id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following 
user 2.
 

Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 10^4
All the tweets have unique IDs.
At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""

import heapq
from collections import defaultdict
class Tweet:
    def __init__(self, tweetId: int, index: int):
        self.tweetId = tweetId
        self.index = index
class Twitter:

    def __init__(self):
        self.user_tweet = defaultdict(list)
        self.follows = defaultdict(list)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = Tweet(tweetId, len(self.tweets) + 1)
        self.tweets.append(tweet)
        self.user_tweet[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweet = self.user_tweet[userId].copy()
        followers = self.follows[userId]
        print(followers)
        for follower in followers:
            all_tweet += self.user_tweet[follower]
        tweet_indexes = [-tweet.index for tweet in all_tweet]
        heapq.heapify(tweet_indexes)
        tweets = []
        for _ in range(10):
            if not tweet_indexes:
                break
            tweets.append(-heapq.heappop(tweet_indexes))
        res = []
        for tweet_index in tweets:
            for tweet in all_tweet:
                if tweet_index == tweet.index:
                    res.append(tweet.tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            return
        self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
        
        
# Test case
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1)) # [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1)) # [6, 5]
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1)) # [5]