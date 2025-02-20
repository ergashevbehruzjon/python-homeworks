def convert_cel_to_far(cel):
    return cel*9/5+32
def convert_far_to_cel(far):
    return (far-32)*5/9

far=input("Enter a temperature in degrees F: ")
cel=convert_far_to_cel(float(far))
print(f"{far} degrees F = {cel:.2f} degrees C")

cel=input("Enter a temperature in degrees C: ")
far=convert_cel_to_far(float(cel))
print(f"{cel} degrees C = {far:.2f} degrees F")