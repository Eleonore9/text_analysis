let table;

function preload() {
  table = loadTable('letters_freq_en_vs_fr.csv', 'csv', 'header');
}

function setup() {
  createCanvas(600, 600);
  noStroke();
}

let data = [{letter: "a", freq: 8},
            {letter: "b", freq: 1},
            {letter: "c", freq: 3}];
let colours = ["#47aef7", "#43cc8c", "#f2ec7d", "#cf84f4", "#f280d0", "#", "#",
              "#", "#", "#", "#", "#", "#",
              "#", "#","#", "#","#", "#", "#",
              "#", "#","#", "#","#", "#"];

function draw() {
  let x_coord = 0;
  background("#424040");
  for (i=0; i<table.getRowCount(); i++){
    letter = table.getColumn('letter');
    freq = table.getColumn('English');
    side = freq * 10;
    fill(colours[i]);
    text(letter, 30 + x_coord, 20);
    square(30 + x_coord, 30, side, 2);
    x_coord = x_coord + side + 3;
  }
}