import matplotlib.pyplot as plot
import numpy as np

#inputBitString = str(input("Enter the bit string: "))
inputBitString = "101100110101"

def setSubPlot(ax,title,xpoints,ypoints):
    ax.set_title(title)
    ax.plot(xpoints,ypoints)
    ax.set_xlabel("time")
    ax.grid(True,which="both")
    ax.set_xticks(np.arange(min(xpoints),max(xpoints)+1,1.0))
    return ax

def appendToPoint(pointsX,pointsY,currX,currY):
    pointsX.append(currX)
    pointsY.append(currY)

def returnRZ(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 0
    if inputStr[0]=="1":
        currY=1
    if inputStr[0]=="0":
        currY=-1
    appendToPoint(pointsX,pointsY,currX,currY)
    for a in inputStr:
        if a == "1":
            currY=1
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)
            currY=0
            appendToPoint(pointsX,pointsY,currX,currY)

            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)

        if a == "0":
            currY=-1
            appendToPoint(pointsX,pointsY,currX,currY)

            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)

            currY=0
            appendToPoint(pointsX,pointsY,currX,currY)

            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)

    return pointsX,pointsY            


def returnManchester(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 0
    if inputStr[0]=="0":
        currY=1
    if inputStr[0]=="1":
        currY=-1
    appendToPoint(pointsX,pointsY,currX,currY)
    for a in inputStr:
        if a == "0":
            currY=1
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)
            currY=-1
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)

        if a == "1":
            currY=-1
            appendToPoint(pointsX,pointsY,currX,currY)

            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)

            currY=1
            appendToPoint(pointsX,pointsY,currX,currY)

            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)

    return pointsX,pointsY

def differentialManchester(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 1
    for a in inputStr:
        if a=="0":
            currY=-currY
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)
            currY=-currY
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)
        if a == "1":
            currY=currY
            appendToPoint(pointsX,pointsY,currX,currY)

            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)

            currY=-currY
            appendToPoint(pointsX,pointsY,currX,currY)

            currX+=0.5
            appendToPoint(pointsX,pointsY,currX,currY)
    return pointsX,pointsY

def returnAMI(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 0
    curr1 = 1
    for a in inputStr:
        if a == "0":
            currY=0
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=1
            appendToPoint(pointsX,pointsY,currX,currY)
        if a == "1":
            if curr1 == 1:
                currY = 1
                curr1 = -1
            else:
                currY = -1
                curr1 = 1
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=1
            appendToPoint(pointsX,pointsY,currX,currY)

    return pointsX,pointsY
    
   
def returnPseudoTernary(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 0
    curr1 = 1
    for a in inputStr:
        if a == "1":
            currY=0
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=1
            appendToPoint(pointsX,pointsY,currX,currY)
        if a == "0":
            if curr1 == 1:
                currY = 1
                curr1 = -1
            else:
                currY = -1
                curr1 = 1
            appendToPoint(pointsX,pointsY,currX,currY)
            currX+=1
            appendToPoint(pointsX,pointsY,currX,currY)

    return pointsX,pointsY    

def returnNRZ(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 0
    appendToPoint(pointsX,pointsY,currX,currY)

    for a in inputStr:
        if a=="1":
            currY=1
        if a=="0":
            currY=0
        appendToPoint(pointsX,pointsY,currX,currY)
        currX+=1
        appendToPoint(pointsX,pointsY,currX,currY)

    return pointsX,pointsY

def returnNRZI(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 1
    for a in inputStr:
        if a=="1":
            currY=-currY
        appendToPoint(pointsX,pointsY,currX,currY)

        currX+=1
        appendToPoint(pointsX,pointsY,currX,currY)

    return pointsX,pointsY        
        

def returnNRZL(inputStr):
    pointsX = []
    pointsY = []
    currX = 0
    currY = 0
    for a in inputStr:
        if a=="0":
            currY=1
        if a=="1":
            currY=-1
        appendToPoint(pointsX,pointsY,currX,currY)

        currX+=1
        appendToPoint(pointsX,pointsY,currX,currY)

    return pointsX,pointsY
           
    
def plotGraph(inputStr):
    fig, ax = plot.subplots(4,2)
    xpoints,ypoints = returnNRZ(inputStr)
    ax[0,0] = setSubPlot(ax[0,0],"NRZ",xpoints,ypoints)
    xpoints,ypoints = returnNRZL(inputStr)
    ax[0,1] = setSubPlot(ax[0,1],"NRZL",xpoints,ypoints)
    xpoints,ypoints = returnNRZI(inputStr)
    ax[1,0] = setSubPlot(ax[1,0],"NRZ-I",xpoints,ypoints)
    xpoints,ypoints = returnRZ(inputStr)
    ax[1,1] = setSubPlot(ax[1,1],"RZ",xpoints,ypoints)
    xpoints,ypoints = returnManchester(inputStr)
    ax[2,0] = setSubPlot(ax[2,0],"Manchester",xpoints,ypoints)
    xpoints,ypoints = differentialManchester(inputStr)
    ax[2,1] = setSubPlot(ax[2,1],"Differential-Manchester",xpoints,ypoints)
    xpoints,ypoints = returnAMI(inputStr)
    ax[3,0] = setSubPlot(ax[3,0],"AMI",xpoints,ypoints)
    xpoints,ypoints = returnPseudoTernary(inputStr)
    ax[3,1] = setSubPlot(ax[3,1],"PseudoTernary",xpoints,ypoints)
    fig.tight_layout()
   # fig.set_figwidth(400)
    title = "Bit String is: " + inputBitString
    fig.suptitle(title)
    plot.show()
    
plotGraph(inputBitString)   