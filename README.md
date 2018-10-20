# Sternberg Working Memory K Task
This repository contains all of the necessary files to run the Sternberg Working Memory (SWMT) K Task. This task is a standard SWMT with 35 events, 7 events of each load size (3,4,5,6,7); events are displayed randomly. The K score is calculated according to: K = s*(percentHits – percentFalseAlarms), where s = load size. The K score is output at the end of the K Task. 

#Getting Started 
You will need to create a folder in the directory that you store KTaskTools.py and KTaskTest.py called 'Backgrounds'. Put all of the .tiff images in the 'Backgrounds' folder. The KTaskTools.py and Ktask.py files utilize libraries from PscyhoPy. I reccomend downloading PsychoPy and working out of this program. KTaskTest.py is used to run the acutal experiment and utilizes KTaskTools.py. After every epoch in the KTask, a data frame is saved as a .csv containing the subject's response, whether or not it was a hit/false alarm/miss, and reaction time. At the conclusion of the task, another data frame containing a summary of the subject's statistics is exported to a .csv. 


