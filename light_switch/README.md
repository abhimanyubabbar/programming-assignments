## PROBLEM STATEMENT
A series of light bulbs is kept on display by the shopkeeper, where random bulbs are either switched ON or switched OFF.
Each bulb has its own switch to either turn it ON or turn it OFF.

Given the random state of N bulbs in the series and some constant K, the problem is to find out longest consecutive series of bulbs that appear ON, when K bulbs are switched from OFF state to ON state.
Any K bulbs from the series can be picked up.

The program should take input as :

T
N
K
arr[]

Where, T is the number of test cases that need to be run, followed by tuple (N, K, arr[]) for each test.
Where tuple for each test is,
N = Total number of bulbs in the series
K = Number of bulbs in OFF state that can be switched ON
arr[] = states of bulbs in the series, where 1 represents that the bulb is ON and 0 represents that the bulb is OFF.

Output: 
consecutive number of bulbs that appear ON
position/s of bulb

Example:

Input:

1
11
2
1 0 0 1 1 0 1 0 1 0 0

Output:
6
5 7

Constraints:

1 <= T <= 500
1 <= K <= 1000
1 <= N <= 10000

## SOLUTION
This problem is a classical example of window problems where a constraint needs to be maintained over an array. In this we need to maintain a window where we have constraints of maximum switches to be flipped and getting a consecutive streak of switched on bulbs.

We start by keeping track of left window pointer and right window pointer. In that window we calculate if we can maintain the constraint of having bulbs switched off less than or equal to the maximum allowed ( say K ). The whole window then becomes the maximum switched on bulbs. We move the pointer to the right to expand the window. If the constraint breaks, we shrink the window from the left. All this while we capture the best streak ( longest streak ) ever seen. If something bigger comes along we replace it.

## EXECUTE:
In order to execute the solution, we will provide the test cases in the input.txt and then run the main file `python3 light_switch.py`.