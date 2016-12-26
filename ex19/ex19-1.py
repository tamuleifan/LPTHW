def cracker_count(crackers_per_box, boxes_of_crackers):
	print "I am supposed to count the total number of crackers"
	total_number = crackers_per_box*boxes_of_crackers
	print "You have %d crackers totally." %total_number

cracker_count(10, 10)

cracker_count(10+1, 10-1)

crackers_per_box = 10
boxes_of_crackers = 10
cracker_count(crackers_per_box, boxes_of_crackers)

print "Now you tell me how many crackers in one box and how many hoxes you have."
cpb = int(raw_input("crackers per box: "))
boc = int(raw_input("boxes of crackers: "))
cracker_count(cpb, boc)