import numpy as np
#row = student
#column = subjects
marks=np.array([[90,67,89,56,98],
               [56,54,78,97,34],
               [87,78,52,89,75],
               [89,56,23,74,15],
               [96,68,75,39,18]])
# student_wise avg,high,low mark 
avg=np.mean(marks,axis=0,dtype='int32')
print("Student_Average Mark:",avg)
max_mark=np.max(marks,axis=0)
print("Student_Highest Mark:",max_mark)
min_mark=np.min(marks,axis=0)
print("student_Lowest Mark:",min_mark)

#student_wise analysis
student_total=np.sum(marks,axis=1)
print("Student_total:",student_total)
student_avg=np.mean(marks,axis=1,dtype='int32')
print("Student_Average:",student_avg)

#subject_wise analysis
sub_avg=np.mean(marks,axis=0,dtype='int32')
print("Subject_Average:",sub_avg)

#top performer in total
top_mark=np.max(student_total)
print("Highest Mark:",top_mark)
               
#marks above 80
above_80=marks>80
print("Students scoring above 80 marks in each subject:",np.sum(above_80,axis=0))
