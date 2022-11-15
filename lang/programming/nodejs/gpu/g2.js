const { GPU } = require('gpu.js')

const gpu = new GPU()
const kernel = gpu.createKernel(function (data, activeColor) {
    const x = this.thread.x, y = this.thread.y, n = 4 *
        (x +
            this.constants.w *
                (this.constants.h - y))
    let red = data[n], green = data[n + 1], blue = data[n + 2], alpha = data[n + 3]
    const isTranslucent = alpha > 0 && alpha < 256
    if (isTranslucent) {
        red = activeColor[0]
        green = activeColor[1]
        blue = activeColor[2]
        alpha = 256
    }
    this.color(red / 256, green / 256, blue / 256, alpha / 256)
})
    .setConstants({ w: 1, h: 1 })
    .setDynamicOutput(true)
    .setGraphical(true)

    kernel.setOutput([1, 1])
    kernel([1], [1,1,1])