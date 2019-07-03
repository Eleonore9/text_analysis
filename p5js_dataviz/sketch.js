let table;

function preload() {
  table = loadTable('letters_freq_en_fr_colours.csv', 'csv', 'header');
}

function setup() {
  createCanvas(1200, 600);
  noStroke();
}

function draw() {
  let x_coord = 0;
  background("#808080");
  for (i=0; i<table.getRowCount(); i++){
    letter = table.get(i, 'letter');
    freq = table.get(i, 'English');
    side = freq * 10;
    fill(table.get(i, 'colour'));
    text(letter, 30 + x_coord, 20);
    square(30 + x_coord, 30, side, 2);
    x_coord = x_coord + side + 5;
  }
}
