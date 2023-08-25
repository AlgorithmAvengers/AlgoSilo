class MyCalendarThree:

    def __init__(self):
        self.cumul = []

    def book(self, startTime: int, endTime: int) -> int:
        self.cumul.append([startTime, endTime])
        return self.temp(self.cumul)
        
    def temp(self, cumul):
        starts = []
        ends = []
        for i in cumul:
            starts.append(i[0])
            ends.append(i[1])
        starts.sort()
        ends.sort()

        count = 0

        for i in range(len(starts)):
            count += 1
            if ends[0] <= starts[i]:
                count -= 1
                ends.pop(0)

        return count

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)