from re import S
import numpy as np


square_no = float(input("Enter a number: "))


if square_no >= 0:
  if square_no == 0:
      print("Uhhhh..Zero??")
else:
  print("Wait...What?")


iteration = 0

PRECISION = 5
dp = 0
apprx = 100

def approximate(square_no: int, apprx: int):
    return 1/2*(apprx + square_no/apprx)

    
while dp < PRECISION:
    while True:
        this_apprx = approximate(square_no, apprx)

        if np.round_(this_apprx, dp) == np.round(apprx, dp):
            apprx = this_apprx
            dp+=1
            iteration+=1
            break
        else:
            apprx = this_apprx
            iteration+=1
            continue

print(f"Approximation: {apprx}, went through {iteration} iterations.")

