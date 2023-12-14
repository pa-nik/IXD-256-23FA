## Introduction   

Provide a description of your initial project idea and include images of the concept sketches that you created in Part 1 of this assignment.  Explain the reasoning behind your final choice of the project concept, whether it’s based on one of the initial sketches, a combination of or a departure from the original concepts.  
  
### Formatting Tips  
   
To format text into separate lines or paragraphs with [markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), include at least 2 spaces at the end.  The extra spaces act as line breaks.  

Links can be inserted with [link text in square brackets] followed by (link URL in parantheses).  For example, the markdown for [link to this page](../assignment04/) on GitHub Pages is: 
`[link to this page](../assignment04/)`  

Note the use of relative paths in links.  The dot slash `./` in link path means the file is in the current directory, `../` means that it is in parent directory, `../../` is one more directory up and so on.  
  
To insert images, the syntax is almost the same with the addition of exclamation point `!` before [image description in square brackets] followed by (image link in parentheses).  The image below is included with:  
`![led blink circuit](../class02/led_blink_bb.png)` syntax.  

![blink led circuit](../class02/led_blink_bb.png) 

## Implementation   

Explain your process of prototype development including all applicable aspects such as hardware (electronics), firmware (MicroPython code), software (HTML/CSS/JavaScript or other code), integrations (Adafruit IO, IFTTT, etc.), enclosure and mechanical design.  Use a separate subheader for each part:

### Hardware

List all the separate hardware components used in your project and briefly explain what they do.  To create a list with markdown syntax, use `-`, `*`, or `+` characters with each line of text:  
* item 1  
* item 2   
* etc.  

Include a schematic diagram image (hand-drawn is OK) showing all the wiring connections between the M5Stack AtomS3 board and other components.  

In addition, include at least one photo showing your hardware wiring.  This can be several close-ups with the goal of showing how the wiring connections are made.  

### Firmware   

Provide a link to your MicroPython code and explain a few important parts that make your prototype work.  Most likely you should explain the inputs/outputs used in your code and how they affect the behavior of the prototype.

To include code snippets, you can use the code block markdown, like this:

``` Python  
if(input_val > 1000):  # sensor value higher than threshold
   led_pin.on()  # turn on LED
```

### Software   

If applicable, explain the important software components of your project with relevant code snippets and links.  

### Integrations   

Include a link to and/or screenshots of other functional components of your project, like Adafruit IO feeds, dashboards, IFTTT applets, etc.  In general, think of your audience as someone new trying to learn how to make your project and make sure to cover anything helpful to explain the functional parts of it.

### Enclosure / Mechanical Design   

Explain how you made the enclosure or any other physical or mechanical aspects of your project with photos, screenshots of relevant files such as laser-cut patterns, 3D models, etc. (it’s great if you’re willing to share the editable source files too!)

## Project outcome  

Summarize the results of your final project implementation and include at least 2 photos of the prototype and a video walkthrough of the functioning demo.

## Conclusion  

As you wrap up the project, reflect on your experience of creating it.  Use this as an opportunity to mention any discoveries or challenges you came across along the way.  If there is anything you would have done differently, or have a chance to continue the project development given more time or resources, it’s a good way to conclude this section.

## Project references  

Please include links to any online resources like videos or tutorials that you may have found helpful in your process of implementing the prototype. If you used any substantial code from an online resource, make sure to credit the author(s) or sources.