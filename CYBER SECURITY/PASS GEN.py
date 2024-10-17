"""
Project: SIMPLE PASSWORD GENERATOR USING PYTHON
Developed by: CyberAbhi
Created: 17th OCTOBER, 2024  
"""
import string
import random
def generatePassword(length,custom):

    character=string.ascii_letters + string.punctuation + string.digits
    password="".join(random.sample(character, length)) + custom
    return password

length=int(input("Enter length of the Password : "))
custom=input("Enter the custom character you want to be included in your Password : ")
password=generatePassword(length,custom)
print("Generated Password is : ",password)