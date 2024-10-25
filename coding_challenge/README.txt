####### Program Execution ######

    Python should be installed before running below commands

    'time' and 'sys' are core libraries of python, so no special installation required

    1. Running Traffic Simulator -- PYTHONPATH=../:. python traffic_simulator.py

    2. Running Test Traffic Simulator -- PYTHONPATH=../:. python test_traffic_simulator.py

####### Development traffic_simulator ######

1. simulate_traffic_lights() - Main method that has the logic for traffic light simulation which internally calls 2 and 3
                               Starts with Red light with the number of seconds,
                               then turns Green with Left turn for half the duration, say 20 seconds for Green as input, 10 with Left turn
                               then Yellow runs for 5 seconds then turns back to Red
                               This circle runs until a Keyboard Interrupt happens
2. get_light_duration() - Method to get the number of seconds to stay active for red and green
3. print_traffic_light() - prints a simple graphic visual to show which light is active

####### Unit Test Cases test_traffic_simulator ######

1. test_get_light_duration_valid()              - valid number with 10 seconds run
2. test_get_light_duration_invalid_then_valid() - provide an invalid input to
3. test_print_traffic_light_red()               - validate red light seconds
4. test_print_traffic_light_green()             - validate green light seconds
5. test_print_traffic_light_green_left()        - validate green left light seconds
6. test_print_traffic_light_yellow()            - validate yellow light seconds
7. test_simulate_traffic_lights()               - validate keyboard interrupt
8. test_simulator_error_handling()              - validate error handling
