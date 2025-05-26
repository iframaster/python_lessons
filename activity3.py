print("Enter marks obtained in 4 subjects\n")
sub1=int(input("Maths:"))
sub2=int(input("English:"))
sub3=int(input("Science:"))
sub4=int(input("Arts:"))

sum=sub1+sub2+sub3+sub4

print("sum of all subjects is {}".format(sum))

percentage=(sum/400)*100

print(end="Percentage marks=")

print(percentage)