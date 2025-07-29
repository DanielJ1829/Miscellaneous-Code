import time
import math
import numpy as np
import matplotlib.pyplot as plt
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

'''
this code attempts to:
1) provide two prime number generation methods (by using a sqrt(n) order function and the sieve of eratosthenes)
2) produce a list of prime numbers up to a user-defined bound, and print upon request
3) return the time taken for each algorithm, allowing for efficiency comparisons
4) plot the prime distribution alongside the prime-number theorem approximation function and the error at the last prime before
the user defined bound. The plot also computes the average prime spacing in the legend
5) Produce arrays of twin primes, cousin primes and sexy primes, plotting their frequencies graphically
6) Return further arrays of prime gaps, based on user request - limited to 5
7) Produce plots of requested prime gaps as subplots
8) (Possibly) return prime prime triplets upon user request
9) Provide prime factorisations of large numbers based on user input -> can extend this a lot into how many prime factorisations each number needs,
could look really cool once you reach large numbers
10) Extend the project so that it can do much more in terms of number theory; this could be various things that are computationally complicated
this could be calculating things, working out what the day will be in x minutes/months and so on, just yeah, make this the place for various ideas
so that a lot of computationally complex stuff can be put here (ideas here: a) factorials and extended choose functions/combinatorics, b)
11) Have a navigatable user input interface that guides you through what the code does, and lets you choose whether you want
prime visualisation, prime factoring and other features
'''


def generate_prime_list(upper_bound, info):
    start = time.time()
    primes = []
    if upper_bound >= 5:  #appends 2,3 and 5 to the list to then eliminate their multiples later on (a bit like a sieving process lmao)
        primes.append(2), primes.append(3), primes.append(5)
    elif upper_bound < 5 and upper_bound >=3:
        primes.append(2), primes.append(3)
    elif upper_bound < 3 and upper_bound >=2:
        primes.append(2)
    for number in range(2, upper_bound):
        if int(str(number)[-1]) % 2 == 0 or int(str(number)[-1]) == 5 or sum(map(int, str(number))) % 3 ==0:   #eliminates 2,3 and 5 bc of divisibility tests, map here sums all numbers in the string
            prime = False
        else:
            prime = True #assumes all numbers in the list are prime to then eliminate ones that aren't
            for i in primes:
                if i > math.isqrt(number):  #tests all numbers up to the square root
                    break
                if number % i == 0:         #if any i up to a number's square root divides it you can eliminate it since it's then not prime
                    prime = False
            if prime:
                primes.append(number)       #append remaining cases
    end_time = time.time()
    total_time = end_time - start
    if info == 'yes':
        print(f'there are {len(primes)} in this interval and it took {total_time:3.2f} seconds to generate.')
    while True:
        y = input("Would you like the list of primes? Please enter 'yes' or 'no': ").strip().lower()
        if y == 'yes':
            print(primes)
            break
        elif y == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        return primes
def sieve_of_eratosthenes(upper_bound, info):
    start_1 = time.time()
    primes = []
    is_prime, is_prime[0], is_prime[1] = [True]*(upper_bound+1), False, False
    for i in np.arange(2, int(math.isqrt(upper_bound))+1, 1):
        if is_prime[i]:
            for j in np.arange(i*i, upper_bound+1, i):
                is_prime[j] = False
    for i in np.arange(2, int(upper_bound)+1, 1):
        if is_prime[i]:
            primes.append(int(i))
    end_1 = time.time()
    total_time = end_1 - start_1
    if info == 'yes':
        print(f'there are {len(primes)} in this interval and it took {total_time:3.2f} seconds to generate.')
        while True:
            y = input("Would you like the list of primes? Please enter 'yes' or 'no': ").strip().lower()
            if y == 'yes':
                print(primes)
                break
            elif y == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    return primes
def info():
    while True:
        y = input("Would you like the results? Please enter 'yes' or 'no': ").strip().lower()
        if y == 'yes':
            break
        elif y == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return y
def retrieve_upper_bound():
    while True:
        n = input('enter a number to search for primes up to:').strip()
        try:
            n = int(n)
            break
        except ValueError:
            print('Please enter an integer')
    return n
def compute_twin_primes():
    '''
    :returns: an array of twin primes up to the user defined bound
    '''
    twin_primes = []
    for i in np.arange(0, len(primes)-1, 1):
        if primes[i+1]-primes[i] == 2:
            twin_primes.append([primes[i], primes[i+1]])
    return twin_primes
def compute_cousin_primes():
    '''
    no arguments
    :returns: an array of cousin primes up to the user-defined upper bound
    '''
    cousin_primes = []
    for i in np.arange(0, len(primes)-2,1):
        if primes[i+2]-primes[i+1] == 4:
            cousin_primes.append([primes[i+1],primes[i+2]])
        elif primes[i+2]-primes[i] == 4:
            cousin_primes.append([primes[i], primes[i+2]])
    return cousin_primes
