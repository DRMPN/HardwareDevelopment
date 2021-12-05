// initialization
@256
D = A
@SP
M = D
// call Sys.init 0
@1603073661284970992
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@5
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@Sys.init
0; JMP
(1603073661284970992)
// function Class1.set 0
// label Class1.set
(Class1.set)
// push argument 0 
@0
D = A
@ARG
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// pop static 0 
@SP
M = M - 1
A = M
D = M
@StaticsTest.0
M = D
// push argument 1 
@1
D = A
@ARG
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// pop static 1 
@SP
M = M - 1
A = M
D = M
@StaticsTest.1
M = D
// push constant 0 
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// return
@LCL
D = M
@FRAME
M = D
@5
A = D - A
D = M
@RET
M = D
@SP
A = M - 1
D = M
@ARG
A = M
M = D
@ARG
D = M + 1
@SP
M = D
@1
D = A
@FRAME
A = M - D
D = M
@THAT
M = D
@2
D = A
@FRAME
A = M - D
D = M
@THIS
M = D
@3
D = A
@FRAME
A = M - D
D = M
@ARG
M = D
@4
D = A
@FRAME
A = M - D
D = M
@LCL
M = D
@RET
A = M
0; JMP
// function Class1.get 0
// label Class1.get
(Class1.get)
// push static 0 
@StaticsTest.0
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push static 1 
@StaticsTest.1
D = M
@SP
A = M
M = D
@SP
M = M + 1
// sub
@SP
M = M - 1
A = M
D = M
A = A - 1
M = M - D
// return
@LCL
D = M
@FRAME
M = D
@5
A = D - A
D = M
@RET
M = D
@SP
A = M - 1
D = M
@ARG
A = M
M = D
@ARG
D = M + 1
@SP
M = D
@1
D = A
@FRAME
A = M - D
D = M
@THAT
M = D
@2
D = A
@FRAME
A = M - D
D = M
@THIS
M = D
@3
D = A
@FRAME
A = M - D
D = M
@ARG
M = D
@4
D = A
@FRAME
A = M - D
D = M
@LCL
M = D
@RET
A = M
0; JMP
// function Class2.set 0
// label Class2.set
(Class2.set)
// push argument 0 
@0
D = A
@ARG
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// pop static 0 
@SP
M = M - 1
A = M
D = M
@StaticsTest.0
M = D
// push argument 1 
@1
D = A
@ARG
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// pop static 1 
@SP
M = M - 1
A = M
D = M
@StaticsTest.1
M = D
// push constant 0 
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// return
@LCL
D = M
@FRAME
M = D
@5
A = D - A
D = M
@RET
M = D
@SP
A = M - 1
D = M
@ARG
A = M
M = D
@ARG
D = M + 1
@SP
M = D
@1
D = A
@FRAME
A = M - D
D = M
@THAT
M = D
@2
D = A
@FRAME
A = M - D
D = M
@THIS
M = D
@3
D = A
@FRAME
A = M - D
D = M
@ARG
M = D
@4
D = A
@FRAME
A = M - D
D = M
@LCL
M = D
@RET
A = M
0; JMP
// function Class2.get 0
// label Class2.get
(Class2.get)
// push static 0 
@StaticsTest.0
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push static 1 
@StaticsTest.1
D = M
@SP
A = M
M = D
@SP
M = M + 1
// sub
@SP
M = M - 1
A = M
D = M
A = A - 1
M = M - D
// return
@LCL
D = M
@FRAME
M = D
@5
A = D - A
D = M
@RET
M = D
@SP
A = M - 1
D = M
@ARG
A = M
M = D
@ARG
D = M + 1
@SP
M = D
@1
D = A
@FRAME
A = M - D
D = M
@THAT
M = D
@2
D = A
@FRAME
A = M - D
D = M
@THIS
M = D
@3
D = A
@FRAME
A = M - D
D = M
@ARG
M = D
@4
D = A
@FRAME
A = M - D
D = M
@LCL
M = D
@RET
A = M
0; JMP
// function Sys.init 0
// label Sys.init
(Sys.init)
// push constant 6 
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 8 
@8
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Class1.set 2
@1603851565761622512
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D = A
@5
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@Class1.set
0; JMP
(1603851565761622512)
// pop temp 0 
@SP
M = M - 1
A = M
D = M
@5
M = D
// push constant 23 
@23
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 15 
@15
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Class2.set 2
@1603958768145330672
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D = A
@5
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@Class2.set
0; JMP
(1603958768145330672)
// pop temp 0 
@SP
M = M - 1
A = M
D = M
@5
M = D
// call Class1.get 0
@1604023639331369456
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@5
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@Class1.get
0; JMP
(1604023639331369456)
// call Class2.get 0
@1604067070040666608
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@5
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@Class2.get
0; JMP
(1604067070040666608)
// label WHILE
(WHILE)
// goto WHILE
@WHILE
0; JMP
