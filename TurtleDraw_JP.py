import turtle
import math

def main():
    # =========================
    # Requirement 1: Setup
    # =========================
    screen = turtle.Screen()
    screen.setup(width=450, height=450)

    t = turtle.Turtle()
    t.speed(0)  # maximum speed

    # =========================
    # Requirement 2: File input
    # =========================
    filename = input("Enter input file name: ")

    try:
        file = open(filename, "r")
    except:
        print("Error: Could not open file.")
        input("Press Enter to exit...")
        return

    # =========================
    # Variables
    # =========================
    first_point = True
    prev_x = None
    prev_y = None
    total_distance = 0

    # =========================
    # Process file
    # =========================
    for line in file:
        line = line.strip()

        if line == "":
            continue

        parts = line.split()

        # Handle "stop"
        if parts[0].lower() == "stop":
            t.penup()
            prev_x = None
            prev_y = None
            first_point = True
            continue

        # Format: color x y
        color = parts[0]
        x = float(parts[1])
        y = float(parts[2])

        # Move to first point without drawing
        if first_point:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.color(color)
            first_point = False
        else:
            t.color(color)
            t.goto(x, y)

        # Calculate distance (only connected points)
        if prev_x is not None and prev_y is not None:
            distance = math.sqrt((x - prev_x)**2 + (y - prev_y)**2)
            total_distance += distance

        prev_x = x
        prev_y = y

    # =========================
    # Requirement 4: Cleanup
    # =========================
    file.close()

    # Display total distance (bottom right)
    t.penup()
    t.goto(120, -200)
    t.write(f"Total Distance: {total_distance:.2f}",
            font=("Arial", 10, "normal"))

    # Wait for user in terminal
    input("Press Enter to close...")

    # Keep window open until click (FIXED crash issue)
    screen.exitonclick()


if __name__ == "__main__":
    main()