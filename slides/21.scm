(define (map fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst))
          (map fn (cdr lst)))))
