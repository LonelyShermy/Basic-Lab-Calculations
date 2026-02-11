import math
## Dumb calculator for Intermediate Lab
def Main():
    Data = [1000,990,1003,1000,1000,998,995,995,997,1003] #Modify to take files
    Mean = MeanFun(Data) 
    SD = StandardDeviation(Data,Mean)
    SDOM = StandardDeviationofMean(Mean, SD)
    ErrOnMean = ErroronMean(Data, SD)
    print("Mean:", Mean)
    print("Standard Deviation", SD)
    print("SDOM", SDOM)
    print("Error on Mean", ErrOnMean)


def MeanFun(Data):
    return sum(Data)/len(Data)

def StandardDeviation(Data, MeanLoc):
    Tot = 0
    for i in Data:
        Tot += (i-MeanLoc)*(i-MeanLoc)
    return math.sqrt(Tot/(len(Data)-1))

def StandardDeviationofMean(MeanLoc,SDLoc):
    return SDLoc/math.sqrt(MeanLoc)

def ErroronMean(Data, SD):
    return SD/math.sqrt(len(Data))

Main()