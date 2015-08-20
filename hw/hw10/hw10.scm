(define (filter pred lst)
  'YOUR-CODE-HERE
)


(define (scale-stream s k)
  'YOUR-CODE-HERE
)


(define (merge s0 s1)
  (cond ((null? s0) s1)
        ((null? s1) s0)
        ; YOUR CODE HERE
  ))


(define (make-s)
  (cons-stream 1
      'YOUR-CODE-HERE
  ))


;;; Utilities

(define (int-list n total)
    (if (= n 0)
        total
        (int-list (- n 1) (cons n total))))

(define (equal? s0 s1)
  (cond ((and (null? s0) (null? s1)) True)
        ((or (null? s0) (null? s1)) False)
        (else (and (= (car s0) (car s1))
                   (equal? (cdr s0) (cdr s1))))))


(define (integers first)
  (cons-stream first (integers (+ first 1))))

(define (stream-to-list s num-elements)
  (if (or (null? s) (= num-elements 0))
    nil
    (cons (car s) (stream-to-list (stream-cdr s) (- num-elements 1)))))

