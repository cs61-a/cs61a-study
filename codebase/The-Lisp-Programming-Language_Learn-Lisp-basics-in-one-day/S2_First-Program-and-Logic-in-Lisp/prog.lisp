(write 2343)
(write-line "hello World")

(defvar x 110)
(format t "x = ~d~%" x)
(setq y 130)
(format t "y = ~d~%" y)


(let ((x `(12))) (y 23))
(format t "x = ~a, y = ~d" x, y)