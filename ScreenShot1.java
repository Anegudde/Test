import java.io.IOException;

class ScreenShot1{
	public static void main(String args[]) throws IOException {
		try {
			 Process p = Runtime.getRuntime().exec("cmd /c adb shell screencap -p /sdcard/screencap.png && adb pull /sdcard/screencap.png");			 			 
		} catch (IOException e1) {
			 System.out.println("Exception Occured while capturing the screenshot");
			 e1.printStackTrace();
		}
		System.out.println("ScreenshotCaptured");

	}
}
