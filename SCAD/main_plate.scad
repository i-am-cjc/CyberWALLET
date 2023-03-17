// 55x86x.8mm

difference () {
    minkowski() {
        cylinder(h=2.5, r=2);
        cube([51, 82, 2.5]);
    }

    translate([25.5, -2, -1]) {
        cylinder(h=10, d=20);
    }
    // 86 / 2 43 (-11) 32
    translate([30, 30, 0]) {
        color("red") {
            cube([22,54,4]);
        }
    }
    
    
// i2c screen
// 30.00 mm × 12.00 mm × 2.00 mm 
    translate([-1, 70, 0]) {
        cube([32, 12, 4]);
        translate([2,1.5,4]) {
            cube([23,9,4]);
        }
    }
    
    // buttons 6.0 x 6.2 tall legs down
    // 4.0 tall 5 tall to button 3.4diam button
    translate([5.5, 10, 0]) {
        cube([6.5, 6.5, 5]);
    }
    
    translate([55-5.5-6.5-4, 10, 0]) {
        cube([6.5, 6.5, 5]);
    }
    
    // wiring gaps for buttons
    translate([5.5, 16.5, 0]) {
        cube([40, 5, 4]);
        translate([40-6.5, 0, 0]) {
            cube([6.5, 15, 4]);
        }
    }
}


