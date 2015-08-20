;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: How to tell Fall is coming
;;;
;;; Description:
;;;    Is it Fall, Peets?
;;;    Never ends, Here it comes
;;;    Pumkin, parades


(define (draw)
  (define (pumkin x y deg count size)
    (penup) (forward x) (left 90) (forward y) (right 90) (left 90) (forward (* size 10)) (right deg) (pendown)
    (cond
      ((= count 0) (penup))
      (else
        ;(penup) (color “99CC00”) (pendown)
        (right 140)
        (forward (* size 10))
        ;(penup) (color “FF6600”) (pendown)
        (right 130)
        (circle (* size 20))
        (right 130)
        ; wish color would work
        ;(penup) (color “99CC00”) (pendown)
        (forward (* size 10))
        (left 130)
        (forward (* size 13))
        (pumkin (- x 50) (- y 50) (* deg 0.7) (- count 1) (* size 0.9))
      )
    )
  )
  (pumkin 320 280 60 200 7)
  (exitonclick))


; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
