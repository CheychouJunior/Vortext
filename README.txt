### User Manual or User Guide (Provides instructions on how to install, configure and use the software) ###

Program Name: Vortext

Vortext is a video media player with advanced functionalities such as text extraction from videos and a built-in text editor for modifying and saving extracted text. 

Copyright (C) 2023 

Released under the GNU General Public License by a team comprising Nikoum Modeste Lorene, Pollah yves,Cheychou Mouafo Junior, and Sibafo Wisdom.

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
Introduction,
System Requirements,
Installation instructions,
Getting Started (How to use the player),
Text Extraction Features,
Troubleshooting,
FAQs,

Introduction
    Have you ever wanted to copy a text directly from a video rather than rewriting it? 
    If yes, then you are at the right place.
    Vortext is a desktop application which is made up of a video media player and a text editor. His purpose
    is to help you going along that problem. All you need is to install the app, and the rest will be done
    just as magic

System Requirements
    OS: linux operating system
    distribution: debian
    RAM: atleast 2Gb
    storage: atleast 300Mb
    CPU: 2GHz

Installation instructions
    - Take a copy of the .deb file vortext_1.0-1_amd64.deb
    - Open the terminal and do the following
        + Update your system
            sudo apt update
        + Install tesseract-ocr
            sudo apt install tesseract-ocr
        + Install python3
            sudo apt install python3
        + Then install the deb package
            sudo dpkg -i vortext_1.0-1_amd64.deb

Getting Started
    - Depending on your system, move to where the install apps are found and search for vortext, then 
      double click to open.(img_1)
    - Click on the open(3) button at the bottom left to open a video 
    - Put pause/play using the pause/play(4) button below or press "space" 
    - Move forward or backward in the video by clicking and draging the small circle in the time
      slider(1)
    - Increase or decrease the volume using the volume slider(7) at the bottom right 
    - In order to hide the bottom bar, click on the small circle with arrow down(2) at the bottom right 
      or press "T" 
    - You can also move to fullscreen mode using the key "F"

Text extraction feature
    The main goal of vortext is to extract text from the video. In order to do so, consider the following 
    steps
    
    - Put pause on the video and click on the select(5) button at the bottom left corner of the media player
    - Then after the cursor changes, select the required portion of the video to be extracted by clicking
      and draging (img_2)
    - Now click on the copy(4) button (inbetween the open and select buttons) and wait for the vortext text 
      editor to pop-up

    Now you are good to go... :)

    You can now do the following with your text editor (img_3)
    - Copy a text and paste using the copy(1) and cut(4) icons respectively at the top bar of the text editor 
      or by using CTRL_C and CTRL_V resp
    - Undo or redo using the undo(2) and redo(3) icons at the top bar of the text editor respectively or by 
      using CTRL_Z and CTRL_SHIFT_Z respectively.
    - Save the text by clicking on the save button(5) at the top right corner of the bar

Troubleshouting
    - The video plays but you can't extract any text: 
        Ensure that you have the read, write and execute permisions in the /tmp directory(img_4)
        If not, contact your administrator

    - The video media player doesn't open:
        Open the terminal and move to the directory "/usr/share/vortext/". Then execute the executable file
        vortext by typing "./vortext".
        Copy the error that appears and send it to one of the mainteners of vortext via the emails at the end
        of the document. A quick reply will be provided in order to fix it

FAQs
    - How do i open another video? must i reopen the window?
        Just click on the open button and it will automatically end the currently playing video in order to
        open another


Emails: 
    - Cheychou Mouafo Junior: cheychoumouafo@gmail.com
    - Sibafo Wisdom: wisdomsibafo45@gmail.com
    - Pollah Yves: 
    - Nikoum Modeste Lorene: 

