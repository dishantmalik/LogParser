# Breaking this code into 3 steps
# Step 1 is to read the log file and test the read output 
# Step 2 is to build a simple regex that looks for numbers in a IPv4 format (0-3.0-3.0-3.0-3)
# Step 3 is to filter clean and valid IPs from the extracted IPs and print the result.
# References
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re
import json

# Step 1
valid_ip = []

with open('Enter the path to the .json AWS CloudTrail log file', 'r') as f:

	line = f.read()
	reader = (json.loads(line))
  
# Step 2
	regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

	ip = (re.findall(regex, str(reader)))
	
# Step 3
	for i in ip:
		valid_ip =  list(map(int, str(i).split(".")))
				
		for j in valid_ip:
			if j > 255 or j <0:
				ip.remove(i)
        print ("Valid IP addresses: ", ip) 
