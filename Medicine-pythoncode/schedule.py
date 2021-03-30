import numpy as np


class Schedule:
    """Class Schedule.
    """
    def __init__(self,medicinename, medicineId, effectdur,constraint_medicines,days):
        """Init
        Arguments:
            medicineId: int, unique course id.
            effectdur: int, unique teacher id.
        """
        self.medicinename=medicinename
        self.medicineId = medicineId
#        self.doseno = doseno
        self.effectdur = effectdur
        self.constraint_medicines=constraint_medicines
        self.days=days
    #    self.roomId = 0
        self.weekDay = 0
        self.slot = 0

    def random_init(self):
        """random init.
        """
        self.weekDay = np.random.randint(1, 4, 1)[0]
        self.slot = np.random.randint(1, 24, 1)[0]
  #      print(self.medicineId,self.slot)


def schedule_cost(population, elite):
    """calculate conflict of medicine schedules.

    Arguments:
        population: List, population of medicine schedules.
        elite: int, number of best result.

    Returns:
        index of best result.
        best conflict score.
    """
    conflicts = []
    n = len(population[0])

    for p in population:
        conflict = 0
        for i in range(0, n):
            if p[i].weekDay not in p[i].days:
                conflict+=1
            for j in range(0, n):
                # check course in same time and same room 
                if i!=j and p[j].medicineId in p[i].constraint_medicines and p[j].slot in range(p[i].slot,p[i].slot + p[i].effectdur) and p[i].weekDay==p[j].weekDay:
                    conflict += 1
                
        conflicts.append(conflict)

    index = np.array(conflicts).argsort()

    return index[: elite], conflicts[index[0]]
