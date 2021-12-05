// initialization
@256
D = A
@SP
M = D
// call Sys.init 0
@834922402527483626
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
(834922402527483626)
// function Main.fibonacci 0
// label Main.fibonacci
(Main.fibonacci)
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
// push constant 2 
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1
// lt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUELT835281942829766378
D; JLT
@SP
A = M
M = 0
@ENDLT835281942829766378
0; JMP
(TRUELT835281942829766378)
@SP
A = M
M = -1
(ENDLT835281942829766378)
@SP
M = M + 1
// goto IF_TRUE
@SP
M = M - 1
A = M
D = M
@IF_TRUE
D; JNE
// goto IF_FALSE
@IF_FALSE
0; JMP
// label IF_TRUE
(IF_TRUE)
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
// label IF_FALSE
(IF_FALSE)
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
// push constant 2 
@2
D = A
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
// call Main.fibonacci 1
@835464461759977194
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
@Main.fibonacci
0; JMP
(835464461759977194)
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
// push constant 1 
@1
D = A
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
// call Main.fibonacci 1
@835556820736710378
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
@Main.fibonacci
0; JMP
(835556820736710378)
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
// function Sys.init 0
// label Sys.init
(Sys.init)
// push constant 4 
@4
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Main.fibonacci 1
@835668970922743530
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
@Main.fibonacci
0; JMP
(835668970922743530)
// label WHILE
(WHILE)
// goto WHILE
@WHILE
0; JMP
