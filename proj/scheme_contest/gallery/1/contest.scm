;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Squares
;;;
;;; Description:
;;;    Simple elegance
;;;    Equality everywhere
;;;    Who doesn't like squares?

(color '"#FF0000")
(bgcolor '"#FFFFFF")

(define (calc_new_side_len old_len)
  (sqrt (+ (expt (* (/ 24 25) old_len) 2) (expt (* (/ 1 25) old_len) 2)))
)

(define (draw_square side_len)
  (fd side_len)
  (rt 90)
  (fd side_len)
  (rt 90)
  (fd side_len)
  (rt 90)
  (fd side_len)
)

(define (draw)
  (define side_len 250)
  (pu)
  (setpos (* (/ side_len 2) -1) (/ side_len 2))
  (pd)
  (rt 90)
  (draw_square side_len)
  (define (draw_helper side_len index)
    (if (< side_len 25)
      nil
      ((define side_len (calc_new_side_len side_len))
      (cond ((= (modulo index 4) 0) (color '"#FF0000"))
            ((and (= (modulo index 3) 0) (= (modulo index 2) 1)) (color '"#006600"))
            ((= (modulo index 2) 0) (color '"#000066"))
            (else (color '"#FF6600")))
      (lt 92.38594403)
      (draw_square side_len)
      (draw_helper side_len (+ index 1)))))
  (draw_helper side_len 1)
  (exitonclick))


; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
