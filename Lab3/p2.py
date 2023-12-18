# Pseudo code fot O(n*2)
#  For each user i from 1 to n:
#    For each user j from i+1 to n:
#       If user i and user j overlap (xi <=yj and xj>=yi):
#           Increment the counter by 1
#  Return the counter as num of distinct pairs

def friendSlower(Input):
    n=len(Input)
    overlapping_pairs=[]
    for i in range(n):
        for j in range(i+1,n):
            if Input[i][0] <=Input[j][1] and Input[j][0] <=Input[i][1]:
                overlapping_pairs.append(i+1,j+1)

    return overlapping_pairs




# pseudocode for algorithm of O(nlogn)
# Initialize an empty list of events
# For each user i from 1 to n:
#     Add event(ai,"Enter",i) to the list of events
#     Add event(bi,"Leave",i) to the list of events
# Sort the list of events by TimeoutError
# Initialize a set of active_users
# initialize a counter to 0

# For each event (t, event_type, user_id) in the sorted list of events
#      If event_type is "Enter":
#         Add user_id to active_users
#      If event_type is "Leave":
#         Remove user_id from active_users
#      Now Increment the counter by size of active_users -1 to count overlapping pairs
# Return the counter as the number of distinct pairs


def friendFaster(Input):
    events=[]
    n=len(Input)
    for i in range(n):
        events.append((Input[i][0],"enter",i))
        events.append((Input[i][1],"leave",i))

    events.sort()

    active_users=set()
    count=0
    overlapping_pairs=[]
    for event in events:
        t, event_type,user_id=event
        if event_type=="enter":
            active_users.add(user_id)
        else:
            active_users.remove(user_id)
            count+=len(active_users)
            overlapping_pairs.extend((i+1,user_id+1) for i in active_users)

    return overlapping_pairs
