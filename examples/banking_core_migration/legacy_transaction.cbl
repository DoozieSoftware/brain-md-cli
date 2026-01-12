       IDENTIFICATION DIVISION.
       PROGRAM-ID. TRANSACT.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-BALANCE       PIC 9(09)V99.
       01  WS-AMOUNT        PIC 9(09)V99.
       01  WS-ACCOUNT-TYPE  PIC X(01).
       PROCEDURE DIVISION.
           IF WS-ACCOUNT-TYPE = 'S'
               IF WS-BALANCE - WS-AMOUNT < 0
                   DISPLAY 'INSUFFICIENT FUNDS'
               ELSE
                   COMPUTE WS-BALANCE = WS-BALANCE - WS-AMOUNT
               END-IF
           ELSE
               COMPUTE WS-BALANCE = WS-BALANCE - WS-AMOUNT
           END-IF.
