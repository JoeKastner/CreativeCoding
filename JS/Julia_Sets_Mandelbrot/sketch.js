var minval = -.5;
var maxval = .5;

var minSlider;
var maxSlider;


function setup() {
    createCanvas(400, 400);
    pixelDensity(1);

    minSlider = createSlider(-2.5, 0, -2.5, 0.01);
    maxSlider = createSlider(0, 2.5, 2.5, 0.01)

}

function draw() {
    var maxiterations = 50;
    var mx = map(mouseX, 0, width, 0, 1);
    var my = map(mouseY, 0, height, 0, 1);
    loadPixels();


    for (var x = 0; x < width; x++) {

        for (var y = 0; y < height; y++) {

            var a = map(x, 0, width, minSlider.value(), maxSlider.value());
            var b = map(y, 0, height, minSlider.value(), maxSlider.value());

            var ca = a;
            var cb = b;

            var n = 0;
            var z = 0;

            while (n < maxiterations) {
                var aa = a * a - b * b;
                var bb = 2 * a * b;
                a = aa + mx;
                b = bb + my;
                if (abs(a + b) > 16) {
                    break;
                }
                n++;
            }

            var bright = map(n, 0, maxiterations, 0, 255);
            if (n === maxiterations) {
                bright = 0;
            }

            var pix = (x + y * width) * 4;

            pixels[pix + 0] = bright;
            pixels[pix + 1] = bright;
            pixels[pix + 2] = bright;
            pixels[pix + 3] = 255;
        }
    }

    updatePixels();
}