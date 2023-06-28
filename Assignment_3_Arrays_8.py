def canAttendMeetings(intervals):
        new_intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1,len(new_intervals)):
            if new_intervals[i-1][1] > new_intervals[i][0]:
                return False
        return True

if __name__ == "__main__":
    intervals  = [[0,30],[5,10],[15,20]]
    print(canAttendMeetings(intervals))