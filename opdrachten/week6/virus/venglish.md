# Simulate with viruses

> This version has been automatically translated and will be reviewed for errors on Monday.

![](virus.jpg)

It is important for policymakers and the pharmaceutical industry to determine the success rate of a drug. Because many factors play a role, it is difficult to capture this probability in a mathematical formula, which is why simulations offer a solution. In this assignment you will **simulate** virus particles that can reproduce and die. We build this assignment step by step into a complete, but simplified simulation.

In this assignment we not only focus on the idea of ​​simulation, but you will also test your code more extensively than before. At each intermediate step you will find instructions for a function that you are going to implement. The explanation always contains a heading "Testing", with instructions on how you can check whether your position meets the expectations. These directions are not complete! It is possible that you run into problems that are not checked because of this. So you should also practice thinking about potential problems for yourself. In any case, keep an eye on the goal: to prevent mistakes from **piling up**. If an error only shows up at the very end, it is much more difficult to find the true cause.

So do this assignment step by step, including testing!

On the other hand, "list comprehensions" play a major role in this assignment. To give extra motivation to use these, there is a **limit** for the number of lines of code that may be used for the solution for assignments. Doesn't that work? First make your solution (if possible) working without list comprehensions and ask the assistants for help with converting to list comprehensions.


## Step 1: Virus Genome

DNA is a strand containing particles called nucleotides. Each DNA molecule actually consists of two strands of such nucleotides, which are additionally linked together at each nucleotide. The connected nucleotides are called base pairs. Because these pairs always occur in fixed combinations, it is sufficient to specify the names of the nucleotides of one strand when typing a DNA double strand. The names are: adenine (A), cytosine (C), guanine (G) and thymine (T). In any human cell, the DNA strand is made up of billions of such base pairs. Many viruses are also made up of exactly the same types of cells.

(Disclaimer: we are not biologists and coronaviruses are RNA viruses and not DNA viruses :-))

### Hints

*   Add these lines at the top of a `virus.py` file:

        import random
        import string

*   Write a function `generate_virus(length)`.

    * This function takes one argument, `length`, which is an integer representing the length of the virus genome.

    * The function must return a string consisting of an arbitrary sequence of nucleotides.

*   Oh, and one more thing: you can only use **one line of code** for this function.

*   Use a list comprehension and the `"".join()` method of a string.

*   Take a look at the `random.choice()` function.

### Testing

Manually create and print viruses of different lengths to verify that they are correct. If you wrote the function in a `virus.py` file, you can run Python **interactive** to test:

    $ python3 -i virus.py
    >>> generate_virus(4)
    'AATC'
    >>> generate_virus(4)
    'TCBT'

The outcome is of course random, so check carefully whether the genomes that are made do indeed differ. Also check that after a few spins you can see all the nucleotides passing by.

Testing interactively is great as a quick check, but as soon as the results seem reasonable you must get started writing doctests!

Writing doctests for a function with random output works differently than for "deterministic" functions. Here are some ideas:

*   You can test **properties** of the output, for example:

    *   The length of the output: `len(generate_virus(3))` must be 3.

    *   The output type: `type(generate_virus(0))` must be `str`.

