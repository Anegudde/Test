package com.omig.soapSamples;

import java.util.List;
import org.junit.Test;
import com.eviware.soapui.impl.wsdl.WsdlProject;
import com.eviware.soapui.model.support.PropertiesMap;
import com.eviware.soapui.model.testsuite.TestCase;
import com.eviware.soapui.model.testsuite.TestRunner;
import com.eviware.soapui.model.testsuite.TestSuite;
import com.eviware.soapui.model.testsuite.TestRunner.Status;
import com.eviware.soapui.tools.SoapUITestCaseRunner;
import static org.junit.Assert.*;
/*
 * http://thewonggei.com/2010/06/23/some-thoughts-on-integrating-soapui-functional-tests-with-your-build/
 * https://pritikaur23.wordpress.com/2013/06/16/saving-a-soapui-project-and-sending-requests-using-soapui-api/
*/
public class SoapUITest {

@Test
public void lessControl() throws Exception {
SoapUITestCaseRunner runner = new SoapUITestCaseRunner();
runner.setProjectFile("D:\\ProgApps\\SoapUI-5.2.0\\test-soapui-project.xml");
runner.setPrintReport(true);  //Outputs a small table to stdout of test results.
runner.run();
}

	@Test
	public void fullControl() throws Exception {
	WsdlProject project = new WsdlProject("Build.xml");
	List<TestSuite> testSuites = project.getTestSuiteList();
		for( TestSuite suite : testSuites ) {
		List<TestCase> testCases = suite.getTestCaseList();
			for( TestCase testCase : testCases ) {
			System.out.println("Running SoapUI test [" + testCase.getName() + "]");
			TestRunner runner2 = testCase.run(new PropertiesMap(), false);
			assertEquals(Status.FINISHED, runner2.getStatus());
			}
		}
	}
}