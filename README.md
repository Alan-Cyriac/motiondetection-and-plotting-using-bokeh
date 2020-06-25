# motiondetection-and-plotting-using-bokeh

At first when the cam on it will take a picture and that would be the reference.<br />
if any frame doesnot match to the reference frame, it will count as a motion and store the start time and end time in a CSV file.<br />
Atlast, When the camera is turned off by pressing 'q',<br />
the program will display the time that detect the motion in a bokeh graph from the data stored in the csv file.<br />

Libraries used:<br />
cv2, bokeh, pandas
