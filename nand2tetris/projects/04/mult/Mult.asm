// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// preusocode
// R2 = 0
//
// LOOP
//    while R1 != 0
//          R2 = R0 + R2
//          R1 = R1 - 1
// END


// initialize R2 to 0
@R2
M=0

(LOOP)
// get R1 value
@R1
D=M

// if D == 0 then jump to @END else do math
@END
D;JEQ

// do math
@R0
D=M
@R2
M=D+M
@R1
M=M-1

// go again
@LOOP
0;JMP


// infinite loop
(END)
@END
0;JMP