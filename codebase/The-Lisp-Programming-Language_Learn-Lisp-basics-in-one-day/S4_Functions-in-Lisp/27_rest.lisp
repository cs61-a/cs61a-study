(defun printnums (a b &rest c)
(format t "~d ~d~% ~%" a b)
(loop for x in c
    do(format t "~d~%" x)))

(printnums 2 3 4 2 5 6 7 42)