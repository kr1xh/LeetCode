from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        
        n = len(friends)
        visited = [False] * n
        
        q = deque([id])
        visited[id] = True
        curr_level = 0
        
        while q and curr_level < level:
            for _ in range(len(q)):
                person = q.popleft()
                
                for f in friends[person]:
                    if not visited[f]:
                        visited[f] = True
                        q.append(f)
            
            curr_level += 1
        
        freq = Counter()
        
        for person in q:
            for video in watchedVideos[person]:
                freq[video] += 1
        
        return sorted(freq.keys(), key=lambda x: (freq[x], x))