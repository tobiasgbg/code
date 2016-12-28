no_elves = 3012210

elves = [0 for x in range(no_elves)]
for x in range(0, no_elves):
    elves[x] = x

elves_no_presents = [1 for x in range(no_elves)]

elf = 0
step = no_elves / 1000
multiplyer = 1000
while (len(elves) > 1):

    index = (elves.index(elf) + 1) % len(elves)
    elves_no_presents[elves.index(elf)] += elves_no_presents[index]
    elves_no_presents[index] = 0
    del elves[index]
    del elves_no_presents[index]

    elf = elves[(index + 1) % len(elves)]
    
    if (len(elves) < step * multiplyer):
        print ('no elves: ' + str(len(elves)))
        multiplyer -= 1

print(elves)