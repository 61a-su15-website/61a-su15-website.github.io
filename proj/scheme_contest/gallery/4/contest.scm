;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Beat Stanford!>
;;;
;;; Description:
;;;   <Chill out, Bears.
;;;    Even without attacks from recursion,
;;;    sequoia is down.>

(define (draw)
  ; *YOUR CODE HERE*
(speed 1000)
(define (repeat n func) ; Repeat func k times.
  (if (> n 1)
      (begin (func) (repeat (- n 1) func))
      (func)))
(define (arcr size)
  (repeat size 
  	   (lambda () (fd 1) (rt 1))))
(define (larcr size)
  (repeat size 
  	   (lambda () (fd 1) (lt 1))))
(define (slarcr size)
  (repeat size 
  	   (lambda () (fd 0.5) (lt 1))))
(define (sarcr size)
  (repeat size 
  	   (lambda () (fd 0.5) (rt 1))))
(define (drawfalltree)
(pu)(fd 100)(pd)(lt 60)(fd 60)(lt 20)(larcr 15)(rt 80)(fd 5)(rt 30)(arcr 10)(rt 80)(fd 10)
(lt 20)(fd 10)(rt 30)(arcr 10)(fd 10)(lt 90)(larcr 10)(fd 5)(lt 90)(fd 10)(larcr 15)(lt 10)(fd 5)(lt 10)(larcr 20)(rt 50)
(fd 10)(rt 130)(fd 10)(larcr 15)(rt 30)(arcr 20)(lt 10)(fd 10)(lt 10)(fd 10)(lt 120)(larcr 10)(lt 50)(fd 10)(rt 30)
(fd 5)(arcr 10)(rt 150)(fd 20)(rt 15)(fd 10)(lt 30)(slarcr 40)(fd 20)(lt 150)(arcr 20)(lt 10)(fd 10)(arcr 10)(rt 150)
(arcr 10)(rt 10)(fd 10)(arcr 15)(lt 30)(fd 10)(lt 40)(fd 10)(rt 170)(fd 10)(arcr 10)(rt 20)(fd 10)(lt 60)(larcr 20)
(rt 20)(fd 20)(rt 160)(arcr 10)(lt 30)(fd 10)(arcr 10)(lt 90)(fd 5)(lt 20)(larcr 10)(lt 50)(fd 20)(rt 10)(arcr 15)(fd 10)
(rt 130)(arcr 20)(lt 10)(fd 10)(lt 130)(larcr 30)(rt 15)(fd 10)(rt 10)(fd 10)(rt 30)(fd 10)(rt 160)(fd 8)(lt 55)(fd 10))
(define (draws)
	(fd 80)(lt 45)(fd 40)(lt 45)(fd 80)(lt 45) (fd 40)(lt 45)(fd 70)(rt 90)(fd 40)
	(rt 90)(fd 40)(rt 90)(fd 20)(lt 90)(fd 50)(lt 90)(fd 40)(lt 45)(fd 40)
	(lt 45)(fd 80)(lt 45)(fd 40)(lt 45)(fd 80)(lt 45)(fd 40)(lt 45)(fd 60)
	(rt 90)(fd 40)(rt 90)(fd 40)(rt 90)(fd 20)(lt 90)(fd 50)(lt 90)(fd 40)
	(lt 45)(fd 40)(lt 45)(fd 10)(lt 90)(fd 3)(rt 90)
	)
(define (drawline)
	(fd 78)(lt 45)(fd 38)(lt 45)(fd 78)(lt 45) (fd 37)(lt 45)(fd 72)(rt 90)(fd 46)
	(rt 90)(fd 46)(rt 90)(fd 20)(lt 90)(fd 44)(lt 90)(fd 35)(lt 45)(fd 37)
	(lt 45)(fd 78)(lt 45)(fd 37)(lt 45)(fd 77)(lt 45)(fd 15)(pu)(fd 7)(pd)(fd 10)(pu)(fd 6)(lt 45)(fd 62)
	(rt 90)(fd 5)(pd)(fd 41)(rt 90)(fd 20)(pu)(fd 13)(pd)(fd 13)(rt 90)(fd 20)(lt 90)(fd 15)(pu)(fd 20)(pd)(fd 10)(lt 90)(fd 36)
	(lt 45)(fd 37)(lt 45)(fd 10))
(define (tree)
	(lt 40)(arcr 15)(lt 35)(arcr 20)(lt 50)(fd 25)(larcr 15)(lt 20)(larcr 20)(lt 70)(larcr 20)
    (rt 50)(larcr 10)(arcr 5)(larcr 10)(rt 140)(arcr 15)(rt 10)(fd 10)(lt 20)(sarcr 40)(lt 90)
    (fd 5)(lt 90)(larcr 25)(rt 170)(fd 10)(arcr 20)(fd 15)(lt 150)(larcr 30)(fd 15)(rt 150)
    (arcr 20)(rt 20)(fd 30)(rt 15)(fd 20)(rt 10)(fd 30)(rt 15)(arcr 15)(rt 60)(fd 4)(rt 80)(arcr 15)(rt 10)(fd 10)
    (lt 140)(larcr 15)(lt 15)(fd 10)(lt 10)(fd 10)(rt 130)(fd 10)(lt 120)(fd 10)(arcr 20)(rt 40)(fd 10)(rt 120)
    (arcr 20)(lt 40)(arcr 30)(lt 90)(larcr 30)(rt 20)(fd 10)(lt 30)(fd 25)(lt 60)(arcr 30)(lt 10)(fd 4)(rt 130)(fd 59))
(color  "#981E32")
(begin_fill)
(draws)
(end_fill)
(color "#FFFFFF")
(begin_fill)
(repeat 6
	(lambda() (tree) (rt 180)))

(color "#067806")
(begin_fill)
(tree)
(end_fill)
(rt 90)
(fd 2)
(rt 90)
(color "#FFFFFF")
(begin_fill)
(repeat 5 drawline)
(color  "#067806")
(begin_fill)
(drawfalltree)
(end_fill)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
