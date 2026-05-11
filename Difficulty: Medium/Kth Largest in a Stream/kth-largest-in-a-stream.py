import heapq

class Solution:
    def kthLargest(self, arr, k):
        result = []
        min_heap = []  # Min-heap to store K largest elements
        
        for num in arr:
            # Add element to heap
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:  # If current num is larger than smallest in K largest
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
            
            # After insertion, check if we have K elements
            if len(min_heap) == k:
                result.append(min_heap[0])  # Smallest of the K largest = Kth largest
            else:
                result.append(-1)
        
        return result