

startingRecords = [
                    [
                      ['D',0,0], ['S',0,0], ['E',0,0], ['R',0,0]
                    ],
                  ]

weeksWithMatchups = [
                      [
                        ['D','E'], ['R','S']
                      ],
                      [
                        ['D','S'], ['E','R']
                      ],
                      [
                        ['D','R'], ['E','S']
                      ],
                    ]


def calculateRecords(listOfRecords, matchups):
  #dummy data for now
  dummyData = [
                [
                  ['d',3,0], ['s',0,3], ['e',2,1], ['r',1,2]
                ],
                [
                  ['d',3,0], ['s',0,3], ['e',2,1], ['r',1,2]
                ],
                [
                  ['d',2,1], ['s',0,3], ['e',2,1], ['r',1,2]
                ],
                [
                  ['d',3,0], ['s',1,3], ['e',2,1], ['r',1,2]
                ],
                [
                  ['d',3,0], ['s',1,3], ['e',2,1], ['r',1,2]
                ],
                [
                  ['d',3,0], ['s',0,3], ['e',1,1], ['r',1,2]
                ],
                [
                  ['d',3,0], ['s',0,3], ['e',2,1], ['r',11,2]
                ],
              ]
  return dummyData

def prune(listOfAllRecords):
  if listOfAllRecords[1:] == []: # if only one record remains
    return listOfAllRecords
  for outcome in listOfAllRecords[1:]:
    if listOfAllRecords[0] == outcome: # if a set of records is achieved again in the possible outcomes
      return prune(listOfAllRecords[1:]) # then dont count it (that instance will be counted when it is the only one left) and continue with the rest of the list
  return [listOfAllRecords[0]] + prune(listOfAllRecords[1:]) # if it was unique, add it and continue on wiht the rest


def iterateThroughMatchups(listoflistofRecords, weekMatchups):
  potentialOutcomes = []
  for listofRecords in listoflistofRecords:
    potentialOutcomes += calculateRecords(listofRecords, weekMatchups)

  return prune(potentialOutcomes)

def main():
  possibleOutcomes = startingRecords

  for week in weeksWithMatchups:
    possibleOutcomes = iterateThroughMatchups(possibleOutcomes, week)

  print(possibleOutcomes)


if __name__ == "__main__":
  main()