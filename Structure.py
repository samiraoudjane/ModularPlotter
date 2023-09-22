
#doprocessing
with open("ProcessingOnly.py") as Process:
    exec(Process.read())



#plottingblock
#---------------------------------

#plotting 0
try:
    with open("Plots0.py") as Plots0:
        exec(Plots0.read())
except:
    print("an error occured block 0")

#plotting 1

try:
    with open("Plots1.py") as Plots1:
        exec(Plots1.read())
except:
    print("an error occured block 1")

#plotting2
try:
    with open("Plots2.py") as Plots1:
        exec(Plots1.read())
except:
    print("an error occurred block 2")

#-----------------------------------

#cleanup

with open("CleanUp.py") as CleanUp:
    exec(CleanUp.read())
