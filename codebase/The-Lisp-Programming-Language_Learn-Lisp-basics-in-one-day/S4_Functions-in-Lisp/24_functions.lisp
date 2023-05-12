; (defun sum(a b)
; (format t "sum is: ~d~%" (+ a b)))

(defun sum (a b)
  (let ((sum (+ a b)))
    (format t "~d = ~d + ~d~%" sum a b)))



(sum 2 4)