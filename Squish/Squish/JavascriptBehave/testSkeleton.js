source(findFile("scripts", "Feature.js"));


var feature = new Feature("addressbook.feature");
 
// Scenario 1
var scenario1 = feature.addScenario("Initial state of created addressbook");
 
scenario1.Given("no prior existing addressbook", function () {
    test.log("Implement me!");
})
 
scenario1.When("I create a new addressbook", function () {
    test.log("Implement me!");
})
 
scenario1.Then("no entries should be present", function () {
    test.log("Implement me!");
})
 
// Scenario 2
var scenario2 = feature.addScenario("State after adding first entry");
 
scenario2.Given("a newly created addressbok", function () {
    test.log("Implement me!");
})
 
scenario2.When("entering the first person", function () {
    test.log("Implement me!");
})
 
scenario2.Then("one entry should be present", function () {
    test.log("Implement me!");
})
 
function main() {
   feature.execute();
}