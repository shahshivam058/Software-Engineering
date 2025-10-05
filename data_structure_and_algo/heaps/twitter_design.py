"""
Design Simplified version of twitter 

Twitter() Insilize object constructor we insilise data structure 

void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.


create a hashmap 

map user id ------> following ids whoever we follow will be added to list 
unfollow Removing is not same as adding  search on entire list and find : end and remove in o(1) Time
each user can post a twit and it can be more than one 
get most recent twit 
count we will decrement to utilise the max heap 
we will spasefic create a tweetmap to store the count and post againest each user id 


removal and add make it o(1) with help of set 


"""
from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        againest each user id store the count of tweet and tweet id 
        store only 10 tweets per each users as thats what we need 
        once we added 10th tweet remove the first one we dont need that 
        adter each tweet decresing the count help us in max heap 
        """
        self.tweetMap[userId].append([self.count ,tweetId ])
        if len(self.tweetMap[userId]) > 10  :
            self.tweetMap[userId].pop(0)
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        we even need the tweets posted by ourselves
        so also add ourselvs in following id 
        users also follow him self 
        fetch each followe 
        check if he tweeted anything or not 
        if tweeted then 
        add to max heap 
        if size of max heap is > 10 then removbe 
        Gets the index of the most recent tweet, which is at the end of the list.
        push data to heap 


        """
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # Gets the index of the most recent tweet, which is at the end of the list.

                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
                
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)