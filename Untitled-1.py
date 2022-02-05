strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"] 
k = 2

def longest_consec(strarr, k):
    # Figure out the length of each index in the array.
    # Then concatenate the strings in the array by the value k
    # Return the first longest string in the array.
    x = []

    longest_string = max(strarr, key=len)
    
    # Need to concat 

    for i in range(len(strarr)):
        x.append(strarr[i] + strarr[i + 1])
        print(x[i])

   # print(strarr[0] + strarr[1])
   # print(strarr[1] + strarr[2])
   # print(strarr[2] + strarr[3])
   # print(strarr[3] + strarr[4])

longest_consec(strarr, k)