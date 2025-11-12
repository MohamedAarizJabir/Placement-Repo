import heapq
from multiprocessing import heap
class ListNode:
    def __init__(self, val=0, next=None):
        self.val= val
        self.next= next
def mergeKlists (lists):
     heap=[]

for i,  node in enumerate(lists):
        if node:
           heapq.heappush(heap,( node.value, i, node))
dummy= listnode(0)
current = dummy

while heap:
          val, i, node = heapq.heappop(heap)
current.next = node
current = currrent.next
if node.next:
   heapq.heappush(heap, (node.next.val, i, node.next)): # type: ignore

 return dummy.next
