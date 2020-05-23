# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

success_estimates = {
   'Australia': [0.6, 0.33, 0.11, 0.14],
   'France': [0.66, 0.78, 0.98, 0.2],
   'Italy': [0.6],
   'Brazil': [0.22, 0.22, 0.43],
   'USA': [0.2, 0.5, 0.3],
   'England': [0.45],
   'Canada': [0.25, 0.3],
   'Argentina': [0.22],
   'Greece': [0.45, 0.66, 0.75, 0.99, 0.15, 0.66],
   'Morocco': [0.29],
   'Tunisia': [0.68, 0.56],
   'Egypt': [0.99],
   'Jamaica': [0.61, 0.65, 0.71],
   'Switzerland': [0.73, 0.86, 0.84, 0.51, 0.99],
   'Germany': [0.45, 0.49, 0.36]
}

print('Number of estimates for France:')
print(len(success_estimates['France']))

print('Number of estimates for Greece:')
print(len(success_estimates['Greece']))

print('Number of estimates for Morocco:')
print(len(success_estimates['Morocco']))

avg_jamaica = (0.61 + 0.65 + 0.71) / 3
print(avg_jamaica)

country_name = 'Jamaica'
jamaica_list = success_estimates[country_name] # list of the estimates for Jamaica
print(jamaica_list)

avg_jamaica = round(sum(jamaica_list) / len(jamaica_list),2)
min_jamaica = min(jamaica_list)
max_jamaica = max(jamaica_list)
print("Country:",country_name,", Average:",avg_jamaica)
print("Country:",country_name,", Min:",min_jamaica)
print("Country:",country_name,", Max:",max_jamaica)

print("Country:",'France',", Average:",sum(success_estimates['France']) / len(success_estimates['France']))
print("Country:",'Brazil',", Average:",sum(success_estimates['Brazil']) / len(success_estimates['Brazil']))
print("Country:",'Argentina',", Average:",sum(success_estimates['Argentina']) / len(success_estimates['Argentina']))
print("Country:",'Germany',", Average:",sum(success_estimates['Germany']) / len(success_estimates['Germany']))
print("Country:",'Australia',", Average:",sum(success_estimates['Australia']) / len(success_estimates['Australia']))
print("Country:",'Canada',", Average:",sum(success_estimates['Canada']) / len(success_estimates['Canada']))
print("Country:",'Greece',", Average:",sum(success_estimates['Greece']) / len(success_estimates['Greece']))
print("Country:",'USA',", Average:",sum(success_estimates['USA']) / len(success_estimates['USA']))
print("Country:",'Switzerland',", Average:",sum(success_estimates['Switzerland']) / len(success_estimates['Switzerland']))
print("Country:",'Tunisia',", Average:",sum(success_estimates['Tunisia']) /len(success_estimates['Tunisia']))
print("Country:",'Italy',", Average:",sum(success_estimates['Italy']) / len(success_estimates['Italy']))
print("Country:",'Egypt',", Average:",sum(success_estimates['Egypt']) / len(success_estimates['Egypt']))
print("Country:",'Jamaica',", Average:",sum(success_estimates['Jamaica']) / len(success_estimates['Jamaica']))
print("Country:",'Morocco',", Average:",sum(success_estimates['Morocco']) / len(success_estimates['Morocco']))
print("Country:",'England',", Average:",sum(success_estimates['England']) / len(success_estimates['England']))

country_name_list = list(success_estimates.keys())

for i in country_name_list:
    print('--Begin one iteration of loop--')
    print('Element of country_name_list, placeholder i = ' + i)
    print('Access value from dict success_estimates[i]: ', success_estimates[i])
    print('Average of list from success_estimates[i]: ', sum(success_estimates[i]) / len(success_estimates[i]))
    print('--Go to next iteration of loop--')
    print()
print(country_name_list)

for country in country_name_list:
    print('Country',country,', Min: ', min(success_estimates[country]))
    print('Country',country,', Max: ', max(success_estimates[country]))
    
    
for country in country_name_list:
    country_range = max(success_estimates[country]) - min(success_estimates[country])
    print('Country: ', country, ", Range: ", country_range)
    
    
value_name_list = [success_estimates[country] for country in success_estimates] # loop over each item in success_estimates and put success_estimates[i] in the list
value_name_list


sum_squares_list = [[i, sum([j**2 for j in success_estimates[i]])] for i in success_estimates]
sum_squares_list

print (sum_squares_list)