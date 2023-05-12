(defun printnums (&key a b c d)
(format t "~d ~d ~d ~d ~%" a b c d))

(printnums :a 2 :b 3 :d 4 :c 2)