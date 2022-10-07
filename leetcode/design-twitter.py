# 355. Design Twitter
# 🟠 Medium
#
# https://leetcode.com/problems/design-twitter/
#
# Tags: Hash Table - Linked List - Design - Heap (Priority Queue)

import timeit
from collections import defaultdict
from heapq import merge
from itertools import count, islice
from typing import List


# The naive and non object oriented implementation can keep a list of
# tweets from oldest (left) to newest (right) and push into it tuples
# with the tweet ID together with the tweeter's ID. It also keeps a
# hashmap of user: following. When we need to get a user's feed we
# reverse iterate the tweets list looking for post tweeted by users
# that the given user is following.
#
# Time complexity: O(n*t) - Worst case complexity where n is the number
# of posts and t is the number of calls to get feed.
# Space complexity: O(n+t) - N is the number of posts and t is the
# number of users.
#
# Runtime: 69 ms, faster than 7.36%
# Memory Usage: 14.1 MB, less than 64.23%
class NaiveTwitter:
    def __init__(self):
        # Hashmap of userId: following user Ids
        self.users = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            # Create a new user, all users follow themselves.
            self.users[userId] = set([userId])
        self.tweets.append((tweetId, userId))

    # The naive get news feed iterates over all posts in O(n) checking
    # in O(1) to see if they belong to a user followed by the given one.
    def getNewsFeed(self, userId: int) -> List[int]:
        # Get a list of tweets from newest to oldest.
        res = []
        for i in range(len(self.tweets) - 1, -1, -1):
            t, u = self.tweets[i]
            if u in self.users[userId]:
                res.append(t)
                # Once we get to 10 posts, stop.
                if len(res) == 10:
                    break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


# We can improve the previous solution if each user only stores their
# own posts together with the time they were posted at and we use a
# min heap to merge posts from users that we follow and return the 10
# most recent ones.
#
# Runtime: 47 ms, faster than 63.45%
# Memory Usage: 14.1 MB, less than 19.47%
class Twitter:
    def __init__(self):
        # Hashmap of userId: following user Ids
        self.users = defaultdict(set)
        # Tweets are now keyed by user.
        self.tweets = defaultdict(list)
        # Timestamp
        self.timer = count(step=-1)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Running time backwards makes using the min heap simpler.
        self.tweets[userId].append((next(self.timer), tweetId))

    # O(n*log(k)) - Where n is the number of combined tweets in the
    # users' feeds and k is the number of posts we take = 10 => O(n)
    # Space is O(1) - The min heap iterator only keeps 10 items in
    # memory at a time. The 10 reversed iterators keep pointers.
    def getNewsFeed(self, userId: int) -> List[int]:
        # Use heapq merge to generate an iterator over all the followed
        # users' tweets ordered by timestamp, remember to add the
        # current user's tweets.
        tweets = merge(
            *(reversed(self.tweets[u]) for u in self.users[userId] | {userId})
        )
        return [tweet for _, tweet in islice(tweets, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


def test():
    executors = [
        NaiveTwitter,
        Twitter,
    ]
    tests = [
        [
            [
                "Twitter",
                "postTweet",
                "getNewsFeed",
                "follow",
                "postTweet",
                "getNewsFeed",
                "unfollow",
                "getNewsFeed",
            ],
            [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
            [None, None, [5], None, None, [6, 5], None, [5]],
        ],
        [
            ["Twitter", "postTweet", "postTweet", "getNewsFeed"],
            [[], [1, 5], [1, 3], [1]],
            [None, None, None, [3, 5]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "getNewsFeed":
                        result = getattr(sol, call)(t[1][i][0])
                    else:
                        result = getattr(sol, call)(t[1][i][0], t[1][i][1])
                    exp = t[2][i]
                    assert result == exp, (
                        f"\033[93m» {result} <> {exp}\033[91m for"
                        + f" test {col} using \033[1m{executor.__name__}"
                    )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
