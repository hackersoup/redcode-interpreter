# TODO


### General

- Memory map
- Instruction pointers
- Instruction classes
- Opcode interpreter operating on AST

### Parsing
- Addressing modes
  - Immediate (#)
  - Direct ($ or empty)
  - Indirect (@)
  - Indirect increment (>)
  - Indirect decrement (<)
  - A-field indirect (\*)
  - A-field indirect increment (})
  - A-field indirect decrement ({)

- Opcodes
  - DAT
    - Check the parser, not quite spec yet
  - MUL
  - DIV
  - MOD
  - JMN
  - DJN
  - SPL
    - Blocked by multi-threading feature
  - SEQ
  - SNE
  - SLT
  - XCH
  - PCT
  - NOP
  - STP
    - Blocked until P-Space is implemented
  - LDP
    - Blocked until P-Space is implemented

- Modifiers
  - .A  (A -> A)
  - .B  (B -> B)
  - .AB (A -> B)
  - .BA (B -> A)
  - .F  (A-\>A and B-\>B)
  - .X  (A-\>B and B-\>A)
  - .I  (Entire instruction)

