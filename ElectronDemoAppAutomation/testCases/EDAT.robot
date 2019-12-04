*** Settings ***
Library     ../lib/ElectronDemoAppLibrary.py

*** Test Cases ***
View demo for window creation
    Launch app  Electron API Demos
    Click on    Create and manage windows
    Click on    Create a new window
    Click on    View Demo
    New window should open with text    Hello World!
    Click on    Close this Window
    Close the application

View demo for frame less window creation
    Launch app  Electron API Demos app
    Click on    Create and manage windows
    Click on    Create a frameless window
    Click on    View Demo
    New window should open with text    Hello World!
    Click on    Close this Window
    Close the application
