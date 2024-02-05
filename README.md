# Structify

This code provides a function to identify the number of chord intersections given two lists: ordered radian measures of the endpoints and identifiers. Although the identifier list can be in any order, we assume that the identifiers are one-to-one with the radian measures i.e. the identifer at index i corresponds to the radian measure of an endpoint at index i. Thus, no sorting is necessary. We also assume that s_x < e_x, where x is any number assigned to a specific chord. 

The algorithm only relies on iterating through the identifier list to count intersections. Stripping the "s_" and "e_", the list is reduced to numbers denoting different chords. When the first instance (start point) of a chord is encountered, it is added to an "open_chords" list. When the second instance (end point) is encountered, we count the number of new start points added to "open_chords" since the first instance. This calculates the number of intersections. The chord value is then removed from "open_chords", as it has now closed.

The estimated big-O runtime is O(n^3).
