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
    goAhead(180, 200, images.arrowImage(ArrowNames.North))
})
function rotateDegrees (num: number, repeat: number) {
    while (index <= repeat) {
        SuperBit.StepperDegree(SuperBit.enSteppers.B2, num)
        basic.pause(500)
        index += 1
    }
}
let index = 0
let v = 0
WSJoyStick.JoyStickInit()
