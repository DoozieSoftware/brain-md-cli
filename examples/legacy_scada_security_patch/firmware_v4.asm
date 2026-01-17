; PLC-5000 Firmware v4.1
; Input Handler

HANDLE_MODBUS_WRITE:
  LOAD R1, [RX_BUFFER]    ; Load received data
  LOAD R2, [RX_LENGTH]    ; Load length
  CMP R2, 128             ; Check if length > 128
  JGT BUFFER_OVERFLOW     ; If yes, jump to error (Broken in v4.1)

  ; ... copy logic ...
  RET

BUFFER_OVERFLOW:
  ; TODO: Implement safe reset
  NOP
  RET
