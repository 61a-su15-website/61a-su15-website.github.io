;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Spirals?
;;;
;;; Description:
;;;    I don't know
;;;    What the heck this is,
;;;    But go bears!. 

(define (draw)
  ; *YOUR CODE HERE*
  (ht)
  (speed 0)
  (bgcolor (rgb 0 0 0))
  (color (rgb 0 0 1))
  (helper_circle 200)
  (color (rgb 0.75 0.5 0.25))
  (seth 90)
  (helper_circle 200)
  (color (rgb 0 0 1))
  (seth 180)
  (helper_circle 200)
  (color (rgb 0.75 0.5 0.25))
  (seth 270)
  (helper_circle 200)
  (exitonclick)
  )

(define (helper_circle r)
	(cond ((> r 5) (circle r)
		(rt 10)
		(helper_circle (* r 0.96))))
	)

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
