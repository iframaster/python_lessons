amount=int(input("Enter the amount you would like to withdraw:"))

note_1=amount//100

note_2=(amount%100)//50

note_3=((amount%100)%50)//10

print("Note of 100 rupees", note_1)
print("Note of 50 rupees", note_2)
print("Note of 10 rupees", note_3)
