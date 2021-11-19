// function SimpleFunction.test 2
// label SimpleFunction.test
(SimpleFunction.test)
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
// add
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D + M
// not
@SP
A = M - 1
M = !M
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
// add
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D + M
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
// sub
@SP
M = M - 1
A = M
D = M
A = A - 1
M = M - D
// return
@SP
M = M - 1
A = M
D = M
@ARG
A = M
M = D
@ARG
D = M + 1
@SP
M = D
@LCL
D = M
@R13
M = D
@R13
A = M - 1
D = M
@THAT
M = D
@2
D = A
@R13
A = M - D
D = M
@THIS
M = D
@3
D = A
@R13
A = M - D
D = M
@ARG
M = D
@4
D = A
@R13
A = M - D
D = M
@LCL
M = D
@5
D = A
@R13
A = M - D
0; JMP
