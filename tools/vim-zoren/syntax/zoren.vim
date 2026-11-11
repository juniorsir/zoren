" Vim syntax file for Zoren Programming Language
" Language:    Zoren (.zor, .zoren)
" Maintainer:  Zoren Language Authors
" Last Change: 2026

if exists("b:current_syntax")
  finish
endif

syn keyword zorenControl if else match when assess case repeat while for in break continue escape skip deliver ret divert diverges catch maybe err ensure
syn keyword zorenDecl    flow model ability grant bind flex pack expose use bring as enum actor chamber extern ABI comptime compute_kernel accel
syn keyword zorenAsync   async await
syn keyword zorenAi      ai simd

syn keyword zorenType    Int UInt Float Bool Char Text Nothing int flt str bool byte rune void
syn keyword zorenType    i8 i16 i32 i64 u8 u16 u32 u64 f32 f64 iptr uptr vec map dyn Result Option Tensor Embedding Graph Table Stream

syn keyword zorenBoolean true false
syn keyword zorenNull    null
syn keyword zorenSelf    self
syn keyword zorenMath    PI TAU E

syn keyword zorenBuiltin post print println len sqrt min max pow abs square clamp hypot sin_deg cos_deg assert panic exit typeof push pop insert remove keys values contains sum avg clone copy

syn match   zorenDecorator "@[a-zA-Z_][a-zA-Z0-9_]*"

syn match   zorenNumber    "\<0x[0-9a-fA-F][0-9a-fA-F_]*\>"
syn match   zorenNumber    "\<0b[01][01_]*\>"
syn match   zorenNumber    "\<0o[0-7][0-7_]*\>"
syn match   zorenFloat     "\<[0-9][0-9_]*\.[0-9][0-9_]*\([eE][+-]\=[0-9]\+\)\=\>"
syn match   zorenNumber    "\<[0-9][0-9_]*\>"

syn match   zorenOperator  "\(==\|!=\|<=\|>=\|<\|>\|&&\|||\|!\|+\|-\|\*\|/\|%\|=\|+=\|-=\|\*=\|/=\|%=\|->\||>\|=>\|::\|\.\.\|\?\?\|\?\)"

syn match   zorenComment   "//.*$" contains=zorenTodo
syn match   zorenComment   "#.*$" contains=zorenTodo
syn region  zorenComment   start="/\*" end="\*/" contains=zorenTodo,zorenDocTag
syn keyword zorenTodo      contained TODO FIXME NOTE BUG HACK
syn match   zorenDocTag    contained "@\(param\|return\|returns\|brief\|note\|warning\|throws\)\>"

syn region  zorenString    start=+"+ skip=+\\\\\|\\"+ end=+"+ contains=zorenEscape,zorenInterpolation
syn region  zorenString    start=+'+ skip=+\\\\\|\\'+ end=+'+ contains=zorenEscape
syn match   zorenEscape    contained "\\\([nrt\\'"0]\|x[0-9a-fA-F]\{2}\|u[0-9a-fA-F]\{4}\)"
syn region  zorenInterpolation contained start=+\${+ end=+}+ contains=TOP

syn match   zorenFuncDef   "\<flow\s\+\zs[a-zA-Z_][a-zA-Z0-9_]*\ze\s*("

hi def link zorenControl       Conditional
hi def link zorenDecl          Keyword
hi def link zorenAsync         Keyword
hi def link zorenAi            Special
hi def link zorenType          Type
hi def link zorenBoolean       Boolean
hi def link zorenNull          Constant
hi def link zorenSelf          Identifier
hi def link zorenMath          Constant
hi def link zorenBuiltin       Function
hi def link zorenDecorator     PreProc
hi def link zorenNumber        Number
hi def link zorenFloat         Float
hi def link zorenOperator      Operator
hi def link zorenComment       Comment
hi def link zorenTodo          Todo
hi def link zorenDocTag        SpecialComment
hi def link zorenString        String
hi def link zorenEscape        SpecialChar
hi def link zorenInterpolation Delimiter
hi def link zorenFuncDef       Function

let b:current_syntax = "zoren"
