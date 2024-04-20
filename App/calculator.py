import math

def minimum_pv_shadow_length(latitude, slope, height):
    """
    Calculate the minimum shadow length of a PV panel on December 21st.

    Inputs:
    - slope (float): The tilt angle of the PV panel from the horizontal (in degrees).
    - height (float): The height of the PV panel above the ground (in meters).
    - latitude (float): The latitude of the location (in degrees).

    Output:
    - minimum_shadow_length (float): The minimum shadow length of the PV panel (in meters).
    """
    # Solar declination on December 21st
    solar_declination_winter_solstice = -23.45  # degrees

    # We Calculate the sun elevation angle on December 21st at solar noon
    angle = 90 - latitude + solar_declination_winter_solstice

    # Calculate the length of the shadow which will be the minimum
    minimum_shadow_length = height / math.tan(math.radians(angle - slope))

    return minimum_shadow_length

# # Example usage
# slope = 2  # degrees
# height = 1.2  # meters
# latitude = 34  # degrees
# if __name__ == "__main__":
#     min_shadow_length = minimum_pv_shadow_length(slope, height, latitude)

