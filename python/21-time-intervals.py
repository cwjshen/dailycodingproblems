# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
#   find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

intervals = [(30, 75), (0, 50), (60, 150), (50, 60), (30, 40), (33, 34), (100, 200)]
def get_min_rooms(intervals):
    room_dict = {}
    # Loop through each interval to check
    for index, interval in enumerate(intervals):
        if not room_dict:
            room_dict[str(index)] = [interval]
        else:   
            interval_added = False
            # Loop through each existing room
            for room in room_dict.keys():
                interval_found = False
                # Loop through each time interval associated to a given room
                for room_intervals in room_dict[room]:
                    # If the interval to check exists in the current room, break and move on to next room
                    if (interval[0] > room_intervals[0] and interval[0] < room_intervals[1]) \
                            or (interval[1] > room_intervals[0] and interval[1] < room_intervals[1]):
                        interval_found = True
                        break
                # If we got to the end and the new interval does not exist in the current list of intervals, add it to the current room
                if not interval_found:
                    room_dict[room].append(interval)
                    interval_added = True
                    break
            if not interval_added:
                room_dict[str(len(room_dict))] = [interval]
    print(room_dict)            
    return len(room_dict)

print(get_min_rooms(intervals))

