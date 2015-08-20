;; Tail Recursion ;;

; Q2
(define (last s)
  'YOUR-CODE-HERE
)


; Q3
(define (reverse lst)
  'YOUR-CODE-HERE
)


; Q5
(define (interleave-map s1 s2)
  'YOUR-CODE-HERE
)


; Q6
(define (stream-filter s pred)
    'YOUR-CODE-HERE
)


; Q7
(define fibs (make-fib-stream 0 1))
(define (make-fib-stream a b)
  'YOUR-CODE-HERE
)


(define (stream-to-list s num-elements)
  (if (or (null? s) (= num-elements 0))
    nil
    (cons (car s)
          (stream-to-list (stream-cdr s)
                          (- num-elements 1)))))
