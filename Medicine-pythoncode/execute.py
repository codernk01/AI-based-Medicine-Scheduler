import prettytable 
from schedule import Schedule
from genetic_algo import Geneticalgorithm



def vis(schedule):
    """visualization medicine Schedule.

    Arguments:
        schedule: List, medicine Schedule
    """
    col_labels = ['Time slots', 'Day1','Day2','Day3']
    table_vals = [[str(i + 1)+':00-'+str(i+2)+':00', '','',''] for i in range(23)]
    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)
  #  print(table)
    for s in schedule:
        weekDay = s.weekDay
        slot = s.slot
        text = 'medicine: {} \n medicineId: {} \n effectdur: {} '.format(s.medicinename,s.medicineId, s.effectdur)
        table_vals[slot-8][weekDay] = text

    for row in table_vals:
        table.add_row(row)

    print(table)

if __name__ == '__main__':
    multdis=[]
        # add schedule
    print("1: Diabetes\n2: Covid\n3: FLU")
    val=input("How many diseases u are currently suffering from(Prefer 2,PS 3 medicines are not efficient):")
    for i in range(int(val)):
        desnum=input("select disease number associated to diseases:")
        multdis.append(desnum)
   # print(multdis)
    schedules=[]
    for diseasenum in multdis:
        if int(diseasenum)==1:
            schedules.append(Schedule("insu",201, 2, [201,202,605,345],[3,2]))
            schedules.append(Schedule("insu",201, 2, [201,202,605,345],[3]))
            schedules.append(Schedule("insu",201, 2, [201,202,605,345],[1,2]))
            schedules.append(Schedule("insu",201, 2, [201,202,605,345],[2,1]))
            schedules.append(Schedule("bloodregu",206, 5, [206,104,605],[1,3]))
            schedules.append(Schedule("bloodregu",206, 5, [206,104,605],[3]))
        elif int(diseasenum)==2:
            schedules.append(Schedule("remedisvie",202, 6, [202,204,201],[1,2]))
            schedules.append(Schedule("remedisvie",202, 6, [202,204,201],[2,3]))
            schedules.append(Schedule("multivit",204, 3, [204,202,605],[1,3]))
         #   schedules.append(Schedule("multivit",204, 3, [204,202,605],[2]))
            schedules.append(Schedule("multivit",204, 3, [204,202,605],[2,1]))
        elif int(diseasenum)==3:
            schedules.append(Schedule("coughrel",104, 1, [104,206,345],[3,2]))
            schedules.append(Schedule("coughrel",104, 1, [104,206,345],[2,1]))
            schedules.append(Schedule("antibio",605, 3, [605,201,204,206],[1,2]))
            schedules.append(Schedule("antibio",605, 3, [605,201,204,206],[3]))
         #   schedules.append(Schedule("antibio",605, 3, [605,201,204,206],[1]))
            schedules.append(Schedule("nostril",345, 4, [345,104,201],[2]))
    """
    schedules.append(Schedule(201, 2, [201,202]))
    schedules.append(Schedule(201, 2, [201,202]))
    schedules.append(Schedule(201, 2, [201,202]))
    schedules.append(Schedule(202, 6, [202,204,201,206]))
    schedules.append(Schedule(204, 3, [204,202]))
    schedules.append(Schedule(204, 3, [204,202]))
    schedules.append(Schedule(206, 5, [206,202]))
    """
        # optimization
    ga = Geneticalgorithm(popsize=50, elite=10, maxiter=2000)
    res = ga.evolution(schedules)

        # visualization
    vis(res)