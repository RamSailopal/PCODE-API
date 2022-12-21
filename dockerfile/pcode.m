START
 S FIL="/home/pcode/ukpostcodes1.csv"
 O FIL:(read)
 U FIL F  Q:$ZEOF=1  D
 . R LIN
 . S PCODE=$P(LIN,",",2)
 . Q:PCODE="id"!(PCODE="")
 . S LAT=$P(LIN,",",3)
 . S LAT=$TR(LAT," ","")
 . S LONG=$P(LIN,",",4)
 . S LONG=$TR(LIN," ","")
 . S ^PCODE(PCODE)=LAT_","_LONG
 C FIL
 QUIT
