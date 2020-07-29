# Upper Confidence Bound




#strip is excepted,top of box is conf boundary,red line is excepted value
#long run red line and strip merge
#initally all with same conf box size and height  and red line same to all
#so now randomly take 1 box 
#if user not click box go down and size also decreasae(shrink) and red line move down
#always select next by checking highesy confident   box height on

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
import math
N = 10000  #total rounds
d = 10  #10 diff ads (no of ads)
ads_selected = []  #storing selected ad at each round
numbers_of_selections = [0] * d  #show count of ads selected corr 10 ads
sums_of_rewards = [0] * d  #sum of reward  corr 10 ads
total_reward = 0  #over all rewards
for n in range(0, N): #iterate 10000   #follow steps in table
    ad = 0
    max_upper_bound = 0  #select based on max upper boundary
    for i in range(0, d): # iterate 10  to select which is max_upper_bound
        if (numbers_of_selections[i] > 0):  #to skip inf so take >0
            #to ensure ad already been selected not as beginner
            average_reward = sums_of_rewards[i] / numbers_of_selections[i] #step2 
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:  #ad not been selected before so assign  upper_bound
            upper_bound = 1e400  #max selected by assign upper bounsdary to high so selected 
        if upper_bound > max_upper_bound:  #upper greater than prev upper  bound
            max_upper_bound = upper_bound  #update max upper boundary value
            ad = i #and corr ad assigning to ad
    ads_selected.append(ad)  #add sel ad in lists
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1 #update corr add in selection list
    reward = dataset.values[n, ad]  #get reward from dataset
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward #get reward update in  corr list
    total_reward = total_reward + reward  #update total reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()