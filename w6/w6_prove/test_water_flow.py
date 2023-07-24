import pytest
from water_flow import pressure_loss_from_fittings,reynolds_number,pressure_loss_from_pipe_reduction

#################################################
# Step 2
#################################################



def test_pressure_loss_from_fittings():
    test_cases = [
        (0, 3, 0),
        (1.65, 0, 0),
        (1.65, 2, -0.109),
        (1.75, 2, -0.122),
        (1.75, 5, -0.306)
    ]

    for velocity, fittings, expected_loss in test_cases:
        loss = pressure_loss_from_fittings(velocity, fittings)
        assert abs(loss - expected_loss) < 0.001

    print("All test cases passed!")

# Run the test function
test_pressure_loss_from_fittings()


#################################################
# Step 4
#################################################

def test_reynolds_number():
    test_cases = [
        (0.048692, 0, 0),
        (0.048692, 1.65, 80069),
        (0.048692, 1.75, 84922),
        (0.28687, 1.65, 471729),
        (0.28687, 1.75, 500318)
    ]

    for hydraulic_diameter, fluid_velocity, expected_reynolds in test_cases:
        result = reynolds_number(hydraulic_diameter, fluid_velocity)
        assert abs(result - expected_reynolds) <= 1, f"Test failed: {result} != {expected_reynolds}"

    print("All tests passed!")

test_reynolds_number()


#################################################
# Step 5
#################################################


def test_pressure_loss_from_pipe_reduction():
    test_cases = [
        (0.28687, 0, 1, 0.048692, 0.001),
        (0.28687, 1.65, 471729, 0.048692, 0.001),
        (0.28687, 1.75, 500318, 0.048692, 0.001)
    ]
    
    for case in test_cases:
        larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, expected_loss, tolerance = case
        loss = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
        assert abs(loss - expected_loss) <= tolerance, f"Test case failed: {case}"
        print(f"Test case passed: {case}")

# Run the test function
test_pressure_loss_from_pipe_reduction()