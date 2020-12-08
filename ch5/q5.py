import sys

data = open(sys.argv[1]).readlines()

def binary_search(state, upper):
    mid = (state[0]+state[1])//2
    if (upper):
        return (state[0], mid)
    else:
        return (mid+1, state[1])


max_seat_id = 0
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

    max_seat_id = max(seat_id, max_seat_id)
print(max_seat_id)
