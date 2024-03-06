
# Main Program
input_file = open('baseball.in', 'r')
output_file = open('baseball.out', 'w')

num = int(input_file.readline())

positions = []
for i in range(num):
    positions.append(int(input_file.readline()))

positions.sort()

total = 0
for i in range(num):
    for j in range(i+1, num):
        differ = positions[j] - positions[i]
        low = positions[j] + differ
        high = positions[j] + differ * 2

        left = j + 1
        while left < num and positions[left] < low:
            left += 1

        right = left
        while right < num and positions[right] <= high:
            right += 1

        total += right - left

output_file.write(str(total))

input_file.close()
output_file.close()