def compute_sexy_primes():
    '''
    :return: computes all sets of primes with a gap of 6 between them
    '''
    sexy_primes = []
    for i in np.arange(0, len(primes)-3, 1):
        if primes[i+3]-primes[i+2] == 6:
            sexy_primes.append([primes[i+2], primes[i+3]])
        elif primes[i+3]-primes[i+1] == 6:
            sexy_primes.append([primes[i+1], primes[i+3]])
        elif primes[i+3]-primes[i] == 6:
            sexy_primes.append([primes[i], primes[i+3]])
    return sexy_primes
def compute_uber_differences():
    '''
    :returns: an array of the differences between all the primes. needs further work to actually output the pairs that
    do this. Note however that this has NO duplicates and covers the differences between all primes.
    this function alone can be used to tell us the cardinalities of certain prime groups efficiently,
     allowing for efficient analysis
    '''
    uber_differences = []
    for i in np.arange(1, len(primes), 1):
        x=[]
        for j in np.arange(0, len(primes)-i, 1):
            x.append(primes[-i]-primes[j])
        x.reverse()
        uber_differences.append(x)
    uber_differences.reverse()
    return uber_differences
def define_gap():
    while True:
        gap = input('Enter the desired prime pair gap: ')
        try:
            gap = int(gap)
            if gap % 2 != 0 or gap == 0:
                raise Exception
            return gap
        except ValueError:
            print('Please enter an integer')
        except Exception:
            print('Please only enter even integers')
def produce_desired_gap_array(gap):
    '''
    :returns an array of prime number pairs, with each pair differing by a user defined number (this typically is even)
    '''
    desired_gap = []
    for i in np.arange(1, len(primes), 1):
        for j in np.arange(0, len(primes)-i, 1):
            if primes[-i]-primes[j] == gap:
                desired_gap.append([primes[j], primes[-i]])
    desired_gap.reverse()
    return desired_gap
#next few problems: trying to output multiple of these gaps. converting the pairs into something i can plot
# the multiple gaps problem is hard. Upon user request, we want to get multiple of these arrays
#i've got the gaps bit right. I just need to now work out the next part
#I need to ask the user: Do you want: twins, cousins, sexies, then: do you want a user defined gap, then reask this 5
#times over, allowing the user to exit at any given opportunity. Then, I need to find a way of subplotting these graphs.
#I will remove the user's option to choose which ones they plot. Either they can have nothing, arrays of each one,
#the plots or both.
#I could also try and save the pairs of primes as a csv file.
def first_gaps_request():
    prime_gaps = ['Twin Primes', 'Cousin Primes', 'Sexy Primes']
    first_gaps = [None, None, None]
    for i in np.arange(0, len(first_gaps), 1):
        while True:
            response = input(f"Would you like to generate the list"
            " of {0}? Please enter 'yes' or 'no': ".format(prime_gaps[i])).strip().lower()
            if response in ['yes', 'no']:
                first_gaps[i] = response
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    return first_gaps
def produce_custom_gaps():
    '''
    :returns: arrays of prime pairs
    '''
    further_gaps = []
    for i in np.arange(0, len(colors), 1):
        while True: #new list loop
            response = input('Would you like to generate another list of prime pairs?' ).strip().lower()
            if response == 'yes':
                while True: #input loop
                    gap = input('Enter the desired prime pair gap: ')
                    try:
                        gap = int(gap)
                        if gap % 2 != 0 or gap == 0 or gap in further_gaps:
                            raise Exception
                        else:
                            further_gaps.append(gap)
                    except ValueError:
                        print('Please enter an integer')
                    except Exception:
                        print('Please only enter unique, positive, even integers')
                    break #breaks out of input loop
                break # breaks out of new list loop to rerun whilst in the range
            elif response == 'no':
                return further_gaps[:i]
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    return further_gaps
def get_custom_arrays(further_gaps):
    time_i = time.time()
    further_arrays = []
    for i in np.arange(0, len(further_gaps), 1):
        while True:
            try:
                if further_gaps[i] > 0:
                    further_arrays.append(produce_desired_gap_array(further_gaps[i]))
                    break
            except:
                break
    while True:
        try:
            if further_gaps[0] != [0]:
                print_the_arrays = input('Would you like to see the arrays? ').strip().lower()
                if print_the_arrays == 'yes':
                    print(further_arrays)
                    break
                elif print_the_arrays == 'no':
                    break
                else:
                    print('Invalid input. Please enter yes or no')
        except:
            break
    time_j = time.time()
    print('the time taken was {}'.format(time_j - time_i))
    return further_arrays
#can use get_graph() or info (they do the same thing lmao) to now plot these graphs. The main issue is not this tho.
#def array_average():
def compute_mean(array):
    x = []
    for i in array:    #can do this in a clunkier way (for i in np.arange(0, len(array), 1) -> l = int(array[i][0]-..))
        l = int((i[0]+i[1])/2)
        x.append(l)
    return x
