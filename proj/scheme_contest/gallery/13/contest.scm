;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Sunrise or Sundown
;;;
;;; Description:
;;;   <Day by day
;;;    	sun goes around tree
;;;   	only tree can tell sun is down or rise >
(define (draw)
  ; *YOUR CODE HERE
  
  (pixelsize 2)
  (screen_width)
  (speed 10)

  ;begin the sky
  (penup)
  (goto -640 -70)
  (color (rgb (/ 255 255) (/ 121 255) (/ 66 255)))
  (begin_fill)
  (fd 390)(right 90)(fd 1280)(right 90)(fd 390)
  (end_fill)
  ;end the sky

  ;begin the sun
  (penup)
  (goto -550 0)
  (color (rgb (/ 205 255) (/ 38 255) (/ 38 255)))
  (begin_fill)
  (circle 150)
  (end_fill)
  (penup)

  ;end the sun

  ;begin the ground
  (penup)
  (seth 0)
  (goto -640 -320)
  (color (rgb (/ 205 255) (/ 198 255) (/ 115 255)))
  (begin_fill)
  (right 90)(fd 1280)(left 90)(fd 300)(left 90)(fd 1280)
  (end_fill)
  (penup)

  ;end the ground


  ;begin the tree
(define (tree r)
  (if (< r 7) 
  (begin 
    (begin_fill)
      (circle (/ r 3))
    (end_fill))
  (begin 
    (forward (/ r 3))
    (left 30)
    (tree (* (/ r 3) 2))
    (right 30)
    (back (/ r 3))

    (forward (/ r 2))
    (right 25)
    (tree (/ r 2))
    (left 25)
    (back (/ r 2))

    (forward (* (/ 5 6) r))
    (right 25)
    (tree (/ r 2))
    (left 25)
    (back (* r (/ 5 6))))))

(define (tree_inverse r)
  (if (< r 10)
  (begin 
    (begin_fill)
      (circle (/ r 3))
    (end_fill))
  (begin 
    (forward (/ r 3))
    (right 30)
    (tree_inverse (* (/ r 3) 2))
    (left 30)
    (back (/ r 3))

    (forward (/ r 2))
    (left 25)
    (tree_inverse (/ r 2))
    (right 25)
    (back (/ r 2))

    (forward (* (/ 5 6) r))
    (left 25)
    (tree_inverse (/ r 2))
    (right 25)
    (back (* r (/ 5 6))))))

  (penup)
  (setposition -150 -150)
  (setheading 0)
  (pendown)
  (color (rgb (/ 60 255) (/ 90 255) (/ 24 255)))
  (tree 300)
  (penup)
  (setposition -150 -150)
  (setheading 115)
  (pendown)
  (color (rgb 0 0 0))
  (tree_inverse 300)
  (penup)

  ;end the tree

 
  ;begin the grass
  (define (gras r)
  	(define d (* 3 r))
    (circle (- 0 d) 30)
  	(right 180)
  	(circle d 30)
  	(right 150)
  	(circle (- 0 d) 25)
  	(right 180)
  	(circle d 25)
  	(left 100)
  	(circle d 20)
  	(right 180)
  	(circle (- 0 d) 20)
  	(setheading 340)
  )
  (define (grass len1 len2 len3 len4 width)
  	(pendown)
  	(setheading 0)(gras len1)(penup)(right 90)(fd width)(left 90)(forward (/ len1 4))
  	(pendown)(gras len2)(penup)(right 90)(fd width)(left 90)(back (* 3 (/ len2 4)))
  	(pendown)(gras len3)(penup)(right 90)(fd width)(left 90)(forward (* 3 (/ len3 4)))
  	(pendown)(gras len4)(penup)
  )

  (define (grass_line x y len1 len2 len3 len4 width)
  	(goto x y)
  	(grass len1 len2 len3 len4 width)
  	(if (> x 640)
  		(penup)
  		(grass_line (+ x (* 4 width)) y len1 len2 len3 len4 width)
  	)
  )

  (color (rgb (/ 110 255) (/ 139 255) (/ 61 255)))
  (grass_line -640 -300 40 34 30 20 18)
  (grass_line -638 -280 38 43 27 18 18)
  (grass_line -634 -255 37 31 24 9 16)
  (grass_line -643 -240 35 32 38 22 16)
  (grass_line -642 -200 28 24 21 18 12)
  (grass_line -636 -210 30 26 29 14 12)
  (grass_line -645 -170 24 22 26 15 13)
  (grass_line -628 -150 18 24 19 12 14)
  (grass_line -625 -130 20 23 14 11 9)
  (grass_line -643 -85 14 12 13 6 7)
  (grass_line -639 -120 17 15 20 10 11)
  (grass_line -641 -100 16 14 15 10 8)
  (grass_line -639 -70 12 10 11 4 7)
  (grass_line -637 -50 10 5 7 3 6)
  (grass_line -636 -40 7 8 3 5 5)
  (grass_line -640 -30 4 2 4 3 3)


  ;end the grass

  (hideturtle)
  (exitonclick))



; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
