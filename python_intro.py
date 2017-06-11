print('Hello, Django girls!')

if 3 > 2:
    print('It works!')
else:
    print("nope")

volume = 57
if volume < 20:
     print("Je to dost potichu.")
elif 20 <= volume < 40:
     print("Jako hudba v pozadí dobré.")
elif 40 <= volume < 60:
     print("Skvělé, slyším všechny detaily.")
elif 60 <= volume < 80:
     print("Dobré na party.")
elif 80 <= volume < 100:
     print("Trochu moc nahlas!")
else:
    print("Krvácí mi uši!")

def hi():
     print('Hi there!')
     print('How are you?')

hi()

def hi(name):
     if name == 'Ola':
         print('Hi Ola!')
     elif name == 'Sonja':
         print('Hi Sonja!')
     else:
         print('Ahoj ' + name)

hi("Daniela")


girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    def hi(name):
     print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
     hi(name)
     print('Next girl')

for i in range(1, 6):
     print(i)