*   You can give the `random` module a ["seed"](https://docs.python.org/3/library/random.html#random.seed) so that the results are no longer really random. This way you can still test the outcome of a function. Make sure you call the `random.seed` in the test, so that the function always works randomly in normal situation. An example of a concrete doctest:

        >>> random.seed(0)
        >>> generate_virus(4)
        'CCGA'

*   You can test the function **serially** by using a list comprehension and then seeing if the output always has a certain property:

        >>> all([len(generate_virus(x)) == x for x in range(8)])
        true

    *   With the list comprehesion we test the function generate virus 8 times, and the list is filled with the results of these tests (True, False).

    *   We use the Python function `all(...)` which checks from a list whether it returns `True` everywhere.


## Step 2: Mutate

Once a virus is born, it has a chance to mutate.
Mutation is changing one random nucleotide for another randomly.
For example from `AGTC` to `ATTC`.

### Hints

* Write a function `mutate(virus)`.

    * This function accepts one argument, `virus`, a string of nucleotides.

    * The function must return a string consisting of the same nucleotides, one of which is mutated.

* No rule limit this time, but if you want to challenge yourself: 3 (or less) rules is possible.

* A change after which the result is the same does not count as a change.

    * You may **not** solve this problem by making random mutations until one succeeds. The mutation must give a valid result in one go.

* Look at the `random.randrange()` function!

* Use list slicing (see your book).

### Testing

* Check if the `mutate` function always changes the virus. For example, you could create a large number (1000) viruses and mutate them. Is every virus different after the mutation?

* Check whether the length of the virus always remains the same after mutation.

* New test strategy: also look at the **edge cases** for this type of function. What happens when `mutate` is called with an empty string? Test this property as well. (An emtpy string is not really a virus of course, but at least you do not want an empty string to contain virus elements after mutating!)


## Step 3: Die off

In the previous two steps, we worked with individual viruses. We have represented it as a string. For our simulation we will be working with a large amount of viruses. To represent such a population we can make a **list** of viruses. That could look like this:

    ['ACTG', 'AGAA', 'ACCG', 'GTCA']

We will now continue to work with this structure.

Virus particles can die. They don't all die at once, but every time step every virus has a chance to die. With the following function we are going to simulate this event.

### Hints

* Write a function `kill(viruses, mortality_prob)`.

    * This function accepts the `viruses` argument, which is a list of virus genomes.

    * And an argument `mortality_prob`, a float between 0 and 1 (inclusive) that represents the probability of death per virus particle.

* The function should return a **new** list containing the virus genomes that survived.

* Note: each virus genome has an independent chance of dying. So with a `mortality_prob` of 0.2 on average 80% of the virus population survives, but this can certainly fluctuate at a time!

* You are allowed to use **one line of code** here, so use a list comprehension!

### Testing

* Consider how many viruses should be left on average after this feature. Note that there is a lot of randomness in this feature, so don't be surprised if it's a little bit above or below it. Test that property.

* Don't just test your function with values ​​in the middle, but also look for the edge cases. Is what happens if I set the chance of death to 0 or 1?


## Step 4: Reproduction

A virus has a chance to propagate at any time step in the simulation.
When a virus reproduces, the child has exactly the same DNA string as the parent.
There is a chance that a mutation will occur: then one base pair is different.

* For reproduction, write a function `reproduce(viruses, mutation_prob, reproduction_prob)`.

    * This function accepts `viruses`, a list of virus genomes.

    * And `mutation_prob`, a float between 0 and 1 (inclusive) that represents the probability of mutation in the child virus particle.

    * And also `reproduction_prob`, a float between 0 and 1 (inclusive) that represents the probability of reproduction per virus particle.

* The function must return the list of the entire population of virus genomes. That includes the parents!

* Please note that each virus genome has an individual chance to reproduce. So at a `reproduction_prob` of 0.2 on average 20% of the population reproduces, but this can fluctuate!

* No rule limit, but if you want to challenge yourself: 2 rules is possible.

### Testing

* As with previous function, check that this function returns approximately the expected number of viruses.

* Check whether viruses have actually mutated and whether this is happening with approximately the right amount of children.


## Step 5: Resistance

![](medicine.png)

Before we can start simulating, we add a virus inhibitor to our simulation.
Viruses can be resistant to such an inhibitor; during reproduction a mutation can cause the resistance to develop. A resistant virus (in this simulation) is any virus that has `AAA` in the DNA strand.
Once the drug is introduced, all viruses except resistant viruses can no longer reproduce.

* Write a function `is_resistant(virus)`.

    * This function takes one argument, `virus`, which is a virus genome.

    * The function must return a boolean indicating whether the virus is resistant (`True`) or not (`False`).

* A virus is only resistant if `AAA` occurs consecutively.

### Testing

Test this feature on different viruses to see if it recognizes the resistant viruses as well as the non-resistant ones.


## Step 6: Reproduction Opportunity

The more virus particles present, the smaller the chance of reproduction:
there is simply not enough room for all the virus particles.
There is a negative linear relationship between the number of viruses and the chance of reproduction.
The probability of reproduction is equal to `(1 - (size_of_virus_population / maximum_number_viruses)) * maximum_reproduction_probability`.
The function to calculate the probability per individual virus particle in a population can be found below:

    def reproduction_probability(viruses, max_reproduction_prob, max_population):
        return (1 - (len(viruses) / max_population)) * max_reproduction_prob if max_population > 0 else 0

Include this function in your elaboration and provide the definition of the correct types.


## Step 7: Simulate with a virus inhibitor

In the steps above, we worked on a **representation** of viruses (as strings) and populations (as lists). Now that we have such a representation for viruses, can make them mutate, die, reproduce, and be resistant, we can start simulating.

The simulation works as follows. During each time step:

* let's kill viruses first,
* then we calculate the production probability, and
* then let's reproduce them.

**But** from the 100th time step we add a virus inhibitor to the simulation, and then only resistant viruses can reproduce.

### Hints

* Write a function called `simulate(viruses, mortality_prob, mutation_prob, max_reproduction_prob, max_population, timesteps = 500)`.

* This function takes five arguments, and one optional argument:

    * `viruses` is a list of virus genomes.
    * `mortality_prob` is a float between 0 and 1 (inclusive) that represents the probability of death per virus particle.
    * `max_reproduction_prob` is a float between 0 and 1 (inclusive) that represents the maximum probability of reproduction per virus particle.
    * `max_population` is an integer for the maximum population size.
    * `mutation_prob` is a float between 0 and 1 (inclusive) that represents the probability of mutation upon reproduction.
    * `timesteps` is an integer and an optional argument that specifies the number of timesteps in the simulation.

* The function must return a list containing the population size (an integer) at each time step.

### Pseudocode

Below is the pseudocode for the `simulate` function. Look at it carefully, because the order of the different steps in the simulation is important. For example, different results may be obtained if the viruses first reproduce and then die.

     1 function simulate
     2 let population_sizes be a list
     3 for every timestep t
     4 kill viruses
     5 calculate reproduction probability
     6 if timestep t >= 100
     7 reproduce only viruses that are resistant, while keeping all other
     8 else
     9 reproduce any virus in the population
    10 add resulting size of population to population_sizes
    11 return population_sizes

### Testing

For this assignment it may be a bit more difficult to come up with tests yourself. That's why we already have two.

*   The first checks whether the result from `population_sizes` indeed consists of exactly 501 elements (500 time steps plus the initial situation).

        >>> viruses = [generate_virus(4) for _ in range(100)]
        >>> len(simulate(viruses, 1, 0, 0, 0))
        501

*   The second checks whether, given those variables, the simulation gives the correct results.

        >>> sims = []
        >>> n = 100
        >>> for i in range(n):
        >>> viruses = [generate_virus(4) for _ in range(100)]
        >>> sims.append(simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 1000)[-1])
        >>> average = sum(sims) / n
        >>> 23 < average < 32
        true


