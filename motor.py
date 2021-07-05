import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class Motor:
    def __init__(self, values):
        self.speed = values[0]
        self.input1 = values[1]
        self.input2 = values[2]
        GPIO.setup(self.input1, GPIO.OUT)
        GPIO.setup(self.input2, GPIO.OUT)
        GPIO.setup(self.speed, GPIO.OUT)


def front(motor1, motor2):
    GPIO.output(motor1.input1, False)
    GPIO.output(motor2.input1, False)
    GPIO.output(motor1.input2, True)
    GPIO.output(motor2.input2, True)


def back(motor1, motor2):
    GPIO.output(motor1.input1, True)
    GPIO.output(motor2.input1, True)
    GPIO.output(motor1.input2, False)
    GPIO.output(motor2.input2, False)


def turnLeft(motor1, motor2):
    GPIO.output(motor1.input1, True)
    GPIO.output(motor2.input1, False)
    GPIO.output(motor1.input2, False)
    GPIO.output(motor2.input2, True)


def turnRight(motor1, motor2):
    GPIO.output(motor1.input1, False)
    GPIO.output(motor2.input1, True)
    GPIO.output(motor1.input2, True)
    GPIO.output(motor2.input2, False)


def stop(motor1, motor2):
    GPIO.output(motor1.input1, False)
    GPIO.output(motor2.input1, False)
    GPIO.output(motor1.input2, False)
    GPIO.output(motor2.input2, False)


if __name__ == "__main__":
    import time

    m1 = Motor([18, 21, 13])  # physical 12, 40, 33
    m2 = Motor([8, 19, 26])
    turnRight(m1, m2)
    time.sleep(2)
    turnLeft(m1, m2)
    time.sleep(2)
    front(m1, m2)
    time.sleep(2)
    back(m1, m2)
    time.sleep(2)
