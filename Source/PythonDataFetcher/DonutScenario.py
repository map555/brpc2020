from beamngpy import BeamNGpy, Scenario, Vehicle, StaticObject, Road
from beamngpy.sensors import Electrics, Damage, GForces

from BeamHome import getBeamngDirectory


def getDonutScenario():
    beamng = BeamNGpy('localhost', 64256, home=getBeamngDirectory())  # This is the host & port used to communicate over
    donutScenario = Scenario('smallgrid', 'road_test')

    concreteWallSide1=StaticObject(name="Crash_Test_Wall", pos=(20, 10, 0), rot=(0, 0, 0), scale=(10, 1, 1),
                 shape='/levels/driver_training/art/shapes/race/concrete_road_barrier_a.dae')

    concreteWallSide2 = StaticObject(name="Crash_Test_Wall2", pos=(35, -5, 0), rot=(0, 0, 90), scale=(10, 1, 1),
                                     shape='/levels/driver_training/art/shapes/race/concrete_road_barrier_a.dae')

    concreteWallSide3 = StaticObject(name="Crash_Test_Wall3", pos=(20, -20, 0), rot=(0, 0, 0), scale=(10, 1, 1),
                                     shape='/levels/driver_training/art/shapes/race/concrete_road_barrier_a.dae')

    concreteWallSide4 = StaticObject(name="Crash_Test_Wall4", pos=(5, -5, 0), rot=(0, 0,90 ), scale=(10, 1, 1),
                                     shape='/levels/driver_training/art/shapes/race/concrete_road_barrier_a.dae')

    testRoad = Road('track_editor_C_center', rid='Test_Road')
    roadNode = [(*(-25, 25, 0), 45), (*(15,25 , 0), 45)]
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


    donutScenario.add_vehicle(testVehicle, pos=(20, 0, 0), rot=(0, 0, 0))

    donutScenario.add_object(concreteWallSide1)
    donutScenario.add_object(concreteWallSide2)
    donutScenario.add_object(concreteWallSide3)
    donutScenario.add_object(concreteWallSide4)

    donutScenario.add_road(testRoad)


    scenarioDict={'beamng':beamng,'scenario':donutScenario,'vehicule':testVehicle}

    return scenarioDict

