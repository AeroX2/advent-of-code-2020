import sys

data = open(sys.argv[1]).readlines()

def binary_search(state, upper):
    mid = (state[0]+state[1])//2
    if (upper):
        return (state[0], mid)
    else:
        return (mid+1, state[1])


seat_ids = []
for line in data:
    line = line.strip()

    state = (0, 127)
    for c in line[:7]:
        state = binary_search(state, c == 'F')
    seat_id = state[0] * 8

    state = (0, 7)
    for c in line[7:]:
        state = binary_search(state, c == 'L')

    seat_id += state[0]

    seat_ids.append(seat_id)

seat_ids = sorted(seat_ids)
for i in range(len(seat_ids)):
    if (seat_ids[0]+i != seat_ids[i]):
        print(seat_ids[i], seat_ids[0]+i)
        break
