# synthetic data for ped ped interaction // no obstacles
# up to 4 pedestrians coming from different random(pseudo) directions
# random start and end points
# initial speed is set to be same for everyone
# if one pedestrian is not present start and end would be both [0, 0]

import random
import math
import pandas as pd
import numpy as np

ped_count = []
in_group, in_group1, in_group2, in_group3, in_group4, in_group5, in_group6 = [], [], [], [], [], [], []
in_group7, in_group8, in_group9, in_group10 = [], [], [], []

start_x1, start_y1, start_x2, start_y2, start_x3, start_y3 = [], [], [], [], [], []
start_x4, start_y4, start_x5, start_y5, start_x6, start_y6 = [], [], [], [], [], []
start_x7, start_y7, start_x8, start_y8, start_x9, start_y9, start_x10, start_y10 = [], [], [], [], [], [], [], []

goal_x1, goal_y1, goal_x2, goal_y2, goal_x3, goal_y3, goal_x4, goal_y4 = [], [], [], [], [], [], [], []
goal_x5, goal_y5, goal_x6, goal_y6, goal_x7, goal_y7, goal_x8, goal_y8 = [], [], [], [], [], [], [], []
goal_x9, goal_y9, goal_x10, goal_y10 = [], [], [], []

velocity_x1, velocity_x2, velocity_x3, velocity_x4, velocity_x5 = [], [], [], [], []
velocity_x6, velocity_x7, velocity_x8, velocity_x9, velocity_x10 = [], [], [], [], []

velocity_start = 0.5

random.seed(1)
choice_set_direction = np.array([1, 2, 3, 4])

choice_set_number = [2, 3, 4, 5, 6, 7, 8, 9, 10]
group_present = [0, 1]
group_size = [2, 3, 4]

