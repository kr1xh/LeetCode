from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        
        if source == target:
            return 0
        
        stop_to_bus = defaultdict(list)
        
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].append(i)
        
        q = deque([source])
        visited_stops = {source}
        visited_buses = set()
        
        buses_taken = 0
        
        while q:
            buses_taken += 1
            
            for _ in range(len(q)):
                stop = q.popleft()
                
                for bus in stop_to_bus[stop]:
                    
                    if bus in visited_buses:
                        continue
                    
                    visited_buses.add(bus)
                    
                    for nxt_stop in routes[bus]:
                        
                        if nxt_stop == target:
                            return buses_taken
                        
                        if nxt_stop not in visited_stops:
                            visited_stops.add(nxt_stop)
                            q.append(nxt_stop)
        
        return -1