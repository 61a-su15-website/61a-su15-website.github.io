;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <At the End of a Rainbow>
;;;
;;; Description:
;;;   <Rain dries blissfully,
;;;    leaving bright diamonds of color
;;;    and a tunnel of hope.>

(define rad 100)
(define deg 360)
(define init -300)
(define (subtract-by y) 
	(- y 10))

(define (decrease-degrees x)
	(- x 10))

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))

(define (caddr s)
  (car(cdr(cdr s))))


(define (recurse-cir radius degrees colors x y)
	(if (null? colors) break)
	(pos x y)
	(setheading 180)
	(begin_fill)
	(color (car colors))
	(circle radius)
	(setheading 180)
	(end_fill)
	(recurse-cir (subtract-by radius) degrees (cdr colors) (+ x 10) (+ y 10)))



(define (square x y unit col)
  (if (> x 300) (road 300 300))
  (if (> y 300) (square (+ x 100) -350 unit rainbow))
  (if (null? col) (square x y unit rainbow))
  	(pos x y)
  	(begin_fill)
  	(color (car col))
  	(forward unit)
  	(right 90)
  	(forward unit)
  	(right 90)
  	(forward unit)
  	(end_fill)
    (square x (+ y 30) unit (cdr col)))


(define (pos x y)
	(penup)
	(setposition x y)
	(pendown))

(define (road x y)
	(color "#48D1CC")
	(pos x y)
	(begin_fill)
	(circle y)
	(end_fill)
	(begin_fill)
	(color "#7171C6")
	(pos (- x 100) y)
	(circle (- y 100))
	(end_fill)
	(recurse-cir 175 deg multi-col (- x 475) y))


(define sq-col '("#8B4513" "#FF9912" "brown"))
(define rainbow '("red" "orange" "yellow" "green" "blue" "purple" "black"))

(define multi-col '("red" "#fff0cb" "#FF00FF" "#9A32CD" "#0000FF" "#CAE1FF" 
	"#00C78C" "#00EE76" "#2E8B57" "yellow" "orange" "#ffa7b6" "#db9539" "#8B2323"));"#BDB76B" "orange" "#8B2323" "#7D9EC0" "#8E8E38"))

(define (draw)
  (square init -350 60 rainbow)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
