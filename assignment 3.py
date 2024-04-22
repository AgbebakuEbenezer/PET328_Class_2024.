Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def classify_block(co2_comp, n2_comp, h2s_comp, h2o_comp, gas_gravity):
...     # convert inputs to numerals
...     co2_comp = float(co2_comp)
...     n2_comp = float(n2_comp)
...     h2s_comp = float(h2s_comp)
...     h2o_comp = float(h2o_comp)
...     gas_gravity = float(gas_gravity)
...     
...     # initialize block category
...     block_cat = None
... 
...     # the if statement
...     if co2_comp > 0.12 or n2_comp > 0.03 or h2s_comp > 0:
...         gas_gravity = (gas_gravity - (1.1767*h2s_comp) - \
...                           (1.5196*co2_comp) - (0.9672*n2_comp) - \
...                            (0.622*h2o_comp))/(1- h2s_comp - co2_comp - n2_comp - h2o_comp)
...         print('The corrected gas gravity is', gas_gravity)
...         block_cat = 'Non-hydrocarbon'
... 
...     # computing pseudo-critical pressure and temperature of the hydrocarbon mixture
...     p_pch = 756.8 - (131*gas_gravity) - (3.6*gas_gravity**2)
...     t_pch = 169.2 + (349.5*gas_gravity) - (74.0*gas_gravity**2)
... 
...     # displaying the results.
...     print('The hydrocarbon pseudo-critical pressure is {0:.2f} psia'.format(p_pch))
...     print('The hydrocarbon pseudo-critical temperature is {0:.2f} deg Rankine'.format(p_pch))
...     
...     return block_cat
... 
... # Example usage:
... co2_comp = input('What is the CO2 composition? ')
... n2_comp = input('What is the N2 composition? ')
... h2s_comp = input('What is the H2S composition? ')
... h2o_comp = input('What is the H2O composition? ')
... gas_gravity = input('What is the measured gas gravity? ')
... 
... block_cat = classify_block(co2_comp, n2_comp, h2s_comp, h2o_comp, gas_gravity)
