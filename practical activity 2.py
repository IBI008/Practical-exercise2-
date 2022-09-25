#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Solution to the Practical Activity


# In[5]:


# Question One
# Emergency numbers: Law Enforcement (123), Fire and Rescue Services (224),
# Emergency Medical Services (101), Emergency Management (999), and Publi Work(900)

import pandas as pd 
# Create a dictionary
dict_1 = {'123':'Law Enforcement',
         '224':'Fire and Rescue Services',
         '101':'Emergency Medical Services',
         '999':'Emergency Management',
         '900':'Public Works'}

# Create a series
emergency_numbers = pd.Series(dict_1)
print(emergency_numbers)


# In[7]:


# Question Two
# Emergency Protocols: Prevention, Mitigation, Preparedness, Response and Recovery.

# Create a number list

emergency_protocols = pd.Series(['Prevention', 'Mitigation',
                               'Preparadness','Response',
                                'Recovery'],
                              index = ['1','2','3','4','5'])
print(emergency_protocols)


# In[8]:


# Question Three.
# Emergency Checklist: Check pulse (neck), breathing (nose),
# Obstructions (nose, mouth, ears), pupil (responsive), 
# Consciousness, contact details and allergies

# create a series from the list

checklist = ['Check pulse (neck)','Check breathing (nose)',
                       'Obstructions (nose, mouth, ears)',
                       'pupil (responsive)','Consciousness',
                      'contact details','Any Allergies']

emergency_checklist = pd.Series(checklist)
print(emergency_checklist)


# In[ ]:




