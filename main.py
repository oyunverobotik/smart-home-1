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
    goAhead(180, 200, images.arrow_image(ArrowNames.NORTH))
input.on_button_pressed(Button.B, on_button_pressed_b)

def rotateDegrees(num: number, repeat: number):
    index = 0
    while index <= repeat:
        SuperBit.stepper_degree(SuperBit.enSteppers.B2, num)
        basic.pause(500)
        index += 1
v = 0

WSJoyStick.joy_stick_init()