class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(tickets)
        queue = [(tickets[i], i) for i in range(n)]  

        time = 0
        while queue:
            ticket_count, position = queue.pop(0) 
            min_tickets = min(ticket_count, 1) 
            time += min_tickets  
            ticket_count -= min_tickets 

            if ticket_count > 0: 
                queue.append((ticket_count, position))
            if position == k and ticket_count == 0:  
                return time

        