def produce_means():
    further_means = []
    for i in np.arange(0, len(further_gaps), 1):
        means = compute_mean(further_arrays[i])
        further_means.append(means)
    return further_means
def construct_dictionary():
    dictionary = dict()
    for i in np.arange(0, len(further_gaps), 1):
        dictionary[f"Primes with gap {further_gaps[i]}"] = further_means[i]
    return dictionary
def get_graph():
    while True:
        plot_the_graph = str(input('plot this graphically? (yes/no) ')).strip().lower()
        if plot_the_graph == 'yes':
            break
        elif plot_the_graph == 'no':
            break
        else:
            print('Please enter yes or no.')
    return plot_the_graph
def factorise_number(x):
    while True:
        n = input('enter a number to factorise:').strip()
        try:
            n = int(n)
            break
        except ValueError:
            print('Please enter an integer')
        try:
            n < x**2
            break
        except ValueError:
            print("Please enter an integer smaller than the upper bound's square root.")
    factors = []
    for i in np.arange(0, len(primes), 1):
        if n%primes[i] == 0:
            factors.append(primes[i])
        else:
            pass
    if len(factors) == 0:
        print('this number is prime')
    else:
        print('this number has prime factors {}'.format(factors))
    factorisation = []
    indexes = []
    for i in np.arange(0, len(factors), 1):
        m = x/factors[i]
        z = 1
        while m/factors[i] == int:
            z += z + 1
            m += m/factors[i]
        factorisation.append(m)
        indexes.append(z)
    print(indexes)
    print(factorisation)
    return factors

#this code can: generate a list of primes (1), display how long it took (2), produce the prime list (3), plot the graph (4)
#produce arrays of prime pairs (5), print them (6), plot them (7), or find the prime factors of a number (8)


n, y = retrieve_upper_bound(), info()
primes = sieve_of_eratosthenes(n, y)
differences = np.diff(primes)
average_spacing = np.mean(differences)
prime_index = np.arange(0, len(primes), 1)
#twin_primes = compute_twin_primes()
#cousin_primes = compute_cousin_primes()
uber_differences = compute_uber_differences()
further_gaps = produce_custom_gaps()
further_arrays = get_custom_arrays(further_gaps)
further_means = produce_means()
dictionary = construct_dictionary()
factors = factorise_number(n)

plot_result = get_graph()
if plot_result == 'yes':
    ax1 = plt.subplot(111)
    ax1.plot(primes, (primes / np.log(primes)), linewidth=1.5, linestyle='-', color='red')
    ax1.text(0, 1100, 'At n = {0}, the difference is {1:3.2f}'.format(prime_index[-1] + 1, prime_index[-1] - (
                primes[-1] / np.log(primes[-1]))))
    ax1.set_title("Plot of prime frequency up to n = {1} (the {0}'th prime)".format(len(primes), primes[-1]))
    legend_label = ("average spacing between primes: {0:.2f}".format(average_spacing))
    ax1.set_ylabel(f"the n'th prime up to {len(primes)}")
    ax1.set_xlabel(f'the primes up to {primes[-1]}')
    ax1.plot(primes, prime_index, 'b.', label=legend_label)
    ax1.legend(loc='upper left', fontsize=10)
    plt.show()
    if len(dictionary) > 0:
        fig = plt.figure()
        ax = fig.add_subplot()
        for i in np.arange(0, len(further_gaps), 1):
            y_values = np.arange(0, len(further_means[i]), 1)
            x_values = further_means[i]
            label = 'n = {}'.format(further_gaps[i])
            legend_label = label
            ax.scatter(x_values, y_values, label = legend_label, color = colors[i])
            ax.legend(loc='upper left', fontsize=20)
        plt.title('Prime Pair Frequency Along the Number Line')
        plt.show()


'''def info():    fix this when you want to come back to this
    while True:
        y = input("Welcome to my prime number code! The code can perform 8 tasks based on user input"
        "1: Generate a list of primes, 2: Display the number of primes and the time taken,"
        " 3: Produce the prime list, 4: Plot a graph of this, 5: Generate arrays of prime pairs, "
        "6: Display these in the terminal, 7: Plot a graph comparing your chosen prime pair arrays,"
        "8: Find the prime factors of a number of your choice. Please enter 1 to generate the prime list,"
        "then any combination of numbers from 2 to 8 to perform the remaining tasks. Please note: a) forgetting 1 will"
                  " make the code"
        " generate an array of primes up to 10000. b) both 3, 4 and 7 require 2 to be entered as well for the code to run."
        " c) 7 requires 5 to be entered. Enjoy the code! Enter your string of numbers from 1-8 here: ").strip().lower()
        if y == 'yes':
            break
        elif y == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return y
'''