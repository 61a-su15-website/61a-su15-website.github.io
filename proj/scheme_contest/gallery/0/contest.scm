;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: A Pair of Snowflakes
;;;
;;; Description:
;;;   <Snowflakes twist and twirl
;;;    fuse to form a perfect whole
;;;    and strike a balance.>

;;;;;;;;;;;;;;;;
;Koch Snowflake;
;;;;;;;;;;;;;;;;

;draws one side of a koch snowflake
(define (snow-side len n)
  (if (<= n 0)
    (fd len)
    (let ((s (/ len 3)))
      (snow-side s (- n 1))
      (lt 60)
      (snow-side s (- n 1))
      (rt 120)
      (snow-side s (- n 1))
      (lt 60)
      (snow-side s (- n 1))
      )
    )
  )
  
;Forms a koch snowflake with your turtle at the center. Aligns bottom side with your orientation
(define (color-snowflake sideLen layers cVal)
  (begin_fill)
  (pu)
  (rt 150)
  (fd (/ sideLen (sqrt 3)))
  (rt 150)
  (pd)
  (snow-side sideLen layers)
  (rt 120)
  (snow-side sideLen layers)
  (rt 120)
  (snow-side sideLen layers)
  (rt 150)
  (pu)
  (fd (quotient sideLen (sqrt 3)))
  (rt 30)
  (pd)
  (end_fill)
  )
  
;multiple layer snowflake with white in center
(define (white-multi size layers cVal)
  (if (>= layers 0)
    (begin
      (color (rgb (- 1 cVal) (- 1 cVal) (- 1 cVal)))
      (color-snowflake size (quotient layers 2) cVal)
      (white-multi (/ size 1.43) (- layers 1) (/ cVal 1.75))
      )
    )
  )
  
;multiple layer snowflake with black in center
(define (black-multi size layers cVal)
  (if (>= layers 0)
    (begin
      (color (rgb cVal cVal cVal))
      (color-snowflake size (quotient layers 2) cVal)
      (black-multi (/ size 1.43) (- layers 1) (/ cVal 1.75))
      )
    )
  )

;;;;;;;;;;;;;;;;;;;;;
;Background Gradient;
;;;;;;;;;;;;;;;;;;;;;
  
;create smooth color gradient from point 1 to point 2, in a rectangle
(define (pattern x1 y1 x2 y2 r1 g1 b1 r2 g2 b2)
  (pu)
  (let ((mR (/ (- (/ r2 255) (/ r1 255)) (dist x1 y1 x2 y2))) (mG (/ (- (/ g2 255) (/ g1 255)) (dist x1 y1 x2 y2))) (mB (/ (- (/ b2 255) (/ b1 255)) (dist x1 y1 x2 y2))))
    (fill-grid x1 y1 x2 y2 (/ r1 255) (/ g1 255) (/ b1 255) mR mG mB)
    )
  (pd)
  )

;fill in the rectangle row by row
(define (fill-grid xS yS x y r g b mR mG mB)
  (goto x y)
  (setheading 180)
  (pd)
  (fill-row xS yS x y r g b mR mG mB)
  (pu)
  (if (not (= yS y))
    (fill-grid xS yS x (- y 1) r g b mR mG mB)
    )
  )
  
;fill in a row
(define (fill-row xS yS x y r g b mR mG mB)
  (let ((nR (+ r (* mR (dist xS yS x y)))) (nG (+ g (* mG (dist xS yS x y)))) (nB (+ b (* mB (dist xS yS x y)))))
    (color (rgb nR nG nB))
    (fd 1)
    )
  (if (not (= xS x))
    (fill-row xS yS (- x 1) y r g b mR mG mB)
    )
  )

;;;;;;;;;;;;;;;;;
;Yin-Yang Symbol;
;;;;;;;;;;;;;;;;;
 
;creates half the yin/yang symbol of a particular color, starting from the bottom point
(define (tear r color)
  (fillcolor color)
  (begin_fill)
  (circle r 180)
  (circle (/ r 2) 180)
  (circle (- (/ r 2)) 180)
  (end_fill)
  )

;creates the yin-yang symbol
(define (yin-yang r)
  (pu)
  (rt 90)
  (fd r)
  (lt 90)
  (tear r 'black)
  (rt 90)
  (fd (* r 2))
  (lt 90)
  (tear r 'white)
  (rt 90)
  (fd (/ r 2))
  (lt 90)
  (pu)
  (black-multi (/ r 1.6) 12 1)
  (rt 90)
  (pu)
  (fd r)
  (lt 90)
  (white-multi (/ r 1.6) 12 1)
  (pu)
  (lt 90)
  (fd (/ r 2))
  (rt 90)
  )

(define (draw)
  (dis-ani)
  (pattern -400 -400 400 400 0 0 0 188 56 56)
  (pu)
  (goto 0 0)
  (yin-yang 300)
  (ud)
  (exitonclick)
  )

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
