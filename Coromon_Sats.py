# Add you code here
import random
with open("CoromonDataset.csv") as dataset:
    total_coromon = 0
    coromon_dict = {}
    coromon_stats = []
    coromon_types = []

    for line in dataset:#for loop that creates a dictionary out of the csv, key is the coromon name, value is a list of it's stats.
        line = line.split(",")
        if line[0] != "Coromon":
            total_coromon += 1
            coromon_stats = line[1:]
            coromon_dict[line[0]] = coromon_stats
            
    for mon, stats in coromon_dict.items():#for loop that adds all different types to a list, ignoring duplicates.
        if stats[0] not in coromon_types:
            coromon_types.append(stats[0])

    stats_lists = list(coromon_dict.values())

    def average_values(mon_type):#Finds the average of every stat of every coromon of a specific type, and stores them in a list
        HP_avg = 0
        ATK_avg = 0
        SP_ATK_avg = 0
        DEF_avg = 0
        SP_DEF_avg = 0
        SPD_avg = 0
        STM_avg = 0 
        divider = 0
        
        for each_list in stats_lists:
            if str(each_list[0]) == mon_type:
                HP_avg += int(each_list[1])
                ATK_avg += int(each_list[2])
                SP_ATK_avg += int(each_list[3])
                DEF_avg += int(each_list[4])
                SP_DEF_avg += int(each_list[5])
                SPD_avg += int(each_list[6])
                STM_avg += int(each_list[7])
                divider += 1

        HP_avg = HP_avg / divider
        ATK_avg = ATK_avg / divider
        SP_ATK_avg = SP_ATK_avg / divider
        DEF_avg = DEF_avg / divider
        SP_DEF_avg = SP_DEF_avg / divider
        SPD_avg = SPD_avg / divider
        STM_avg = STM_avg / divider

        results = ("Average stats for all coromon of the ",mon_type," type:\n","Health: ",str(HP_avg) + '\n' + "Attack: ",str(ATK_avg) + '\n' + "Sp. Attack: ",str(SP_ATK_avg) + '\n'+ "Defense: ",str(DEF_avg) + '\n'+ "Sp. Defense: ",str(SP_DEF_avg) + '\n'+ "Speed: ",str(SPD_avg) + '\n'+ "Stamina Points: ",str(STM_avg) + '\n')

        return "".join(results)

    def list_average_values(mon_type):#Returns a list of the average stats of one mon type
        HP_avg = 0
        ATK_avg = 0
        SP_ATK_avg = 0
        DEF_avg = 0
        SP_DEF_avg = 0
        SPD_avg = 0
        STM_avg = 0 
        divider = 0
        avg_stats_list = []
        

        for each_list in stats_lists:
            if str(each_list[0]) == mon_type:
                HP_avg += int(each_list[1])
                ATK_avg += int(each_list[2])
                SP_ATK_avg += int(each_list[3])
                DEF_avg += int(each_list[4])
                SP_DEF_avg += int(each_list[5])
                SPD_avg += int(each_list[6])
                STM_avg += int(each_list[7])
                divider += 1

        HP_avg = HP_avg / divider
        ATK_avg = ATK_avg / divider
        SP_ATK_avg = SP_ATK_avg / divider
        DEF_avg = DEF_avg / divider
        SP_DEF_avg = SP_DEF_avg / divider
        SPD_avg = SPD_avg / divider
        STM_avg = STM_avg / divider

        avg_stats_list.append(HP_avg)
        avg_stats_list.append(ATK_avg)
        avg_stats_list.append(SP_ATK_avg)
        avg_stats_list.append(DEF_avg)
        avg_stats_list.append(SP_DEF_avg)
        avg_stats_list.append(SPD_avg)
        avg_stats_list.append(STM_avg)
        
        return avg_stats_list

    def max_and_min():
        max_hp = 0
        min_hp = 100000
        max_atk = 0
        min_atk = 10000
        max_sp_atk = 0
        min_sp_atk = 10000
        max_def = 0
        min_def = 10000
        max_sp_def = 0
        min_sp_def = 10000
        max_speed = 0
        min_speed = 10000
        max_stam = 0
        min_stam = 10000
        for Type in coromon_types:
            if list_average_values(Type)[0] > max_hp:
                type_with_max_hp = Type
                max_hp = list_average_values(Type)[0]
            if list_average_values(Type)[0] < min_hp:
                type_with_min_hp = Type
                min_hp = list_average_values(Type)[0]
            if list_average_values(Type)[1] > max_atk:
                type_with_max_atk = Type
                max_atk = list_average_values(Type)[1]

            if list_average_values(Type)[1] < min_atk:
                type_with_min_atk = Type
                min_atk = list_average_values(Type)[1]

            if list_average_values(Type)[2] > max_sp_atk:
                type_with_max_sp_atk = Type
                max_sp_atk = list_average_values(Type)[2]

            if list_average_values(Type)[2] < min_sp_atk:
                type_with_min_sp_atk = Type
                min_sp_atk = list_average_values(Type)[2]

            if list_average_values(Type)[3] > max_def:
                type_with_max_def = Type
                max_def = list_average_values(Type)[3]
            
            if list_average_values(Type)[3] < min_def:
                type_with_min_def = Type
                min_def = list_average_values(Type)[3]
            
            if list_average_values(Type)[4] > max_sp_def:
                type_with_max_sp_def = Type
                max_sp_def = list_average_values(Type)[4]
            
            if list_average_values(Type)[4] < min_sp_def:
                type_with_min_sp_def = Type
                min_sp_def = list_average_values(Type)[4]

            if list_average_values(Type)[5] > max_speed:
                type_with_max_speed = Type
                max_speed = list_average_values(Type)[5]

            if list_average_values(Type)[5] < min_speed:
                type_with_min_speed = Type
                min_speed = list_average_values(Type)[5]
            
            if list_average_values(Type)[6] > max_stam:
                type_with_max_stam = Type
                max_stam = list_average_values(Type)[6]
            
            if list_average_values(Type)[6] < min_stam:
                type_with_min_stam = Type
                min_stam = list_average_values(Type)[6]
        results = ("The type with the highest avg HP is " + str(type_with_max_hp) + " at " + str(max_hp) + "\n" + 
        "The type with the lowest avg HP is " + str(type_with_min_hp) + " at " + str(min_hp) + "\n" + 
        "The type with the highest avg Attack is " + str(type_with_max_atk) + " at " + str(max_atk) + "\n" + 
        "The type with the lowest avg Attack is " + str(type_with_min_atk) + " at " + str(min_atk) + "\n" + 
        "The type with the highest avg Sp. Attack is " + str(type_with_max_sp_atk) + " at " + str(max_sp_atk) + "\n" + 
        "The type with the lowest avg Sp. Attack is " + str(type_with_min_sp_atk) + " at " + str(min_sp_atk) + "\n" + 
        "The type with the highest avg Defense is " + str(type_with_max_def) + " at " + str(max_def) + "\n" +
        "The type with the lowest avg Defense is " + str(type_with_min_def) + " at " + str(min_def) + "\n" +  
        "The type with the highest avg Sp. Defense is " + str(type_with_max_sp_def) + " at " + str(max_sp_def) + "\n" +
        "The type with the lowest avg Sp. Defense is " + str(type_with_min_sp_def) + " at " + str(min_sp_def) + "\n" +  
        "The type with the highest avg Speed is " + str(type_with_max_speed) + " at " + str(max_speed) + "\n" + 
        "The type with the lowest avg Speed is " + str(type_with_min_speed) + " at " + str(min_speed) + "\n" + 
        "The type with the highest avg Stamina is " + str(type_with_max_stam) + " at " + str(max_stam) + "\n") 
        return results

