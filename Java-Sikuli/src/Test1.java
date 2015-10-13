//package com.test;

import org.junit.Test;
import org.sikuli.script.FindFailed;

import org.sikuli.script.Screen;
public class Test1 {
@Test
public  void openFileTest() throws FindFailed, InterruptedException {
	// TODO Auto-generated method stub
	Screen s=new Screen();
	s.find("file.png");
	s.doubleClick("file.png");
	System.out.println("File icon clicked");

}
}
