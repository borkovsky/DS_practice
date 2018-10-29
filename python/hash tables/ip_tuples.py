# return top n ip addresses from the following document:

# id		time 		ip
# 1,		12=200=122,	11.22,

def count_ip(file, number_top):
	ip_dict = {}
	for elem in file:
		ip_dict.update(elem.split(','))
	ip_tuple = ip_dict.items()
	ip_tuple.sorted()
	return ip_tuple[:number_top]
