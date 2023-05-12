; (write (vector 'a 'g 'f)) ; #(A G F)

; (write #('a 'g 'f)) ; #('A 'G 'F)

(setq v (make-array 5))

(dotimes (i 5)
    (setf (aref v i) (* i i))
)
(write v) ; #(0 1 4 9 16)
