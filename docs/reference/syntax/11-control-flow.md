# Control Flow

## 1. Syntax
```ebnf
IfStmt = "if" Expression Block [ "else" ( Block | IfStmt ) ] ;
AssessStmt = "assess" Expression "{" { "case" Pattern "->" Block } "}" ;
RepeatWhileStmt = "repeat" "while" Expression Block ;
```

## 2. Examples
```zoren
if score >= 90 {
    post("Grade A")
} else {
    post("Grade B")
}

repeat while (i <= 10) {
    i = i + 1
}
```

## 3. Implementation Status
`SUPPORTED` (`zoren/src/parser.rs`, `codegen.rs`)
