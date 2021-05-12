#PythonChallenge 1:

puzzle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

orig_alphabets = "abcdefghijklmnopqrstuvwxyz"
encoded_aphabets = "cdefghijklmnopqrstuvwxyzab"
table = puzzle.maketrans(orig_alphabets, encoded_aphabets)
#This shifts all letters by two, that is, a becomes c, b becomes d and so on.

decoded_puzzle = puzzle.translate(table)
print(decoded_puzzle)

#Now change puzzle to "map"
#This gives you "ocr"
#Apply this in the url to progess to the next level
