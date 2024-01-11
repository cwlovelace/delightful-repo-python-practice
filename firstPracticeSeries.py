
# The first portion of this is a basic control flow test
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
#planet = int(input ("Please enter the number for your planet: "))
#weight = float(input ("Please enter your weight: "))

if planet == 1:
    weight *= 0.91
elif planet == 2:
    weight *= .38
elif planet == 3:
    weight *= 2.34
elif planet == 4:
    weight *= 1.06
elif planet == 5:
    weight *= .92
elif planet == 6:
    weight *= 1.19

print("You have selected planet " + str(planet) + ".")
print("On this planet, your weight is: " + str(weight) + "pounds.")

# This next portion tests basic list ideas
heights = [61, 70, 67, 64]
heights.append(65)
heights += [25]

print(heights)
print(heights[2])

print(heights[-1])