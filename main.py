import math
## Dumb calculator for Intermediate Lab
def Main():
    Data = [310, 350, 290, 300, 285] #Modify to take files
    Mean = MeanFun(Data) 
    SD = StandardDeviation(Data,Mean)
    SDOM = StandardDeviationofMean(Mean, SD)
    print("Mean:", Mean)
    print("Standard Deviation", SD)
    print("SDOM", SDOM)

def MeanFun(Data):
    return sum(Data)/len(Data)

def StandardDeviation(Data, MeanLoc):
    Tot = 0
    for i in Data:
        Tot += (i-MeanLoc)*(i-MeanLoc)
    return math.sqrt(Tot/(MeanLoc-1))

def StandardDeviationofMean(MeanLoc,SDLoc):
    return SDLoc/math.sqrt(MeanLoc)

Main()