
function Application() {
    this.launch = function() {
        startApplication("AddressBook.class");
    }
    this.createAddressbook = function() {
        activateItem(waitForObjectItem(":Address Book_JMenuBar",
                                   "File"));
        activateItem(waitForObjectItem(":File_JMenu", "New..."));
    }
    this.addDummyEntry = function() {
        activateItem(waitForObjectItem(
                     ":Address Book - Unnamed_JMenuBar", "Edit"));
        activateItem(waitForObjectItem(":Edit_JMenu", "Add..."));
        type(waitForObject(":Address Book – Add.Forename:_JTextField"),
                           "Mike");
        type(waitForObject(":Address Book – Add.Forename:_JTextField"),
                           "<Tab>");
        type(waitForObject(":Address Book – Add.Surname:_JTextField"),
                           "Meyers");
        type(waitForObject(":Address Book – Add.Surname:_JTextField"),
                           "<Tab>");
        type(waitForObject(":Address Book – Add.Email:_JTextField"),
                           "mike@example.com");
        type(waitForObject(":Address Book – Add.Email:_JTextField"),
                           "<Tab>");
        type(waitForObject(":Address Book – Add.Phone:_JTextField"),
                           "0123/456789");
        clickButton(waitForObject(":Address Book - Add.OK_JButton"));
    }
    this.countEntries = function() {
        return findObject(":Address Book - Unnamed_JTable").rowcount;
    }
}