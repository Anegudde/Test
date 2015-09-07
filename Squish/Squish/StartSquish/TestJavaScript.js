source(findFile("scripts", "misc.js"))
 
function main() {
    test.log("" + misc.add(1, 1));
    test.log("" + misc.subtract(1, 1));
}