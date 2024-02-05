
# chord intersections function
def chord_intersections(radian_measures, identifiers):
    open_chords = []
    intersections = 0
    for i in range(len(identifiers)):
        if identifiers[i][2] not in open_chords:
            open_chords.append(identifiers[i][2])
        else:
            intersections += len(open_chords[open_chords.index(identifiers[i][2]):]) - 1
            open_chords.remove(identifiers[i][2])
    return intersections


# test cases
radian_measures_test1 = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
identifiers_test1 = ["s_1","s_2","s_3","e_1","e_2", "e_3"]

radian_measures_test2 = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
identifiers_test2 = ["s_1","e_1","s_2","e_2","s_3", "e_3"]

radian_measures_test3 = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
identifiers_test3 = ["s_1","s_3","e_3","e_1","s_2", "e_2"]

radian_measures_test4 = [0.78, 1.47, 1.77, 3.92]
identifiers_test4 = ["s_1","s_2","e_1","e_2"]

radian_measures_test5 = [0.9, 1.3, 1.7, 2.92]
identifiers_test5 = ["s_1","e_1","s_2","e_2"]


#print(chord_intersections(radian_measures_test1, identifiers_test1))
#print(chord_intersections(radian_measures_test2, identifiers_test2))
#print(chord_intersections(radian_measures_test3, identifiers_test3))
#print(chord_intersections(radian_measures_test4, identifiers_test4))
#print(chord_intersections(radian_measures_test5, identifiers_test5))
