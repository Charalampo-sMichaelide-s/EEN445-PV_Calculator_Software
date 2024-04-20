## Here goes the logic of the app.

import math

def minimum_pv_shadow_length(latitude, slope, length):
    """
    Calculate the minimum shadow length of a PV panel on December 21st.

    Inputs:
    - slope (float): The tilt angle of the PV panel from the horizontal (in degrees).
    - length (float): The length of the PV panel above the ground (in meters).
    - latitude (float): The latitude of the location (in degrees).

    Output:
    - minimum_shadow_length (float): The minimum shadow length of the PV panel (in meters).
    """
    # Solar declination on December 21st
    solar_declination_winter_solstice = -23.45  # degrees

    # We Calculate the sun elevation angle on December 21st at solar noon
    angle = 90 - latitude + solar_declination_winter_solstice


    h = length * math.sin(math.radians(slope))
 

    # Calculate the length of the shadow which will be the minimum
    minimum_shadow_length = h / math.tan(math.radians(angle))

    return minimum_shadow_length

# # Example usage
# slope = 45  # degrees
# length = 1.2  # meters
# latitude = 34  # degrees
# min_shadow_length = minimum_pv_shadow_length(latitude, slope, length )

