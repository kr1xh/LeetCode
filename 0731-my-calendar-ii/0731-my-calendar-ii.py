class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:

        for s, e in self.overlaps:
            if max(start, s) < min(end, e):
                return False

        for s, e in self.booked:
            if max(start, s) < min(end, e):
                self.overlaps.append((max(start, s), min(end, e)))

        self.booked.append((start, end))
        return True