# Optimal Keyboard Layout

QWERTY Layout dominates the keyboard world currently. However, there exist many possible
layouts that have potentially higher performance than QWERTY. In this programming exercise, I will try to generate an layout that is optimized for movement speed for a 6 by 5 virtual keyboard utilizing the Fitts’ Law.

![equation](http://latex.codecogs.com/gif.latex?%24%24MT_%7Bij%7D%20%3D%20a%20+%20b%20log_2%28D_%7Bij%7D/W_%7Bij%7D%20+1%29%24%24)

Our goal is to minimize the average movement time given as:

![equation](http://latex.codecogs.com/gif.latex?%24%24t%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7BN%7D%5Csum_%7Bj%3D1%7D%5E%7BN%7DP_%7Bij%7DMT_%7Bij%7D%24%24)

One possible way to find the optimal layout is to first generate all possible layouts and then for
each layout, we compute the average movement time. However, this
brute-force approach is not computable since the number of possible layout (>10^26) is far
beyond our computing power. To tackle this problem, we use a kind of genetic algorithm- the
simulated annealing to approximate the optimal solution. The algorithm works like this:
Given a random starting layout, we randomly exchange the position of 2 keys. If the resulting
layout has lower average movement time, then we keep this layout and use this layout as the
starting layout for next iteration. After k iterations, if the average layout is not lowering anymore
by exchange 2 keys, then we stop and output the result.

# Execution

* Inputs:</br>
python optimal_layout.py 10000 100 words_100.txt
</br></br>
* Output:</br>
Optimal MT: 0.23658230722778248</br>Optimal Keyboard Layout:</br>k &nbsp;&nbsp; d &nbsp;&nbsp; z &nbsp;&nbsp; q &nbsp;&nbsp; 2</br>i &nbsp;&nbsp; n &nbsp;&nbsp; l &nbsp;&nbsp; c &nbsp;&nbsp; 3</br>t &nbsp;&nbsp; a &nbsp;&nbsp; s &nbsp;&nbsp; b &nbsp;&nbsp; x</br>h&nbsp;&nbsp; e &nbsp;&nbsp; r &nbsp;&nbsp; u &nbsp;&nbsp; p</br>v &nbsp;&nbsp; w &nbsp;&nbsp; o &nbsp;&nbsp; f &nbsp;&nbsp; j</br>g &nbsp;&nbsp; m &nbsp;&nbsp; y &nbsp;&nbsp; 1 &nbsp;&nbsp; 4
