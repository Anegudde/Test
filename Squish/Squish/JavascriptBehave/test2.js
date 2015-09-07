source(findFile("scripts", "Feature.js"));
source(findFile("scripts", "Application.js"));
 
var feature = new Feature("addressbook.feature");
 
// Scenario 1
var scenario1 = feature.addScenario("Initial state of created addressbook");
 
scenario1.Given("no prior existing addressbook", function () {
    this.scenario.application = new Application();
    this.scenario.application.launch();
})
 
scenario1.When("I create a new addressbook", function () {
    this.scenario.application.createAddressbook();
})
 
scenario1.Then("no entries should be present", function () {
    test.compare(this.scenario.application.countEntries(), 0);
})
 
// Scenario 2
var scenario2 = feature.addScenario("State after adding first entry");
 
scenario2.Given("a newly created addressbok", function () {
    this.scenario.application = new Application();
    this.scenario.application.launch();
    this.scenario.application.createAddressbook();
})
 
scenario2.When("entering the first person", function () {
    this.scenario.application.addDummyEntry();
})
 
scenario2.Then("one entry should be present", function () {
    test.compare(this.scenario.application.countEntries(), 1);
})
 
function main() {
   feature.execute();
}