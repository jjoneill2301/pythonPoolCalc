# Write a Python program to calculate the estimated number of gallons in a swimming pool.
# We will be calculating for in ground pools that are Square/Rectangle or Circular pools.

# Named Constants
fPI = 3.14
fCUBIC_FEET_TO_GALLONS = 7.5

# Ask the user if the Pool is S for Square/Rectangle or C for Circular
sShape = input("Is the pool a square or circle? Enter either 'S' or 'C': ").upper()

# Only if the pool is Square get these inputs:
if sShape == 'S':
    fLength = float(input("Enter the length of the pool in feet: "))
    fWidth = float(input("Enter the width of the pool in feet: "))
    fShallowDepth = float(input("Enter the depth of the shallow end in feet: "))
    fDeepDepth = float(input("Enter the depth of the deep end in feet: "))
    # Calculations
    fAverageDepth = (fShallowDepth + fDeepDepth)/2
    fTotalCubicFeet = fLength * fWidth * fAverageDepth
    fTotalGallons = fTotalCubicFeet * fCUBIC_FEET_TO_GALLONS
    # Output
    print(f"The estimated volume of the pool (expressed in gallons) is {fTotalGallons:,.2f}")

# Only if the pool is Circular get these inputs:
elif sShape == 'C':
    fDiameter = float(input("Enter the diameter of the pool in feet: "))
    fShallowDepth = float(input("Enter the depth of the shallow end in feet: "))
    fDeepDepth = float(input("Enter the depth of the deep end in feet: "))
    # Calculations
    fRadius = fDiameter/2
    fAverageDepth = (fShallowDepth + fDeepDepth)/2
    fCircumference = fPI * fRadius * fRadius
    fTotalCubicFeet = fCircumference * fAverageDepth
    fTotalGallons = fTotalCubicFeet * fCUBIC_FEET_TO_GALLONS
    # Output
    print(f"The estimated volume of the pool (expressed in gallons) is {fTotalGallons:,.2f}")
