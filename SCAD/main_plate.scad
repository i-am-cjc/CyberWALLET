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
    translate([-1, 40, 0]) {
        color("red") {
            cube([53,22,4]);
        }
        translate([0, 6, 0]) {
            cube([200, 10, 4]);
        }
    }
    
    // middle 10 out of 22
    
    
    
// i2c screen
// 30.00 mm × 12.00 mm × 2.00 mm 
    translate([8, 68, 0]) {
        cube([43 , 13, 4]);
        translate([7,0,4]) {
            cube([34,13,4]);
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
        
            cube([6.5, 64.5, 4]);
        
    }
}