for x in range(1002):
    choice_ped_no = random.choice(choice_set_number)
    print(choice_ped_no)
    group_exists = random.choice(group_present)
    in_group.append(group_exists)
    count = 1
    ped_count.append(choice_ped_no)
    group_size2 = random.choice(group_size)
    if group_exists == 1:
        # group_size2 = random.choice(group_size)
        if group_size2 >= choice_ped_no:
            group_size2 = choice_ped_no

        choice_set_direction_final = random.choice(choice_set_direction)
        if choice_set_direction_final == 1:  # down to up
            choice_set_direction2 = np.delete(choice_set_direction, 0)
            choice_set_end = random.choice(choice_set_direction2)
        elif choice_set_direction_final == 2:  # up to down
            choice_set_direction2 = np.delete(choice_set_direction, 1)
            choice_set_end = random.choice(choice_set_direction2)
        elif choice_set_direction_final == 3:  # 3
            choice_set_direction2 = np.delete(choice_set_direction, 2)
            choice_set_end = random.choice(choice_set_direction2)
        else:
            choice_set_direction2 = np.delete(choice_set_direction, 3)
            choice_set_end = random.choice(choice_set_direction2)

        for x in range(group_size2):
            if choice_set_direction_final == 1:  # down to up
                temp_s_x = round(random.uniform(2.6, 3.0), 2)
                temp_s_y = round(random.uniform(0.6, 1), 2)
                velocity_temp = velocity_start

            elif choice_set_direction_final == 2:  # up to down
                temp_s_x = round(random.uniform(-2.7, -2.3), 2)
                temp_s_y = round(random.uniform(5.1, 5.5), 2)
                velocity_temp = velocity_start

            elif choice_set_direction_final == 3:  # 3
                temp_s_x = round(random.uniform(2.6, 3.0), 2)
                temp_s_y = round(random.uniform(10.1, 10.5), 2)
                velocity_temp = -velocity_start

            else:
                temp_s_x = round(random.uniform(8.1, 8.5), 2)
                temp_s_y = round(random.uniform(5.1, 5.5), 2)
                velocity_temp = -velocity_start

            if choice_set_end == 1:
                temp_g_x = round(random.uniform(2.6, 3.0), 2)
                temp_g_y = round(random.uniform(0.6, 1), 2)
            elif choice_set_end == 2:
                temp_g_x = round(random.uniform(-2.7, -2.3), 2)
                temp_g_y = round(random.uniform(5.1, 5.5), 2)
            elif choice_set_end == 3:
                temp_g_x = round(random.uniform(2.6, 3.0), 2)
                temp_g_y = round(random.uniform(10.1, 10.5), 2)
            else:
                temp_g_x = round(random.uniform(8.1, 8.5), 2)
                temp_g_y = round(random.uniform(5.1, 5.5), 2)

            if count == 1:
                start_x1.append(temp_s_x), start_y1.append(temp_s_y)
                goal_x1.append(temp_g_x), goal_y1.append(temp_g_y)
                velocity_x1.append(velocity_temp), in_group1.append(1)
            elif count == 2:
                start_x2.append(temp_s_x), start_y2.append(temp_s_y)
                goal_x2.append(temp_g_x), goal_y2.append(temp_g_y)
                velocity_x2.append(velocity_temp), in_group2.append(1)
            elif count == 3:
                start_x3.append(temp_s_x), start_y3.append(temp_s_y)
                goal_x3.append(temp_g_x), goal_y3.append(temp_g_y)
                velocity_x3.append(velocity_temp), in_group3.append(1)
            else:
                start_x4.append(temp_s_x), start_y4.append(temp_s_y)
                goal_x4.append(temp_g_x), goal_y4.append(temp_g_y)
                velocity_x4.append(velocity_temp), in_group4.append(1)

            count += 1

    d_set_temp = []
    if group_exists == 1:
        if group_size2 >= choice_ped_no:
            remaining_peds = 0
        else:
            remaining_peds = choice_ped_no - group_size2
    else:
        remaining_peds = choice_ped_no
    for n in range(remaining_peds):
        choice_set_direction_final = random.choice(choice_set_direction)

        if choice_set_direction_final == 1:  # down to up
            temp_s_x = round(random.uniform(1.0, 5.0), 2)
            temp_s_y = round(random.uniform(0.5, 1), 2)
            choice_set_direction2 = np.delete(choice_set_direction, 0)
            choice_set_end = random.choice(choice_set_direction2)

            # temp_g_x = round(random.uniform(1.0, 4.0), 2)
            # temp_g_y = round(random.uniform(8.5, 10.5), 2)
            velocity_temp = velocity_start
            if choice_set_end == 1:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(0.5, 1.0), 2)
            elif choice_set_end == 2:
                temp_g_x = round(random.uniform(-3.0, -2.0), 2)
                temp_g_y = round(random.uniform(4.0, 6.0), 2)
            elif choice_set_end == 3:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(10.0, 10.5), 2)
            else:
                temp_g_x = round(random.uniform(8.0, 8.5), 2)
                temp_g_y = round(random.uniform(4.0, 6.0), 2)

        elif choice_set_direction_final == 2:  # up to down
            temp_s_x = round(random.uniform(-3.0, -2.0), 2)
            temp_s_y = round(random.uniform(3.5, 7.5), 2)
            choice_set_direction2 = np.delete(choice_set_direction, 1)
            choice_set_end = random.choice(choice_set_direction2)

            # temp_g_x = round(random.uniform(1.0, 4.0), 2)
            # temp_g_y = round(random.uniform(0.5, 2.5), 2)
            velocity_temp = -velocity_start
            if choice_set_end == 1:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(0.5, 1), 2)
            elif choice_set_end == 2:
                temp_g_x = round(random.uniform(-3.0, -2.0), 2)
                temp_g_y = round(random.uniform(3.5, 7.5), 2)
            elif choice_set_end == 3:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(10.0, 10.5), 2)
            else:
                temp_g_x = round(random.uniform(8.0, 8.5), 2)
                temp_g_y = round(random.uniform(3.5, 7.5), 2)

        elif choice_set_direction_final == 3:  # 3
            # # start_x = (1, 2), end_x= (4, 5),, start_y = (0.75, 2.75), end_X = (8.75, 11.25)
            temp_s_x = round(random.uniform(1.0, 5.0), 2)
            temp_s_y = round(random.uniform(10.0, 10.5), 2)
            choice_set_direction2 = np.delete(choice_set_direction, 2)
            choice_set_end = random.choice(choice_set_direction2)

            velocity_temp = velocity_start
            if choice_set_end == 1:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(0.5, 1), 2)
            elif choice_set_end == 2:
                temp_g_x = round(random.uniform(-3.0, -2.0), 2)
                temp_g_y = round(random.uniform(3.5, 7.5), 2)
            elif choice_set_end == 3:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(10.0, 10.5), 2)
            else:
                temp_g_x = round(random.uniform(8.0, 8.5), 2)
                temp_g_y = round(random.uniform(3.5, 7.5), 2)

        else:
            temp_s_x = round(random.uniform(8.0, 8.5), 2)
            temp_s_y = round(random.uniform(3.5, 7.5), 2)
            choice_set_direction2 = np.delete(choice_set_direction, 3)
            choice_set_end = random.choice(choice_set_direction2)
            velocity_temp = -velocity_start
            if choice_set_end == 1:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(0.5, 1), 2)
            elif choice_set_end == 2:
                temp_g_x = round(random.uniform(-3.0, -2.0), 2)
                temp_g_y = round(random.uniform(3.5, 7.5), 2)
            elif choice_set_end == 3:
                temp_g_x = round(random.uniform(1.0, 5.0), 2)
                temp_g_y = round(random.uniform(10.0, 10.5), 2)
            else:
                temp_g_x = round(random.uniform(8.0, 8.5), 2)
                temp_g_y = round(random.uniform(3.5, 7.5), 2)

        if count == 1:
            start_x1.append(temp_s_x), start_y1.append(temp_s_y), goal_x1.append(temp_g_x)
            goal_y1.append(temp_g_y), velocity_x1.append(velocity_temp), in_group1.append(0)
        elif count == 2:
            start_x2.append(temp_s_x), start_y2.append(temp_s_y), goal_x2.append(temp_g_x)
            goal_y2.append(temp_g_y), velocity_x2.append(velocity_temp), in_group2.append(0)
        elif count == 3:
            start_x3.append(temp_s_x), start_y3.append(temp_s_y), goal_x3.append(temp_g_x)
            goal_y3.append(temp_g_y), velocity_x3.append(velocity_temp), in_group3.append(0)
        elif count == 4:
            start_x4.append(temp_s_x), start_y4.append(temp_s_y), goal_x4.append(temp_g_x)
            goal_y4.append(temp_g_y), velocity_x4.append(velocity_temp), in_group4.append(0)
        elif count == 5:
            start_x5.append(temp_s_x), start_y5.append(temp_s_y), goal_x5.append(temp_g_x)
            goal_y5.append(temp_g_y), velocity_x5.append(velocity_temp), in_group5.append(0)
        elif count == 6:
            start_x6.append(temp_s_x), start_y6.append(temp_s_y)
            goal_x6.append(temp_g_x), goal_y6.append(temp_g_y)
            velocity_x6.append(velocity_temp), in_group6.append(0)
        elif count == 7:
            start_x7.append(temp_s_x), start_y7.append(temp_s_y)
            goal_x7.append(temp_g_x), goal_y7.append(temp_g_y)
            velocity_x7.append(velocity_temp), in_group7.append(0)
        elif count == 8:
            start_x8.append(temp_s_x), start_y8.append(temp_s_y)
            goal_x8.append(temp_g_x), goal_y8.append(temp_g_y)
            velocity_x8.append(velocity_temp), in_group8.append(0)
        elif count == 9:
            start_x9.append(temp_s_x), start_y9.append(temp_s_y)
            goal_x9.append(temp_g_x), goal_y9.append(temp_g_y)
            velocity_x9.append(velocity_temp), in_group9.append(0)
        else:
            start_x10.append(temp_s_x), start_y10.append(temp_s_y)
            goal_x10.append(temp_g_x), goal_y10.append(temp_g_y)
            velocity_x10.append(velocity_temp), in_group10.append(0)

        count += 1
    if choice_ped_no < 3:
        start_x3.append(0), start_y3.append(0), goal_x3.append(0), goal_y3.append(0)
        start_x4.append(0), start_y4.append(0), goal_x4.append(0), goal_y4.append(0)
        start_x5.append(0), start_y5.append(0), goal_x5.append(0), goal_y5.append(0)
        start_x6.append(0), start_y6.append(0), goal_x6.append(0), goal_y6.append(0)
        start_x7.append(0), start_y7.append(0), goal_x7.append(0), goal_y7.append(0)
        start_x8.append(0), start_y8.append(0), goal_x8.append(0), goal_y8.append(0)
        start_x9.append(0), start_y9.append(0), goal_x9.append(0), goal_y9.append(0)
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0)
        velocity_x3.append(0), velocity_x4.append(0), velocity_x5.append(0), velocity_x6.append(0)
        velocity_x7.append(0), velocity_x8.append(0), velocity_x9.append(0), velocity_x10.append(0)
        in_group3.append(0), in_group4.append(0), in_group5.append(0), in_group6.append(0)
        in_group7.append(0), in_group8.append(0), in_group9.append(0), in_group10.append(0)

    elif choice_ped_no < 4:
        start_x4.append(0), start_y4.append(0), goal_x4.append(0), goal_y4.append(0), velocity_x4.append(0)
        start_x5.append(0), start_y5.append(0), goal_x5.append(0), goal_y5.append(0), velocity_x5.append(0)
        start_x6.append(0), start_y6.append(0), goal_x6.append(0), goal_y6.append(0), velocity_x6.append(0)
        start_x7.append(0), start_y7.append(0), goal_x7.append(0), goal_y7.append(0), velocity_x7.append(0)
        start_x8.append(0), start_y8.append(0), goal_x8.append(0), goal_y8.append(0), velocity_x8.append(0)
        start_x9.append(0), start_y9.append(0), goal_x9.append(0), goal_y9.append(0), velocity_x9.append(0)
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0), velocity_x10.append(0)
        in_group4.append(0), in_group5.append(0), in_group6.append(0), in_group7.append(0)
        in_group8.append(0), in_group9.append(0), in_group10.append(0)

    elif choice_ped_no < 5:
        start_x5.append(0), start_y5.append(0), goal_x5.append(0), goal_y5.append(0), velocity_x5.append(0)
        start_x6.append(0), start_y6.append(0), goal_x6.append(0), goal_y6.append(0), velocity_x6.append(0)
        start_x7.append(0), start_y7.append(0), goal_x7.append(0), goal_y7.append(0), velocity_x7.append(0)
        start_x8.append(0), start_y8.append(0), goal_x8.append(0), goal_y8.append(0), velocity_x8.append(0)
        start_x9.append(0), start_y9.append(0), goal_x9.append(0), goal_y9.append(0), velocity_x9.append(0)
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0), velocity_x10.append(0)
        in_group5.append(0), in_group6.append(0), in_group7.append(0)
        in_group8.append(0), in_group9.append(0), in_group10.append(0)

    elif choice_ped_no < 6:
        start_x6.append(0), start_y6.append(0), goal_x6.append(0), goal_y6.append(0), velocity_x6.append(0)
        start_x7.append(0), start_y7.append(0), goal_x7.append(0), goal_y7.append(0), velocity_x7.append(0)
        start_x8.append(0), start_y8.append(0), goal_x8.append(0), goal_y8.append(0), velocity_x8.append(0)
        start_x9.append(0), start_y9.append(0), goal_x9.append(0), goal_y9.append(0), velocity_x9.append(0)
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0), velocity_x10.append(0)
        in_group6.append(0), in_group7.append(0), in_group8.append(0), in_group9.append(0), in_group10.append(0)

    elif choice_ped_no < 7:
        start_x7.append(0), start_y7.append(0), goal_x7.append(0), goal_y7.append(0), velocity_x7.append(0)
        start_x8.append(0), start_y8.append(0), goal_x8.append(0), goal_y8.append(0), velocity_x8.append(0)
        start_x9.append(0), start_y9.append(0), goal_x9.append(0), goal_y9.append(0), velocity_x9.append(0)
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0), velocity_x10.append(0)
        in_group7.append(0), in_group8.append(0), in_group9.append(0), in_group10.append(0)

    elif choice_ped_no < 8:
        start_x8.append(0), start_y8.append(0), goal_x8.append(0), goal_y8.append(0), velocity_x8.append(0)
        start_x9.append(0), start_y9.append(0), goal_x9.append(0), goal_y9.append(0), velocity_x9.append(0)
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0), velocity_x10.append(0)
        in_group8.append(0), in_group9.append(0), in_group10.append(0)

    elif choice_ped_no < 9:
        start_x9.append(0), start_y9.append(0), goal_x9.append(0), goal_y9.append(0), velocity_x9.append(0)
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0), velocity_x10.append(0)
        in_group9.append(0), in_group10.append(0)

    elif choice_ped_no < 10:
        start_x10.append(0), start_y10.append(0), goal_x10.append(0), goal_y10.append(0), velocity_x10.append(0)
        in_group10.append(0)


