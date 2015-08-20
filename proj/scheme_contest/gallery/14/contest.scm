;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Hopefully win by default>
;;;
;;; Description:
;;;   <Hey look its a star.
;;;    Looks somewhat interesting...
;;;    Eh, why not. *submit>


(define (draw)

(define (drawer x y z)
	(forward x)
	(right y)
	(forward z)
	(drawer z (/ 100 y) x))

(drawer 200 160 90)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
