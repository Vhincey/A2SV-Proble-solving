class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones] # Creating a max heap
        heapq.heapify(heap)
        print(heap)
       
        while len(heap) > 1:
            # Get the heaviest stone
            x = -heapq.heappop(heap)  
            # Get the second heaviest stone
            y = -heapq.heappop(heap)  
            
            if x != y:
                diff = x - y
                heapq.heappush(heap, -diff)  #Add their difference back into heap
        
        return 0 if not heap else -heap[0]
