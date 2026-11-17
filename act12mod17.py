numberLargest = int(input("enter largest number:"))
numberSmallest = int(input("enter ssmallest number:"))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest%numberSmallest
    numberLargest = numberStore

print("HCF is:",numberLargest)