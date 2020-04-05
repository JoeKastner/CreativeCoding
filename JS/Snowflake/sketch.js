let symSlider;
let sizeSlider;
// let symmetry = 12;
// let angle = 360 / symmetry;


function setup() {
    createCanvas(600, 600);
    angleMode(DEGREES);
    background(0);
    symSlider = createSlider(1, 24, 5, 1);
    sizeSlider = createSlider(0.1, 8, 1, 0.1);
    // slider.position(50, 650);
    // symSlider.style('width', '80px');
    let saveButton = createButton('save');
    saveButton.mousePressed(saveSnowFlake);
    let clearButton = createButton('clearCanvas');
    clearButton.mousePressed(clearCanvas);
}

function saveSnowFlake() {
    saveCanvas('snowflake.png');
}

function clearCanvas() {
    background(0);
}

function draw() {

    translate(width / 2, height / 2);
    if (mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
        let mx = mouseX - width / 2;
        let my = mouseY - height / 2;
        let pmx = pmouseX - width / 2;
        let pmy = pmouseY - height / 2;
        let c = map(mouseX, 0, width, 0, 175);
        r = random(255);
        g = random(255);
        b = random(255);


        if (mouseIsPressed) {

            stroke(r, 0, b, 100);
            let symmetry = symSlider.value();
            let angle = 360 / symmetry;
            for (let i = 0; i < symmetry; i++) {
                rotate(angle);
                // let d = dist(mx, my, pmx, pmy);
                // let sw = map(d, 0, 15, 15, 1);
                strokeWeight(sizeSlider.value());
                line(mx, my, pmx, pmy);
                push();
                scale(-1, 1);
                line(mx, my, pmx, pmy);
                pop();
            }
        }
    }

}