
import numpy as np

marks = np.array([
    [78, 85, 90, 88, 92],
    [70, 60, 65, 72, 68],
    [95, 90, 92, 98, 88],
    [50, 55, 60, 58, 52],
    [80, 82, 78, 85, 88]
])

flat = marks.flatten()
average = (np.mean(marks,axis=1))
percentage = (np.sum(marks,axis=1))
print("-----student marks analysis start-----")

print(f"The highest percentage of among all student {np.max(average)} ,(student{np.argmax(average)+1})")   #highest percentage of student

print(f"The minmum percentage of among  all student {np.min(average)} ,(student{np.argmin(average)+1})")    #minimum percentage of student

sub = np.max(marks,axis=0)

print(f"Highest marks in each subject: {sub} ")    #highest marks in each sub
print(f"Class average : {np.mean(marks)}")         #class average 
each_sub_avg = np.mean(marks,axis=0)          
print(f"The average marks in each subject is: {each_sub_avg}")   #average in each subject 


print("-----student analysis completed-----")

