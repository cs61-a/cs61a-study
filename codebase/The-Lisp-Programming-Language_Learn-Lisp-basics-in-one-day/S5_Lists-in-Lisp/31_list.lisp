; (write (list 'a 'b 'b)) ; (A B B)

; (write (list 'a 'b (list 'a 'b 'b))) ; (A B (A B B))

; The cdr function is applied to the list, which means that 
;it returns the "rest" of the list starting from the second element.
; (write (cdr (list 'a 'b (list 'a 'b 'b)))) ; (B (A B B))

; The cadr function is a shorthand for (car (cdr ...)). 
; (write (cadr (list 'a 'b (list 'a 'b 'b)))) ; B

; The caddr function is a shorthand for (car (cdr (cdr ...))).
(write (caddr (list 'a 'b (list 'a 'b 'b)))) ; (A B B)

