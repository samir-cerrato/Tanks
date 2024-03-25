# Tanks
Get familiar with dynamic programming design and development pt. 2

Task 2: Arrange tanks to eliminate enemies

2.1 Problem description

You have a queue of n tanks hidden in a forest. Due to the UAV of enemies, only 1 tank is used per
day, and the used tank can only be taken from the front or rear of the queue for some security reasons.
Each tank has a number indicating the number of potential units the tank can eliminate. Since tanks
are hurrily queued up during the night, you cannot organize the tank in the good order to use. Instead,
you have a queue of n values, each reflects the number of potential eliminated units for each tank in
the queue.

Since the war is more and more severe, the number of potential eliminated units dramatically increases
day-by-day. Let the labels of the number of eliminated units from n tanks in the queue be t1, t2, . . . , tn.

In the i-th day, the used tank k will eliminate i ∗tk units.

As a commander, for each day, your task is to give an order 1 or 0 corresponding to whether the front
or the rear tank in the queue is used. Write a program to compute the best order of using n tanks on
n days to eliminate maximum number of enemies’ units.

Since there might be several orderings that output the same number of eliminated units, you would
need to output the maximum number of eliminated units only.

2.2 Test case description

Your input will be a sequence of n integers, each value per line i corresponding to the amount of elimi-
nated units of the tank ti. The first and last lines correspond to the front and rear tanks, respectively.
Your output is an integer in range [0..2^31] corresponding to the maximum number of eliminated units.

Sample Input 1:

4

8

12

4

10

Sample Output 1:

128

The order is {1, 0, 0, 1, 1}, and the maximum number of detroyed units is 4 * 1 + 10 * 2 + 4 * 3 + 8 *
4 + 12 * 5 = 128. Note that for the last tank (#3), any order of 1 or 0 does not matter.

Sample Input 2:

1

9

1

9

8

8

7

7

Sample Output 2:

261

The maximum number of detroyed units is 261 and the order is {1, 1, 1, 0, 0, 0, 0, 1}. Note that for the
last tank (#4), any order of 1 or 0 does not matter.
