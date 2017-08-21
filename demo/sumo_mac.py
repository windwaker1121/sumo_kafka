import os, sys

if 'SUMO_HOME' in os.environ:
  tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
  sys.path.append(tools)
else:   
  sys.exit("please declare environment variable 'SUMO_HOME'")

import traci

sumoBinary = "/opt/local/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "/opt/local/share/doc/sumo/tutorial/hello/data/hello.sumocfg"]
tc = traci.constants
traci.start(sumoCmd) 
step = 0
while step < 1000:
  print('--------------------')
  traci.vehicle.subscribe("veh0", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
  ##
  strtemp = traci.vehicle.getSubscriptionResults("veh0")
  print('left_1:'+strtemp[80]+','+str(strtemp[86]))
  """try:
    traci.vehicle.subscribe("right_2", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
    strtemp = traci.vehicle.getSubscriptionResults("right_2")
    print('right_2:'+strtemp[80]+','+str(strtemp[86]))    
  except:
    print("")
  try:
    traci.vehicle.subscribe("right_3", (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
    strtemp = traci.vehicle.getSubscriptionResults("right_3")
    print('right_3:'+strtemp[80]+','+str(strtemp[86]))   
  except:
    print("")
  """
  try:
    traci.simulationStep()
  except:
    print("")
  step += 1

traci.close()
exit()