dict1 = {"ped_count": ped_count, "in_group": in_group, "start_x1": start_x1, "start_y1": start_y1, "start_x2": start_x2,
         "start_y2": start_y2, "start_x3": start_x3,
         "start_y3": start_y3, "start_x4": start_x4, "start_y4": start_y4, "start_x5": start_x5, "start_y5": start_y5,
         "start_x6": start_x6, "start_y6": start_y6, "start_x7": start_x7, "start_y7": start_y7,
         "start_x8": start_x8, "start_y8": start_y8, "start_x9": start_x9, "start_y9": start_y9,
         "start_x10": start_x10, "start_y10": start_y10,
         "goal_x1": goal_x1, "goal_y1": goal_y1,
         "goal_x2": goal_x2, "goal_y2": goal_y2, "goal_x3": goal_x3, "goal_y3": goal_y3, "goal_x4": goal_x4,
         "goal_y4": goal_y4, "goal_x5": goal_x5, "goal_y5": goal_y5,
         "goal_x6": goal_x6, "goal_y6": goal_y6, "goal_x7": goal_x7, "goal_y7": goal_y7,
         "goal_x8": goal_x8, "goal_y8": goal_y8, "goal_x9": goal_x9, "goal_y9": goal_y9,
         "goal_x10": goal_x10, "goal_y10": goal_y10,
         "vel_1": velocity_x1, "vel_2": velocity_x2,
         "vel_3": velocity_x3, "vel_4": velocity_x4, "vel_5": velocity_x5,
         "vel_6": velocity_x6, "vel_7": velocity_x7, "vel_8": velocity_x8,
         "vel_9": velocity_x9, "vel_10": velocity_x10,
         "in_group1": in_group1, "in_group2": in_group2, "in_group3": in_group3,
         "in_group4": in_group4, "in_group5": in_group5, "in_group6": in_group6,
         "in_group7": in_group7, "in_group8": in_group8,
         "in_group9": in_group9, "in_group10": in_group10}

tempDf = pd.DataFrame(dict1, columns=["ped_count", "in_group", "start_x1", "start_y1", "start_x2", "start_y2", "start_x3",
                                      "start_y3", "start_x4", "start_y4", "start_x5", "start_y5",
                                      "start_x6", "start_y6", "start_x7", "start_y7",
                                      "start_x8", "start_y8", "start_x9", "start_y9", "start_x10", "start_y10",
                                      "goal_x1","goal_y1", "goal_x2", "goal_y2",
                                      "goal_x3", "goal_y3", "goal_x4", "goal_y4", "goal_x5", "goal_y5",
                                      "goal_x6", "goal_y6", "goal_x7", "goal_y7", "goal_x8", "goal_y8",
                                      "goal_x9", "goal_y9", "goal_x10", "goal_y10",
                                      "vel_1", "vel_2", "vel_3", "vel_4", "vel_5",
                                      "vel_6", "vel_7", "vel_8", "vel_9", "vel_10",
                                      "in_group1", "in_group2", "in_group3", "in_group4", "in_group5",
                                      "in_group6", "in_group7", "in_group8", "in_group9", "in_group10"])

tempDf.to_csv("synthetic_data_cpp_group_new_1011.csv", index=False)
print("done")

