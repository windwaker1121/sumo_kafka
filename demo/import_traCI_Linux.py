import os, sys

if 'SUMO_HOME' in os.environ:
  tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
  sys.path.append(tools)
else:   
  sys.exit("please declare environment variable 'SUMO_HOME'")

from kafka import KafkaProducer
from kafka.errors import KafkaError
import traci

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

sumoBinary = "/usr/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "/usr/share/doc/sumo-doc/tutorial/traci_tls/data/cross.sumocfg"]
tc = traci.constants
traci.start(sumoCmd) 
step = 0
while step < 1000:
  producer.send('test', '--------------------')
  traci.vehicle.subscribe("left_0", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
  traci.vehicle.subscribe("left_1", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
  strtemp = traci.vehicle.getSubscriptionResults("left_0")
  producer.send('test', 'left_0:'+strtemp[80]+','+str(strtemp[86]))
  #print(traci.vehicle.getSubscriptionResults("left_0"))
  #traci.vehicle.subscribe("left_1", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
  strtemp = traci.vehicle.getSubscriptionResults("left_1")
  producer.send('test', 'left_1:'+strtemp[80]+','+str(strtemp[86]))
  #print(traci.vehicle.getSubscriptionResults("left_1"))
  try:
    traci.vehicle.subscribe("right_2", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
    #print(traci.vehicle.getSubscriptionResults("right_2"))
    strtemp = traci.vehicle.getSubscriptionResults("right_2")
    producer.send('test', 'right_2:'+strtemp[80]+','+str(strtemp[86]))    
  except:
    print("")
  try:
    traci.vehicle.subscribe("right_3", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
    #print(traci.vehicle.getSubscriptionResults("right_3"))
    strtemp = traci.vehicle.getSubscriptionResults("right_3")
    producer.send('test', 'right_3:'+strtemp[80]+','+str(strtemp[86]))   
  except:
    print("")
  traci.simulationStep()
  if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
    traci.trafficlights.setRedYellowGreenState("0", "GrGr")
  step += 1

traci.close()
exit()
