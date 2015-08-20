;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Scheme, Lord of Lispland
;;;
;;; Description:
;;;   Banished from my own homeland (MIT)
;;;   And now you dare enter my realm
;;;   You are not prepared

(define (draw)
	(bgcolor "black")
	(speed 0)
	(penup)
	(fd 100)
	(pendown)
	(define (truehelper r)
  		(define (helper r)
  			(if (= 0 (modulo r 1)) (color "red"))
  			(if (= 0 (modulo r 2)) (color "blue"))
  			(if (= 0 (modulo r 3)) (color "green"))
  			(if (= 0 (modulo r 5)) (color "yellow"))
  			(if (= r 0) (penup)
  			(
  			(rt 90)
  			(fd 30) 
  			(rt 90) 
  			(fd 30) 
  			(rt 90) 
			(fd 30) 
			(rt 160)
			(helper (- r 1)))))
  	(if (= r 0) (penup)
  	((helper 35)
  	(rt 180)
  	(fd 180)
  	(pendown)
  	(truehelper (- r 1)))))
  (truehelper 13)
  (rt 180)
  (fd 200)
  (pendown)
  (color "green")
  (define (stemhelper r)
  	(if (= r 0) (penup)
	  (
	  (fd 250)
	  (rt 270)
	  (fd (- r 2))
	  (rt 270)
	  (fd 250)
	  (rt 270)
	  (fd (- r 4))
	  (rt 270)
	  (stemhelper (- r 1)))))
  (stemhelper 50)
  (exitonclick)
  )

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
