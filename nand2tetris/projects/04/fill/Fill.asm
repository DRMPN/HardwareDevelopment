// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// ideally find a way to reduce two loops, but I can't T_T

// set screen memory size
@8191
D = A
@size
M = D


(START)
// .........................................
// get input from keyboard
@KBD
D = M
                                        
// if any key is pressed, jump
@PRESSED
D; JNE
// .........................................

// .........................................
// do not feel the screen with black pixels

// jump to screen loop
@CLEAR_SCREEN
0; JMP
// .........................................

// .........................................
// fill the screen with black pixels

(PRESSED)

// jump to screen loop
@FILL_SCREEN
0; JMP
// .........................................


// -----------------------------------
(CLEAR_SCREEN)

@size
D = M

(LOOP_CS)
@START
D; JLT

@SCREEN
A = D + A
M = 0
D = D - 1

@LOOP_CS
0;JMP
// -----------------------------------


// -----------------------------------
(FILL_SCREEN)

@size
D = M

(LOOP_FS)
@START
D; JLT

@SCREEN
A = D + A
M = -1
D = D - 1

@LOOP_FS
0;JMP
// -----------------------------------


// end of the program, shouldn't be reachable
(END)
0;JMP