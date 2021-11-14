# Flow Traders: CRACK THE CODE! 3.0

![](/img/hero.png)

Code written for [Flow Traders "Crack The Code 3.0"](https://www.flowtraders.com/crackthecode) challenge.

## Problem description
The duration was 90 minutes (that's why my code is so raw ✨)
The problem was formulated as a short story. It required me to develop a program able to manage 2 commands:
- add ID: added the element with id=ID to the queue
- move: remove the first element from the queue

Before every "move" command, the queue MUST be sorted in order to assure to remove the element with the lowest id
### INPUT
N lines where each line should contain one of the two commands
### OUTPUT
Print the lowest number of sorting operations needed

## Solution
The tricky part of the problem was to solve it with a good Time complexity.
I personally developed to solutions:
- version1: is the (almost) brute force approach. Time complexity (m*nlogn)
- version2: uses a minHeap in order to keep the element in the queue always sorted. 
    - Cost of the extractMin() --> logn
    - Cost of the insert() --> logn
    - Total Time complexity (nlogn)