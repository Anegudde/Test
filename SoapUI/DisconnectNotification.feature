Feature: Notification messages - Display of notification message on disconnection of transducer

@URS_842
@URS_843

@CMT_DOC1384895_11.100.50.14_B

Narrative:
As a clinician 
I want to see US1 Transducer Disconnected Notification when US1 transducer is disconnected so that I can be alerted for an action to take.

Scenario: Notification Message is displayed location, height, width, text color, font size, Background color 

Given valid FHR value is displayed in the US1 uncompressed screen

When I disconnect the ultrasound transducer from the ultrasound channel

Then transducer disconnected notification displayed at bottom right of the screen And the height 50 DP and width 350 DP And the text color #FFFFFF And background color #2D64AA


Scenario: Notification message displayed followed by info icon (Note : This test case is duplicated, We can remove this scenario)

Given The valid FHR value is displayed in the US1 uncompressed screen

When I disconnect the Ultrasound connector

Then I should see notification message displayed followed by info icon
