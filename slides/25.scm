;;; Tail Recursion

; Regular recursion
(define (factorial n)
  (if (= n 0)
    1
    (* n (factorial (- n 1)))))

; Tail recursion
(define (factorial n)
  (define (helper n total)
    (if (= 0 n)
      1
      (helper (- n 1) (* total n))))
  (helper n 1)
)

(define (length lst)
  (define (helper lst total)
    (if (null? lst)
      total
      (helper (cdr lst) (+ total 1))))
  (helper lst 0)
)

(define (int-list n so-far)
  (if (= n 0)
    so-far
    (int-list (- n 1) (cons n so-far))))

;;; Streams

; Stream of integers starting at first
(define (ints first)
  (cons-stream first
               (ints (+ first 1))))

; map-stream
(define (map-list fn s)
  (if (null? s)
    nil
    (cons (fn (car s)) (map-list fn (cdr s))))
)

(define (map-stream fn s)
  (if (null? s)
    nil
    (cons-stream (fn (car s)) (map-stream fn (stream-cdr s))))
)

; stream-to-list
(define (stream-to-list s num-elements)
  (if (or (null? s) (= num-elements 0))
    nil
    (cons (car s) (stream-to-list (stream-cdr s) (- num-elements 1))))
)
