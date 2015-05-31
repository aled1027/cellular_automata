The use of we is a formality I like. 
When really just means that I did it or think it.

When I use the word racism here, you can substitute any of form of discrimination in and the statement still applies. 
I use racism because it's concrete and easier to explain.

This blog post is a summary of a research paper I did on Schelling's Cellular Automata model. 
Before you decide now that you don't want to read this, I will go over ideas relating, but not limited, to:
- cause and effects of racism
- cause and effects of discrimination in general
- the relationship between an individual and all of society
- to what extent can an individual affect society

First, let us begin by presenting cellular automata. 
Cellular Automata are a type of computer simulations that consists of a grid of cells, where each cell can be either on or off. 
It's easiest to picture an 8 by 8 checkerboard where each cell is either white or black (we generally think of a white cell as being dead and a black cell as being alive). 
Cellular Autaomta then assign rules to the cell. 
These rules govern whether the cell is going to be a live or dead next based on the compositions of its neighbors, the 8 blocks surrounding the cell.

The most well known cellular automata is called Game of Life.
The rules of Game of Life are simple: 
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overcrowding.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction (wikipedia)

Game of Life is interesting because the rules give rise to really cool patterns.
Given the right starting configuration of alive and dead cells, you can create oscillating patterns, patterns that move around the board, a pattern that acts as a gun (it shoots out live cells), and so forth. 
Combining these patterns, we can actually prove mathematically that a cellular automaton with the rules of Game of Life can do anything that a computer can do. 
It can perform any computation: sort a list, multiply numbers, and if it were hooked up to the internet, it could have the internet on it.
Anything a computer can do, Game of Life can do. 
And vice versa. 

We can also use cellular automata to think about people and relations among people.
Since we can simulate the cellular automata model on a computer, we can see how the people act given different rules. 
This is what Schelling did in the 1970s with discrimination.

Schelling took an 8 by 8 grid (thinka checkboard) and randomly put dimes and pennies on it. 
He then said that if at least 1/3 of a given coin's neighbors are like themself (the same type coin), then that coin is happy; and otherwise the coin is sad. 
Then the rule is that one by one, we randomly pick a sad coin, and move them to the nearest empty cell such that they are happy.
What we find is that eventually there is segregation. 
There are clusters of predominantly dimes, and clusters of predominantly pennies. 

Let us relate this model to society.
We can think of the dimes as one group of people, and the pennies as a different group.
For example, say the dimes are black people and the pennies are white people. 
Then, each race doesn't like to be surrounded by people that don't look the same as them.
If a black person moves into a neighborhood where more than 2/3 of their neighbors are white, they are less comfortable (less happy) than if a white person lived in the same spot.
Therefore that black has a tendency to move. 

What we then see is that because of this, perhaps natural, tendency to not want to be totally surrounded by people that different than us, we get segregation on the system level.
Even if we hold all else equal - there is equal pay among the people, equal schools, equal opportunity, and no degradation of other races, no "mean" discimination - we simply say that people don't like it when more than 2/3 of the people around them are different, then we see segregation.

This is huge. 
We're not saying that socioeconomic inequality, historical advantage, hiring preferences and other issues don't contribute to segregation and racism - they most certainly do - but perhaps at the core, there is something simpler happenning. 
We are each, not to our own fault, or to society's fault, slight racist.
And when we are all slightly racist, then we get huge emergent segregation, and probably consequently racism, on the macro level. 

Most importantly, the amount of segregation on the macro level is not of the same degree or proportion as the racism on the micro level.
If we are 33% racist on the micro level, then on the macro level we see approximatley 80% segregation. 
80% segregation means that each person is similar to at least 4/5 neighbors - a much greater number than 1/3.

So what should we make of this?

We find the following ideas compelling.

1. Racism, and other forms of discrimination, are really hard to stop once they get doing.
    In the model, once there is a predominantly white neighborhood, all of those white people are happy.
    They have no impetus to move.
    In a sense, segregation is irreversible without new, incentives.

2. Racism begins with the individuals.
    In Schelling's model, there is nothing about person being indoctrinated with racist attitudes, or a biased against those different than they are.
    And the amont of segregation and racism on the macro level has no effect on an individual's attitudes. 
    The segregation in the model is purely the result of individual attitudes.

3. Racism does not stem from inequality.
    Both races were equally racist, had equal income, were equal in all ways. 
    And yet, we still observed segregatoin.

4. Add more?

TODO add link to the shapes page.
TODO explain what the shapes page is doing wrong.

TODO define the word "agent" and agents

So that was Schelling's paper. 
My research into Schelling's model was to look at how changing the movement procedure changed the results of the model.
In Schelling's orginal model, the agents move to the nearest cell such that they are happy.
This means that model is deterministic - agents always move to the same place.
Also, it means that agents have a tendency to stay close to home.

The problem with the model being deterministic is that it may not be modeling society that well.
As behavioral economists and psychologists have shown, we are not the most rational people, so we may not move to the nearest place such that we are happy.
Moreover, for some reason or another, we may want to move farther away sometimes. 

To change this problem, we had the unhappy agents take a random instead of moving directly to the nearest such that they are happy.
A random walk is ...

TODO define random and explain random walk

TODO results of my model

TODO changing preferences

TODO changing the length of the random walk to model socioeconomic inequality

For comparison, the shapes simulation (link: ) has agents move to random cells such that they are happy.

The results in all three models - nearest, random walk, unif-random - demonstrated segregation after a period of time, given that the agents were sufficiently bias.
This suggests to me that the core of Schelling's model is not the movement procedure of the agents but the fact that agents can be happy or sad and react to it. 
The agents don't even need to react rationally, as demonstrated by the random walk and the unif-random model. 


























