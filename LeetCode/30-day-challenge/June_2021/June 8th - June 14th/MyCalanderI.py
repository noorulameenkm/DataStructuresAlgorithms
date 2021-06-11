class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start, end):
        
        if len(self.bookings) == 0:
            self.bookings.append([start, end])
            return True
            
        for booking in self.bookings:
            if start >= booking[0] and start < booking[1]:
                return False
            
            if start < booking[0] and end > booking[0]:
                return False
        
        self.bookings.append([start,end])
        self.bookings.sort(key=lambda booking: booking[0])
        return True



# Test case 1
calender = MyCalendar()
print(calender.book(10, 20))
print(calender.book(15, 25))
print(calender.book(20, 30))