#***************EXECUTION STATEMENTS*************
while True:
    user_input = input("Select what you'd like to do:\n 1 to display how many coromon exist \n 2 to display a random coromon and it's stats \n 3 to display the different coromon types \n 4 to display the average value of all stats across all coromon types \n 5 to display the highest and lowest average values, as well as which type has each. Enter 'stop' to stop.\n")

    if user_input == "1":
        print("There are " + str(total_coromon) + " total Coromon.\n")

    elif user_input == "2":
        random_mon = random.choice(list(coromon_dict.items())) #generates a random coromon from the dictionary
        mon_stats = random_mon[1]
        print(random_mon[0] +":" + "\n" + "Type:" , str(mon_stats[0]) + '\n' + "Health Points:", str(mon_stats[1]) + '\n' + "Attack:",str(mon_stats[2]) + '\n' + "Sp. Attack:",str(mon_stats[3]) + '\n' + "Defense:",str(mon_stats[4]) + '\n' + "Sp. Defense:",str(mon_stats[5]) + '\n' + "Speed:",str(mon_stats[6]) + '\n' + "Stamina Points:",str(mon_stats[7]))

    elif user_input == "3":
        print("The coromon types include: " + ", ".join(coromon_types) + '\n')

    elif user_input == "4":
        for Type in coromon_types:
            print(average_values(Type))

    elif user_input == "5":
        print(max_and_min())
    
    elif user_input.lower() == "stop":
        break
    
    else:
        print("Invalid Input. Please Try again.")





    """
#displays a random coromon and it's stats
print(random_mon[0] +":" + "\n" + "Type:" , str(mon_stats[0]) + '\n' + "Health Points:", str(mon_stats[1]) + '\n' + "Attack:",str(mon_stats[2]) + '\n' + "Sp. Attack:",str(mon_stats[3]) + '\n' + "Defense:",str(mon_stats[4]) + '\n' + "Sp. Defense:",str(mon_stats[5]) + '\n' + "Speed:",str(mon_stats[6]) + '\n' + "Stamina Points:",str(mon_stats[7]))
    
print("The coromon types include: " + ", ".join(coromon_types) + '\n')

#displays average stats across all coromon of each type (avg stats for Fire, then Ice, then Water, etc.)
for Type in coromon_types:
    print(average_values(Type))

print(list_average_values("Ice"))


print(max_and_min())

"""
    