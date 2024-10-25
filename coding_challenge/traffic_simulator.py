import time
import sys

light_red = "RED"
light_yel = "YELLOW"
light_gre = "GREEN"
light_gre_lft = "GREEN_LFT"


def simulate_traffic_lights():
    try:
        print("One Way Traffic Light Simulator")

        # Get durations for each light
        red_duration = get_light_duration(light_red)
        green_duration = get_light_duration(light_gre)
        # set yellow duration to be 5 seconds
        yellow_duration = 5

        print("Traffic Light Simulation Starting... (Press Ctrl+C to EXIT)\n")
        # Iterates non-stop, until keyboard interrupted
        while True:
            print("Red means STOP:")
            print_traffic_light(light_red)
            time.sleep(red_duration)

            print("Green means GO with Turn Left:")
            print_traffic_light(light_gre_lft)
            green_dur_lft = green_duration / 2
            time.sleep(green_dur_lft)

            print("Green Turn Left is OFF")
            print_traffic_light(light_gre)
            time.sleep(green_dur_lft)

            print("Yellow means WATCH:")
            print_traffic_light(light_yel)
            for number in range(yellow_duration, 0, -1):
                print(f"{number}")
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nTraffic Light Simulator Interrupted.. EXITING!")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Traffic Light Simulator shutting down safely.")
        sys.exit(1)


def print_traffic_light(color):
    print("      ##")
    print("      ##")
    print("    ######")
    print("  ##########")
    print("  ##      ##")
    print("  ##   R  ##" if color == light_red else "  ##      ##")
    print("  ##      ##")
    print("  ##########")
    print("  ##      ##")
    print("  ##   Y  ##" if color == light_yel else "  ##      ##")
    print("  ##      ##")
    print("  ##########")
    print("  ##      ##")
    if color == light_gre or color == light_gre_lft:
        print("  ## <-G  ##" if color == light_gre_lft else "  ##   G  ##")
    else:
        print("  ##      ##")
    print("  ##      ##")
    print("  ##########")
    print("    ######")


def get_light_duration(light):
    while True:
        try:
            duration = int(input(f"Enter duration for {light.upper()} light in seconds: "))
            if duration > 0:
                return duration
            else:
                print(f"{light.upper()} light duration should be greater than 0 seconds.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    simulate_traffic_lights()
