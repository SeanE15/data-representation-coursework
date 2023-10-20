import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

#print (doc.toprettyxml(), end='')

#with open("trainxml.xml","w") as xmlfp:
  #doc.writexml(xmlfp)

#objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
#for objTrainPositionsNode in objTrainPositionsNodes:
    #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    #traincode = traincodenode.firstChild.nodeValue.strip()
    #print(traincode)

with open("week01_train,csv", mode="w", newline='') as train_file:
  train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  TrainPositions = doc.getElementsByTagName("objTrainPositions")
  for objTrainPositionsNode in TrainPositions:
    latitude_node = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    if latitude_node and latitude_node.firstChild:
      latitude = latitude_node.firstChild.nodeValue.strip()
      train_writer.writerow([latitude])