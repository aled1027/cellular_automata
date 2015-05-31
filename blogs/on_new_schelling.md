
# New CA models influenced by Schelling

The questions: 
- how do agents simultaenously react to and construt their environment?
- what is the relationship between agent and overall system?
    - in particular, how much "agency" does a single agent have in the overall system?
        - is there a way to answer this question that isn't just asking "how robust is the system given the loss/gain of an agent?"
        - I think it is different than that.
        - global responsibilty; local action
- Can we create a CA which has a system metric that is dynamic?
    - the metric can be high, and then move, and then high
    - i.e. the metric never reaches a point of equilibrium.
- How can we move the CA away from the 2-d board to mathematical graph?

We call schelling's model, "nearest".
We call schelling's model with the random walk "random-walk".
We call schelling's model where agents move to uniform random position, "unif-random".

Each model needs global metrics. 
In Schelling's model, these metrics are
- average similarity (aka amount of segregation)
- average happiness

## Threat-Vuln Model
1. There is 1 type of agent.
2. Each agent has two real values assigned to it: agent.threat and agent.vuln
3. Define get_neighbors however you want. Call its return value neighborhood.
4. On agent.update():

    1. ` nbr_threat = sum([nbr.threat for nbr in self.neighborhood])`
    2. ` if nbr_threat <= self.vuln then self.is_happy = True else self.is_happy = False`
    3. And update the agents threat based on its neighbors. `self.threat += function(nbr_threat)`

The change of schelling's model is that in addition to being happy or sad based on their environment, agents also change how they affect the agents around them.
Perhaps one way to think about it is that we are also updating the race of agents.

## Supply-Demand model
1. each agent has supply, demand, money
2. agents sell and buy goods basd on this. 
3. see what happens

## Power Model
1. There is 1 type of agent.
2. Each agent has `agent.power, agent.desired_power, agent.is_happy`
3. ``
    agent.update():
        nbr_power = sum([nbr.power for nbr in neighbors])
        cur_ration = nbr_power / self.power
        if cur_ratio < self.desired:
            do something
        else:
            do something else
    ``
This is supposed to model power dynamics in society.
Some people don't necessarily want to make a lot of decisions but others do.
TODO add better explanation.

## Leaving the 2-d board
One limitation of cellular automat is that you are stuck on a 2-dimensional board. 
This isn't really reflective of the world, so maybe there's a way around it. 
I propose that instead of putting agents in a 2-d array, i.e. a board, we instead use a Laplacian matrix to represent relations among agents. 

If there are $n$ agents, then the laplacian would be an $n \times n$ matrix. 
The entry in the $i$th row and $j$th column would represent how "close" the $i$th agent is to the $j$th agent.

The 2-d board is actually a special case of the Laplacian.
Most of the entires are zero, but a particular few are 1s. 
Each row and columns would have $8 1$s and the diagonal would be all $0$s.
