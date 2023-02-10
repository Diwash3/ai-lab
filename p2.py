import random
def display(room):
    print(room)
    
a = int(input("Enter no. of rows:"))
b = int(input("Enter no. of columns:"))
room = [[1 for _ in range (b)]for _ in range (a)]
print("All  the rooms are dirty")
display(room)
x=0
y=0
while x<a:
    while y<b:
        room [x][y] = random.choice([0, 1])
        y +=1
    x +=1
    y=0
    
print("Before cleaning the room I detect all of these random dirts")
display(room)
x=0
y=0
z=0
while x < a:
    while y < b:
        if room[x][y] == 1:
            print("Vaccum in this location now,",x, y)
            room[x][y] = 0
            print("cleaned", x, y)
            z+=1
        y+=1
    x+=1
    y=0
pro= (100-((z/(a*b))*100))
print("Room is clean now, Thanks for using")
display(room)
print('performance=',pro,'%')
