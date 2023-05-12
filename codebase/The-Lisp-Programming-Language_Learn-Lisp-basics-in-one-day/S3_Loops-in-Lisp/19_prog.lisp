(do ((x 0 (+ 1 x)) (y 1 (* 2 y)))
((= x 10) 1)
(format t "2^~d = ~d ~%" x y))