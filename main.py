def goAhead(m1: number, m2: number, image: Image):
    image.show_image(0)
    SuperBit.servo2(SuperBit.enServo.S1, m1)
    SuperBit.servo2(SuperBit.enServo.S2, m1)

def on_button_pressed_a():
    global v
    v = v + 0.2
    music.play_melody("C D E F G A B C5 ", 1200)
    goAhead(0,
        0,
        images.create_image("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """))
    SuperBit.music(SuperBit.enMusic.RINGTONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    rotateDegrees(15, 24)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global v
    v = v - 0.2
    music.play_melody("C5 B A G F E D C ", 1200)
    goAhead(210, 200, images.arrow_image(ArrowNames.NORTH))
input.on_button_pressed(Button.B, on_button_pressed_b)

def rotateDegrees(num: number, repeat: number):
    global index
    while index <= repeat:
        SuperBit.stepper_degree(SuperBit.enSteppers.B2, num)
        basic.pause(500)
        index += 1
distance = 0
index = 0
v = 0
WSJoyStick.joy_stick_init()

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    if distance < 10:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.HEART)
        goAhead(0, 0, images.arrow_image(ArrowNames.EAST))
    else:
        basic.show_icon(IconNames.TORTOISE)
        goAhead(210, 200, images.arrow_image(ArrowNames.WEST))
basic.forever(on_forever)
