from beamngpy import BeamNGpy, Scenario, Road, Vehicle, StaticObject
from beamngpy.sensors import Electrics, Damage, GForces

from BeamHome import getBeamngDirectory


def getWallCrashScenario():
    beamng = BeamNGpy('localhost', 64256, home=getBeamngDirectory())  # This is the host & port used to communicate over
    wallCrashScenario = Scenario('smallgrid', 'road_test')


    wall = StaticObject(name="Crash_Test_Wall", pos=(420, 0, 0), rot=(0, 0, 0), scale=(1, 10, 75),
                        shape='/levels/smallgrid/art/shapes/misc/gm_alpha_barrier.dae')

    testRoad=Road('track_editor_B_center', rid='Test_Road')
    roadNode=[(-2,0,0,7),(420,0,0,7)]
    testRoad.nodes.extend(roadNode)



    testVehicle = Vehicle('Test_Vehicule', model='etkc', licence='LIFLAB', colour='Blue')

    # Create an Electrics sensor and attach it to the vehicle
    electrics = Electrics()
    testVehicle.attach_sensor('electrics', electrics)

    # Create a Damage sensor and attach it to the vehicle if module is selected
    damage = Damage()
    testVehicle.attach_sensor('damage', damage)

    # Create a Gforce sensor and attach it to the vehicle if module is selected
    gForce = GForces()
    testVehicle.attach_sensor('GForces', gForce)



    wallCrashScenario.add_road(testRoad)
    wallCrashScenario.add_object(wall)
    wallCrashScenario.add_vehicle(testVehicle, pos=(0, 0, 0), rot=(0, 0, -90))
    scenarioDict={'beamng':beamng,'scenario':wallCrashScenario,'vehicule':testVehicle}


    return scenarioDict

getWallCrashScenario()