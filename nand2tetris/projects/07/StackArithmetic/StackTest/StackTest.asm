// push constant 17 
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 17 
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// eq
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUEEQ69
D; JEQ
@SP
A = M
M = 0
@ENDEQ69
0; JMP
(TRUEEQ69)
@SP
A = M
M = -1
(ENDEQ69)
@SP
M = M + 1
// push constant 17 
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 16 
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
// eq
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUEEQ46
D; JEQ
@SP
A = M
M = 0
@ENDEQ46
0; JMP
(TRUEEQ46)
@SP
A = M
M = -1
(ENDEQ46)
@SP
M = M + 1
// push constant 16 
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 17 
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// eq
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUEEQ38
D; JEQ
@SP
A = M
M = 0
@ENDEQ38
0; JMP
(TRUEEQ38)
@SP
A = M
M = -1
(ENDEQ38)
@SP
M = M + 1
// push constant 892 
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 891 
@891
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
@TRUELT35
D; JLT
@SP
A = M
M = 0
@ENDLT35
0; JMP
(TRUELT35)
@SP
A = M
M = -1
(ENDLT35)
@SP
M = M + 1
// push constant 891 
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 892 
@892
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
@TRUELT68
D; JLT
@SP
A = M
M = 0
@ENDLT68
0; JMP
(TRUELT68)
@SP
A = M
M = -1
(ENDLT68)
@SP
M = M + 1
// push constant 891 
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 891 
@891
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
@TRUELT92
D; JLT
@SP
A = M
M = 0
@ENDLT92
0; JMP
(TRUELT92)
@SP
A = M
M = -1
(ENDLT92)
@SP
M = M + 1
// push constant 32767 
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32766 
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// gt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUEGT67
D; JGT
@SP
A = M
M = 0
@ENDGT67
0; JMP
(TRUEGT67)
@SP
A = M
M = -1
(ENDGT67)
@SP
M = M + 1
// push constant 32766 
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32767 
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
// gt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUEGT15
D; JGT
@SP
A = M
M = 0
@ENDGT15
0; JMP
(TRUEGT15)
@SP
A = M
M = -1
(ENDGT15)
@SP
M = M + 1
// push constant 32766 
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32766 
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// gt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUEGT13
D; JGT
@SP
A = M
M = 0
@ENDGT13
0; JMP
(TRUEGT13)
@SP
A = M
M = -1
(ENDGT13)
@SP
M = M + 1
// push constant 57 
@57
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 31 
@31
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 53 
@53
D = A
@SP
A = M
M = D
@SP
M = M + 1
// add
@SP
A = M - 1
D = M
A = A - 1
M = D + M
@SP
M = M - 1
// push constant 112 
@112
D = A
@SP
A = M
M = D
@SP
M = M + 1
// sub
@SP
A = M - 1
D = M
A = A - 1
M = M - D
@SP
M = M - 1
// neg
@SP
A = M - 1
M = -M
// and
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D & M
// push constant 82 
@82
D = A
@SP
A = M
M = D
@SP
M = M + 1
// or
@SP
M = M - 1
A = M
D = M
A = A - 1
M = D | M
// not
@SP
A = M - 1
M = !M
