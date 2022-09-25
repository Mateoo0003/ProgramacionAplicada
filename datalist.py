'''
STATES: Outputs
S1 = [1,0,0,0,0] -> filling
S2 = [0,0,0,1,1] -> heating water for 20 minutes
S3 = [0,0,1,0,0] -> emptying 
S4 = [0,1,0,0,0] -> filling tank w second valve

EVENTS: Inputs 
O1 = [0,1,0,0,0] -> fill the main tank til first level
O2 = [0,0,0,1,1] -> water boiling after 20 minutes
O3 = [1,0,0,0,0] -> empty the main tank
O4 = [0,0,0,0,1] -> past 20 minutes the water is not hot
'''

input_test_data = (
    (6, 0), (7, 1), (8, 0), (9, 0), (10, 0),
    (6, 0), (7, 0), (8, 0), (9, 1), (10, 1),
    (6, 1), (7, 0), (8, 1), (9, 0), (10, 0),
    (6, 0), (7, 0), (8, 0), (9, 0), (10, 1)
)

input_cont = 0


def input_test(gp_req):
    global input_cont
    gp_test, val_test = input_test_data[input_cont]
    assert gp_test == gp_req, f'The input required GP {gp_req} is different from the test GP {gp_test} in {input_cont}'
    input_cont += 1
    if len(input_test_data) <= input_cont:
        raise Exception(f'No more test data')
    return val_test


output_test_data = (
    (17, 1), (18, 0), (19, 0), (20, 0), (21, 0),
    (17, 0), (18, 0), (19, 0), (20, 1), (21, 1),
    (17, 0), (18, 0), (19, 1), (20, 0), (21, 0),
    (17, 0), (18, 1), (19, 0), (20, 0), (21, 0),
)

output_cont = 0


def output_test(gp_req, val_req):
    global output_cont
    gp_test, val_test = output_test_data[output_cont]
    assert gp_test == gp_req, f'The output required GP {gp_req} is different from the test GP {gp_test} in {output_cont}'
    assert val_test == val_req, f'The required value {val_req} is different from the test value {val_test} in {output_cont}'
    output_cont += 1
    if len(output_test_data) <= output_cont:
        raise Exception(f'No more test data')
