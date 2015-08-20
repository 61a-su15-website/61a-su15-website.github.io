;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Waking with the Stars
;;;
;;; Description:
;;;    When the sun comes up
;;;    Even those sitting in space
;;;    Can see its bright light

(define (draw)
  (define (earth length ratio depth color)
  	(if (> depth 0)
  		(
  		(pencolor (hsv_rgb (/ color 1000) 1.0 1.0))
  		(circle length)
  		(right (tan 60))
  		(if (= color 1000) (define color (- 0 10)))
  		(if (> length 2000) (define ratio (/ 1 ratio)))
  		(earth (* length ratio) ratio (- depth 1) (+ color 10))
  		)
  		(stars 9)
  	)
  )

  (define (stars amount)
    ;Note: The stars are created randomly above the earth, so each generated picture will be different
  	(if (> amount 0)
  		(
  		(fill 'white)
  		(begin_fill)
  		(circle (* (random) 2.5))
  		(end_fill)
  		(pencolor 'black)
  		(if (= (modulo amount 2) 0)
  			(setpos (* (random) 500) (+ (* (random) 400) 100))
  			(setpos (* (random) (- 0 500)) (+ (* (random) 400) 100))
  		)
  		(pencolor 'white)
  		(stars (- amount 1))
  		)
  	)
  )
  
  (bgcolor 'black)
  (hideturtle)
  (speed 0)
  (right 270)
  (earth 10 1.1 125 0)

  (exitonclick)
)

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
