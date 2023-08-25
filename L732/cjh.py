from sortedcontainers import SortedList
class MyCalendarThree(object):

    def __init__(self):
        self.event = SortedList()

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        self.event.add((startTime, 1))
        self.event.add((endTime, -1))
        x = ans = 0

        for _, e in self.event:
            x += e
            ans = max(ans, x)
        return ans
        

        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)