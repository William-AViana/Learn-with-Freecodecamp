# string slicing to extract the portion of the string after the colon character

string = 'X-DSPAM-Confidence: 0.8405'
i_position = string.find(': ')
number = float(string[i_position+1:])
print(number)