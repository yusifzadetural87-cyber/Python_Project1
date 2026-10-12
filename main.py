import bmi
import zodiac
import birthday

while True:
    print("press 'a1' for BMI ")
    print("press 'a2' for zodiac ")
    print("press 'a3' for birthday_guess ")
    print("press 'a4' for exit ")
    
    ans=input("Choose one:", )
    
    if ans=="a1":
        bmi.T()
    elif ans=="a2":
        zodiac.T()
    elif ans=="a3":
        birthday.T()
    elif ans=="a4":
        break