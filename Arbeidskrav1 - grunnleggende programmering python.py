"""
Created on Mon Nov  4 17:52:21 2024

Arbeidskrav 1 - Grunnleggende programmering med python

@author: Marlen G. Stoetvig
"""

""" Beregning av årlig totalkostnad elbil, antatt 10.000 kjørte km per år. """

a=5000  # Forsikring kr/år
b=8.38*365  # Trafikkforsikringsavgift kr/år (8.38kr/dag)
c=0.2*10000*2  # Drivstoffbruk kr/år (0.2kWh/km, 2.00kr/kWh)
d=0.1*10000  # Bomavgift kr/år (0.1kr/km)
e=a+b+c+d  # Totalkostnad kr/år elbil

""" Beregning av årlig totalkostnad bensinbil, antatt 10.000 kjørte km per år. """ 

f=7500  # Forsikring kr/år
g=8.38*365  # Trafikkforsikringsavgift kr/år (8.38kr/dag)
h=1*10000  # Drivstoffbruk kr/år (1.0kr/km)
i=0.3*10000  # Bomavgift kr/år (0.3kr/km)
j=f+g+h+i  # Totalkostnad kr/år bensinbil

""" Beregning av kostandsdifferanse, bensinbil-elbil. """

k=j-e  # Årlig kostnadsdifferanse

print("Totalkostnad elbil, kr/år =", e)
print("Totalkostnad bensinbil, kr/år =", j)
print("Årlig kostnadsdifferanse =", k)



