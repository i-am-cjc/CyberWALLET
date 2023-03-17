// 55x86x.8mm
difference() {
    minkowski() {
        cylinder(h=.5, r=2);
        cube([51, 82, .5]);
    }

    translate([25.5, -2, -1]) {
        cylinder(h=2, d=20);
    }
}