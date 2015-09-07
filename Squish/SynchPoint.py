def main():
	ok = waitFor("object.exists(':Address Book - Save As_QFileDialog')", 5000)
	if not ok:
		test.fatal("AddressBook Save As dialog didn't appear")
	
if __name__ == "__main__":
    main()
	
#squishrunner --testsuite /home/reggie/suite_addressbook --testcase tst_add_address --testcase tst_edit_address
#squishrunner --testsuite /home/reggie/suite_addressbook --record tst_search_for_address --useWaitFor
#quishrunner --testcase tst_update_address --aut addressbook