// initialization
@256
D = A
@SP
M = D
// call Sys.init 0
@2059809691951338535
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
(2059809691951338535)
// function Sys.init 0
// label Sys.init
(Sys.init)
// push constant 4000 
@4000
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 0 
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5000 
@5000
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 1 
@SP
M = M - 1
A = M
D = M
@THAT
M = D
// call Sys.main 0
@2060250046358262823
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
@Sys.main
0; JMP
(2060250046358262823)
// pop temp 1 
@SP
M = M - 1
A = M
D = M
@6
M = D
// label LOOP
(LOOP)
// goto LOOP
@LOOP
0; JMP
// function Sys.main 5
// label Sys.main
(Sys.main)
// push constant 0 
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 0 
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 0 
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 0 
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 0 
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 4001 
@4001
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 0 
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5001 
@5001
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 1 
@SP
M = M - 1
A = M
D = M
@THAT
M = D
// push constant 200 
@200
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 1 
@1
D = A
@LCL
D = D + M
@R13
M = D
@SP
M = M - 1
A = M
D = M
@R13
A = M
M = D
// push constant 40 
@40
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 2 
@2
D = A
@LCL
D = D + M
@R13
M = D
@SP
M = M - 1
A = M
D = M
@R13
A = M
M = D
// push constant 6 
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 3 
@3
D = A
@LCL
D = D + M
@R13
M = D
@SP
M = M - 1
A = M
D = M
@R13
A = M
M = D
// push constant 123 
@123
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Sys.add12 1
@2060598591544267815
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
@1
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
@Sys.add12
0; JMP
(2060598591544267815)
// pop temp 0 
@SP
M = M - 1
A = M
D = M
@5
M = D
// push local 0 
@0
D = A
@LCL
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push local 1 
@1
D = A
@LCL
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push local 2 
@2
D = A
@LCL
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push local 3 
@3
D = A
@LCL
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push local 4 
@4
D = A
@LCL
A = M + D
D = M
@SP
A = M
M = D
@SP
M = M + 1
// add
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D + M
// add
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D + M
// add
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D + M
// add
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D + M
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
// function Sys.add12 0
// label Sys.add12
(Sys.add12)
// push constant 4002 
@4002
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 0 
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5002 
@5002
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 1 
@SP
M = M - 1
A = M
D = M
@THAT
M = D
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
// push constant 12 
@12
D = A
@SP
A = M
M = D
@SP
M = M + 1
// add
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D + M
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
