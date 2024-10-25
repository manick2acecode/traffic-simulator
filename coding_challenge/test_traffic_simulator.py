import unittest
from unittest.mock import patch, MagicMock
import time
import sys

# Assuming the traffic light functions are imported from the traffic_light module
from traffic_simulator import simulate_traffic_lights, print_traffic_light, get_light_duration, light_red, light_yel, \
    light_gre, light_gre_lft

# Mocking time.sleep to avoid delays in tests
time.sleep = MagicMock()

light_red = "RED"
light_yel = "YELLOW"
light_gre = "GREEN"
light_gre_lft = "GREEN_LFT"


class TestTrafficLightSimulator(unittest.TestCase):

    @patch('builtins.input', side_effect=['10'])
    def test_get_light_duration_valid(self, mock_input):
        # Test valid input for get_light_duration.
        self.assertEqual(get_light_duration(light_red), 10)

    @patch('builtins.input', side_effect=['0', 'abc', '-5', '7'])
    def test_get_light_duration_invalid_then_valid(self, mock_input):
        # Test invalid inputs followed by a valid input for get_light_duration.
        self.assertEqual(get_light_duration(light_gre), 7)

    @patch('sys.stdout', new_callable=MagicMock)
    def test_print_traffic_light_red(self, mock_stdout):
        # Test printing the red light.
        print_traffic_light(light_red)
        mock_stdout.assert_called()

    @patch('sys.stdout', new_callable=MagicMock)
    def test_print_traffic_light_green(self, mock_stdout):
        # Test printing the green light.
        print_traffic_light(light_gre)
        mock_stdout.assert_called()

    @patch('sys.stdout', new_callable=MagicMock)
    def test_print_traffic_light_green_left(self, mock_stdout):
        # Test printing the green left turn light.#
        print_traffic_light(light_gre_lft)
        mock_stdout.assert_called()

    @patch('sys.stdout', new_callable=MagicMock)
    def test_print_traffic_light_yellow(self, mock_stdout):
        # Test printing the yellow light.#
        print_traffic_light(light_yel)
        mock_stdout.assert_called()

    @patch('builtins.input', side_effect=['15', '10'])
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=MagicMock)
    def test_simulate_traffic_lights(self, mock_stdout, mock_sleep, mock_input):
        # Test simulate_traffic_lights function to ensure it runs properly.
        with self.assertRaises(KeyboardInterrupt):
            simulate_traffic_lights()  # Simulate a keyboard interrupt after running

    @patch('builtins.input', side_effect=Exception("Test Error"))
    @patch('sys.stdout', new_callable=MagicMock)
    def test_simulator_error_handling(self, mock_stdout):
        # Test unexpected error handling in the simulator.
        with self.assertRaises(SystemExit):
            simulate_traffic_lights()
        mock_stdout.assert_any_call("Unexpected error: Test Error")


if __name__ == '__main__':
    unittest.main()
