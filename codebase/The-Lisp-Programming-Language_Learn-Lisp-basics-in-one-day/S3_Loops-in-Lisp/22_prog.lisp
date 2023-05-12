(setq x 0)
(loop
    (setq x (+ x 1))
    (format t "x=~d~%" x)
    (if (= x 10) (return x))
)