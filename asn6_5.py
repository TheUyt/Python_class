text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
number = text[pos:]
print number
result = float(number)
print result