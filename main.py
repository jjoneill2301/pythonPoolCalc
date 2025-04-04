# Write a Python program to calculate the estimated number of gallons in a swimming pool.
# We will be calculating for in ground pools that are Square/Rectangle or Circular pools.

# Named Constants
fPI = 3.14
fCUBIC_FEET_TO_GALLONS = 7.5

while 1: # Ask the user if the Pool is S for Square/Rectangle or C for Circular
    sShape = input("Is the pool a square or circle? Enter either 'S' or 'C': ").upper()
    if sShape in ('S', 'C'):
        print("Answer each query for length in feet")
        break
    print("Invalid input. Please enter 'S' or 'C'.")


# Only if the pool is Square get these inputs:

if sShape == 'S':
    while 1:
        try:
            fShallowLength = float(input(f"{'Enter the length from the beginning of the shallow end to the beginning of the decline:':<90}"))
            if fShallowLength < 1:
                raise ValueError()
            fTransitionLength = float(input(f"{'Enter the length from the beginning of the decline to the end of the decline:':<90}"))
            if fTransitionLength  < 1:
                raise ValueError()
            fDeepLength = float(input(f"{'Enter the length from the beginning of end of the decline to the end of the pool:':<90}"))
            if fDeepLength  < 1:
                raise ValueError()
            fShallowDepth = float(input(f"{'How deep is the shallow end:':<90}"))
            if fShallowDepth  < 1:
                raise ValueError()
            fDeepDepth = float(input(f"{'How deep is the deep end:':<90}"))
            if fDeepDepth  < 1:
                raise ValueError()
            fPoolWidth = float(input(f"{'How wide is the pool:':<90}"))
            if fPoolWidth  < 1:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Input must be numeric. Please only enter your answers as at least one foot.")
    # Calculations
    fShallowVolume = (fShallowLength * fShallowDepth * fPoolWidth)
    fTransitionTopVolume = (fTransitionLength * fShallowDepth * fPoolWidth) # Calculate top half of decline
    fTransitionBottomVolume = (((fTransitionLength * (fDeepDepth - fShallowDepth))/2) * fPoolWidth) # Calculate bottom half of mid
    fDeepVolume = (fDeepLength * fDeepDepth * fPoolWidth)

    fTotalVolInCubicFeet = fShallowVolume + fTransitionTopVolume + fTransitionBottomVolume + fDeepVolume
    fTotalGallons = fTotalVolInCubicFeet * fCUBIC_FEET_TO_GALLONS
    # Output
    print(f"The estimated volume of the pool (expressed in gallons) is {fTotalGallons:,.2f}")

# Only if the pool is Circular get these inputs:
elif sShape == 'C':
    while 1:
        try:
            fDiameter = float(input(f"{'Enter the diameter of the pool:':<45}"))
            if fDiameter < 1:
                raise ValueError
            fShallowDepth = float(input(f"{'Enter the depth of the shallow end:':<45}"))
            if fShallowDepth < 1:
                raise ValueError
            fDeepDepth = float(input(f"{'Enter the depth of the deep end in feet:':<45}"))
            if fDeepDepth < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Input must be numeric. Please only enter your answers as at least one foot.")
    # Calculations
    fRadius = fDiameter/2
    fAverageDepth = (fShallowDepth + fDeepDepth)/2
    fCircumference = fPI * fRadius * fRadius
    fTotalCubicFeet = fCircumference * fAverageDepth
    fTotalGallons = fTotalCubicFeet * fCUBIC_FEET_TO_GALLONS
    # Output
    print(f"The estimated volume of the pool (expressed in gallons) is {fTotalGallons:,.2f}")