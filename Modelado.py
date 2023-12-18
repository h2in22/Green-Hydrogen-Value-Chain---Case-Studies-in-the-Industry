# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:06:03 2023

@author: jorge
"""

import calliope
import pandas as pd

model = calliope.Model('C:/Users/jorge/OneDrive/Documents/PUCV/TESIS-H2IN-PAPELERAS/MODELO BIOBIO/MODELO PAPELERA/model.yml')

model.inputs
model.inputs.resource.to_pandas()
model.get_formatted_array('resource').sum('locs').to_pandas()
model.run()
model.results
model.to_csv("csv/TEST_3B01_AN")

model.plot.summary(to_file='C:/Users/jorge/OneDrive/Documents/PUCV/TESIS-H2IN-PAPELERAS/MODELO BIOBIO/MODELO PAPELERA/plot/TEST_3B01_AN.html', mapbox_access_token='pk.eyJ1IjoiZWxyaWNoaWFyZG8iLCJhIjoiY2wxbGJxN2VxMDQ1djNpbnd1ejAxYXQ4NSJ9.CUIkq5dLLfYC4ZvDb-SOlA')
#model.plot.flows(timestep_cycle=1)
#model.plot.capacity()
    