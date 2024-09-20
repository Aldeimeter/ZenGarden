## Task 
A Zen garden is an area filled with coarser sand (small pebbles). 
However, it also contains non-movable larger objects, such as stones, statues, 
constructions, plants. The monk has to adjust the sand in the garden with a rake 
so that strips are formed as in the picture below.
![Alt text](/img/zen-s.png?raw=true "Zen Garden Example")

The tracks can only go horizontally or vertically, never diagonally. It always starts at the edge of the garden and pulls a straight strip to the other edge or to an obstacle. At edge - outside the garden he can walk as he wishes. But if it comes to an obstacle - a stone or sand that has already been raked - he must turn around if he has somewhere to go. If he has free directions left and right, it's up to him where he turns. If he has only one direction free, he turns there. If he has nowhere to turn, it's game over. A successful game is one in which the monk can rake the whole garden under the given rules, the case of maximum possible number of squares. The output is the coverage of a given garden by the monk's passes. 

For example, the coverage corresponding exactly to the first picture (intermediate state) is as follows:

<TABLE CELLSPACING=1 CELLPADDING=4 style='border-collapse: collapse; border: .5pt solid black;background: #e0ddbb;margin-left: 1cm;'>
<TR><TD>0</TD><TD>0</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #008'>10</TD><TD style='color: #008'>10</TD><TD style='color: #065'>8</TD><TD style='color: #06f'>9</TD></TR>

<TR><TD>0</TD><TD>0</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD style='background: #aaa'>K</TD><TD>0</TD><TD>0</TD><TD style='color: #008'>10</TD><TD style='color: #008'>10</TD><TD style='color: #065'>8</TD><TD style='color: #06f'>9</TD></TR>

<TR><TD>0</TD><TD style='background: #aaa'>K</TD><TD style='color: red'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #008'>10</TD><TD style='color: #008'>10</TD><TD style='color: #065'>8</TD><TD style='color: #06f'>9</TD></TR>

<TR><TD>0</TD><TD>0</TD><TD style='color: #f00'>1</TD><TD style='color: #f00'>1</TD><TD style='background: #aaa'>K</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #008'>10</TD><TD style='color: #008'>10</TD><TD style='color: #065'>8</TD><TD style='color: #06f'>9</TD></TR>

<TR><TD>0</TD><TD>0</TD><TD style='background: #aaa'>K</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #008'>10</TD><TD style='color: #008'>10</TD><TD style='color: #065'>8</TD><TD style='color: #06f'>9</TD></TR>

<TR><TD style='color: #d00'>2</TD><TD style='color: #d00'>2</TD><TD style='color: #d00'>2</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #008'>10</TD><TD style='color: #008'>10</TD><TD style='color: #065'>8</TD><TD style='color: #06f'>9</TD></TR>

<TR><TD style='color: #a00'>3</TD><TD style='color: #a00'>3</TD><TD style='color: #d00'>2</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='background: #aaa'>K</TD><TD style='background: #aaa'>K</TD><TD style='color: #065'>8</TD><TD style='color: #065'>8</TD></TR>

<TR><TD style='color: #700'>4</TD><TD style='color: #a00'>3</TD><TD style='color: #d00'>2</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #0e0'>5</TD><TD style='color: #0e0'>5</TD><TD style='color: #0e0'>5</TD><TD style='color: #0e0'>5</TD></TR>

<TR><TD style='color: #700'>4</TD><TD style='color: #a00'>3</TD><TD style='color: #d00'>2</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #70a'>11</TD><TD style='color: #0e0'>5</TD><TD style='color: #0c0'>6</TD><TD style='color: #0c0'>6</TD><TD style='color: #0c0'>6</TD></TR>

<TR><TD style='color: #700'>4</TD><TD style='color: #a00'>3</TD><TD style='color: #d00'>2</TD><TD style='color: #f00'>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD style='color: #70a'>11</TD><TD style='color: #0e0'>5</TD><TD style='color: #0c0'>6</TD><TD style='color: #090'>7</TD><TD style='color: #090'>7</TD></TR>
</TABLE>

## Assignment

Solve the above problem using the genetic algorithm. The maximum number of genes must not exceed half the perimeter of the garden plus the number of stones, in our example according to the first figure 12+10+6=28. The fitness is determined by the number of raked patches. The output is a matrix showing the paths of the monk. It is necessary for the program to handle at least the garden according to the first picture, but the input can in principle be any map.

