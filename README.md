Indigenous Students
Write a Python script that uses plotly create a bar plot showing the mean percentage of indigenous students for each Australian Statistical Geography Standard (ASGS) Remoteness region.
Your script must ask the user to enter the ASGS regions to be included in the plot. These are to be entered as shorthand codes with the following mapping
MC - Major Cities of Australia
IR - Inner Regional Australia
OR - Outer Regional Australia
R - Remote Australia
VR - Very Remote Australia
Requirements
Your program must only produce a figure if two or more codes are entered.
If an invalid code is entered an error must be displayed and the user will be allowed to try again.
Your script must contain an object called fig that holds the plotly figure object
You must use px.bar to create the figure
