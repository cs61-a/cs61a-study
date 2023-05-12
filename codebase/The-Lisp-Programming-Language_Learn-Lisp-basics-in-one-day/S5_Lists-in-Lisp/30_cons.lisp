; (write (cons 'a 'b))
; (write (cons 'a (cons 'a nil)))
(write (cdr (cons 'a (cons 'a (cons 'a nil)))))