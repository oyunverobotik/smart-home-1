function goAhead (m1: number, m2: number, image: Image) {
    image.showImage(0)
    SuperBit.Servo2(SuperBit.enServo.S1, m1)
    SuperBit.Servo2(SuperBit.enServo.S2, m1)
}
input.onButtonPressed(Button.A, function () {
    v = v + 0.2
    music.playMelody("C D E F G A B C5 ", 1200)
    goAhead(0, 0, images.createImage(`
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        `))
    SuperBit.Music(SuperBit.enMusic.ringtone)
})
input.onButtonPressed(Button.AB, function () {
    rotateDegrees(15, 24)
})
input.onButtonPressed(Button.B, function () {
    v = v - 0.2
    music.playMelody("C5 B A G F E D C ", 1200)
    goAhead(210, 200, images.arrowImage(ArrowNames.North))
})
function rotateDegrees (num: number, repeat: number) {
    while (index <= repeat) {
        SuperBit.StepperDegree(SuperBit.enSteppers.B2, num)
        basic.pause(500)
        index += 1
    }
}
let distance = 0
let index = 0
let v = 0
WSJoyStick.JoyStickInit()
basic.forever(function () {
    distance = sonar.ping(
    DigitalPin.P0,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    if (distance < 10) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.showIcon(IconNames.Heart)
        SuperBit.Servo2(SuperBit.enServo.S1, 0)
    } else {
        SuperBit.Servo2(SuperBit.enServo.S1, 270)
    }
})
