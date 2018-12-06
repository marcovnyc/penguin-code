 ## BMI = (	Weight in Pounds / (Height in inches) x (Height in inches)) x 703 ##

h_feet = int(input('Enter your Height in Feet: '))
h_inches =  int(input('Enter your Height inches: '))
W = int(input('Enter your Weight in Pounds: '))
height = h_feet * 12 + h_inches

BMI =  (W / ( height * height)) * 703
print('Your BMI is ', BMI)

# Todo: Depending on your BMI you are told you are either one of the status below 
#BMI	Weight Status
#Below 18.5	Underweight
#18.5 – 24.9	Normal
#25.0 – 29.9	Overweight
#30.0 and Above	Obese
