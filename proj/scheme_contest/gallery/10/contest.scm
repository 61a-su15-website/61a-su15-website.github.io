;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Broccoli>
;;;
;;; Description:
;;;   <Broccoli's ready, hold  
;;;   steady, on pizza, heavy,
;;;   like mom's spaghetti.
;;;




(define (slice)
	(penup)
	(goto -300 200)
	(pendown)
	(color "white")
	(goto 200 100)
	(rt 60)
	(repeat 25 (lambda () (rt 5) (fd 20)))
	(goto -300 200)
	(rt 180))


(define (repeat n f)
  (if (> n 1)
      (begin (f)(repeat (- n 1) f))
      (f)))



(define (tomato count m d)
	(pendown)
	(color "red")
  	(cond ((= count 0) 0)
        (else (fd m)
              (rt d)
              (tomato (- count 1) (+ m 1) d))))	



(define (broccoli level size)
	(speed 0)
	(pendown)
	(color "green")
	(cond  
		((= level 1) (fd size) (fd (- 0 size)) )
	(else
		(fd size) (rt -35) (broccoli (- level 1) (* 0.8 size)) (rt 70) (broccoli (- level 1) (* 0.7 size)) (rt -35) (fd (- 0 size)))))



(define (draw)
(rt 80)
(bgcolor "yellow")

(repeat 4 slice)

(penup)
(goto -10 -70)
(tomato 60 1 50)

(penup)
(goto 90 60)
(tomato 45 1 60)

(penup)
(goto -150 100)
(tomato 55 1 85)




(penup)
(rt 80)
(goto -150 100)

(broccoli 9 30)

(penup)
(goto 60 20)
(broccoli 10 40)

(penup)
(goto -90 -5)
(broccoli 7 33)

(penup)
(goto -50 -80)
(broccoli 8 35)


(exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