## Final steps: graphs

Below you will find code for creating graphs based on your self-written functions. You don't have to change anything in the code below. This is of course the ultimate test: it will only work if all the above functions are implemented exactly according to the specification.

Create an `if __name__ == '__main__'` for your program and put the following import into it:

    import matplotlib.pyplot as plt

So **don't** put this import at the top of your program because it is only needed for the plots you make in the main.

Then copy the following pieces of code one by one into the main to see what comes out. If `matplotlib` does not work properly (error messages), it is best to ask for help or look up the error message on the internet.

Look through the code to see if you understand what's happening. The functions of the `matplotlib` library are simple, but most of them have very cryptic names. Optionally, you can check the documentation of matplotlib to see what the function does. And if you're interested and still have time, try adding another interesting chart yourself!

### Graph of one simulation

Below is a graph of one simulation of your function! This graph shows the course of the simulation over time. You can start your program multiple times to view different graphs.

    # outcome of the simulation
    simulate_result = simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 500)

    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes()

    # plotting the data
    ax.plot(range(501), simulate_result)

    # layout of the chart
    plt.title('Simulation')
    plt.xlabel('Timestep')
    plt.ylabel('Number of viruses')
    plt.ylim(0.110)
    plt.xlim(0.500)

    plt.show()

### Graph of multiple simulations

As you may have noticed from the graph above, the result varies quite a bit. We can also run the simulation several times and plot everything in one graph. Then you can see that there are more or less two ways in which the simulation can run.

    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes()

    # run twenty simulations
    for i in range(20):
        simulate_result = simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 500)

        # add the result of a simulation as a line
        ax.plot(range(501), simulate_result)

    # layout of the chart
    plt.title('Simulations')
    plt.xlabel('Timestep')
    plt.ylabel('Number of viruses')
    plt.ylim(0.110)
    plt.xlim(0.500)

    plt.show()

So in a large part of the simulations, the virus gets a big dent from the virus inhibitor, but then recovers and stays at the same level until the end of the simulation. In a smaller number of the simulations, the virus inhibitor works so well that the virus soon disappears.

### Healed/unhealed

As a final graph, we will look at how many cases the virus inhibitor has been successful in.

    cured = 0
    # number of cured simulations
    n_simulations = 100

    # run the simulation 100 times, and keep track of how many of them are healed
    for i in range(n_simulations):
        simulate_result = simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 500)
        # if the last time step does not contain viruses, the person is cured
        if simulate_result[-1] == 0:
            cured += 1

    labels = 'Cured', 'Not Cured'
    sizes = [cured, n_simulations - cured]

    # making the pie chart
    fig1, ax1 = plt.subplots(figsize=(8, 8))
    ax1.pie(sizes, labels=labels, autopct='%1i%%',startangle=90)
    ax1.axis('equal')
    plt.title('Pie chart of cured and non cured simulations')
    plt.show()


## Valve

So much for **Virus**. Hopefully you had a nice introduction to making simulations. Because you can never simulate the complete situation, the trick is to look for a good combination of factors that you can take into account. That is why making good simulations is a [field](https://uva.computationalscience.nl) in itself!
