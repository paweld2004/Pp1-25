def detect_people(detector):
    count = 0
    max_count = 0
    for event in detector:
        if event == "+":
            count += 1
            max_count = max(max_count, count)
        elif event == "-":
            count -= 1
            max_count = max(max_count, count)
    return max_count >= 3

print(detect_people("+-+++-+---"))      # True
print(detect_people("+-+-+-+-"))         # False
print(detect_people("+-++-+--"))        # False
print(detect_people("+-++-++-+---"))    # True
