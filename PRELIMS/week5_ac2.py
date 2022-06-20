##Queue
##Initialization
queue = []
queue.append("Holy")
queue.append("Angel")
queue.append("University")

print(queue)


s1 = []
q_size = int(input("Enter length of queue: "))
cntr = 0
for i in range(q_size):
    a = int(input("Value" + str(cntr+1)+" : "))
    s1.append(a)
    cntr+=1

print(s1)

q1 = [1,2,3,4,5]
print("Dequeue Item: ",q1.pop(0))
print("Q1 after dequeue: ",q1)

