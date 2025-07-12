

# K-D trees

- Pick a dimension say x- do that randomly or in round robin fashion.
- find the median of all teh points along x dimension
- when you get the median the divide the data into parts
- repeat teh procedure for other dimensions and divide the space.
- We have divided the data into many partitions. 
- We then find teh given point in the newly made partitions and find the KNN in that partition only

As a consequence of less time ... we may have to do trade offs which leads to accurary loss but what can we do to mitigate such problems.


Time complexity analysis
How much time does it take to create a tree like structure. 
log$_2$n   is the time requred to spit n points in the groups and for finding the median at each stage we need to sort the array NlogN and find the median for logN levels.
Total time required to built the tree is O(nLogn 2)


What time does it take to do the query O(logN + SD)


# Locality Sensitive hashing





|--------------|----------------|-----------|----------------|
|       Date         |   Day               |    Subject   |    Time Slot   |
|--------------|--------------|------------|-----------------|

| Date | Day      | Subject | Time Slot             |
| ---- | -------- | ------- | --------------------- |
| 23   | Saturday | ML      | 9-11:30    (Jasubhai) |
| 28   | Saturday | DM      | 2-4:30   (1/103)      |
| 24   | Sunday   | Biology | 9-11:30    (Jasubhai) |
| 24   | Sunday   | DSA1    | 2-4:30   (Jasubhai)   |
