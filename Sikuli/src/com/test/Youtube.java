package com.test;

import org.sikuli.script.FindFailed;
import org.sikuli.script.Screen;

public class Youtube {
public static void main(String[] args) throws FindFailed, InterruptedException {
	
	 // TODO Auto-generated method stub
	Screen s=new Screen();
	s.find("pause.png"); //identify pause button
	s.showClick("pause.png"); //click pause button
	System.out.println("pause button clicked");
	s.find("play.png"); //identify play button
	s.showClick("play.png"); //click play button

 }
}
