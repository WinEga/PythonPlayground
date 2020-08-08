# Python program to check 0 power 0 is what?
# power() function
# Ega Learning Curve UK, https://www.youtube.com/channel/UCTmehr9p2PDXN0i_D1FA1QQ
import numpy as np

# input_array
arr1 = [0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0]

# output_array
out = np.power(arr1, arr1)

print("\n Output array : ", out)
