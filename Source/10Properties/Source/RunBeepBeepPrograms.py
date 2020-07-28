import os
import subprocess

from getBeepBeepProgramsFilePath import getBeepBeepProgramsFilePath


def RunBeepBeepPrograms(beepbeepProgramsFilePath,reposRootFilePath,scenarioDataFilePath):

    programsName=["MaxSpeed","CarAngle","MaxAcceleration","GForce",
                  "Check","GearTime","MinMaxAverageRPM","SteeringAngle"]

    commandTemplate="java -classpath \""+os.path.join(reposRootFilePath,"beepbeep-3.jar"+";"
              +os.path.join(reposRootFilePath,"json.jar")+";"+os.path.join(reposRootFilePath,"mtnp.jar")+
              ";.\" ")


    for x in range (len(beepbeepProgramsFilePath)):
        os.chdir(beepbeepProgramsFilePath[x])
        if(x!=4):
            subprocess.check_output((commandTemplate+programsName[x]+ " " +scenarioDataFilePath))
        else:
            xPos=int(input("Enter the X position to check: "))
            yPos=int(input("Enter the Y position to check: "))
            subprocess.check_output((commandTemplate+programsName[x]+ " " +scenarioDataFilePath+" "+str(xPos)+" "+str(yPos)))



