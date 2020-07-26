with open("homework_task_4.3.1.txt") as f:

    nums = []
    lines = f.readlines()
    for i in lines:
        i = i.strip()
        a = int(i[-1])
        nums.append(a)
        if a < 3:
            print (i)      
print('Average score: ', round(sum(nums)/len(nums)))