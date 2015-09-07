def main():
	for record in testData.dataset("addresses.tsv"):
		firstName = testData.field(record, "First Name")
		lastName = testData.field(record, "Last Name")
		address = testData.field(record, "Address")
		email = testData.field(record, "Email")
		test.log("%s %s, %s; email: %s" % (
			firstName, lastName, address, email))
		
def main2():
    # Load customers.adr and add/edit/delete addresses
    ...
    mainwindow = waitForObject("Addressbook")
    # Use the AUT's API to save the data to the AUT's directory
    mainwindow.saveAs("edited-customers.adr")
    # Copy "expected" from the AUT's directory to the test case's directory
    testData.get("expected-customers.adr")
    edited = open("edited-customers.adr").read()
    expected = open("expected-customers.adr").read()
    test.compare(edited, expected)
		
if __name__ == "__main__":
    main()		