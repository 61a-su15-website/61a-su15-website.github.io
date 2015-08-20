;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: THE SCHEMING TREE
;;;         By Shel Silverscheme
;;;
;;; Description:
;;;   To fathom a tree
;;;   That ceases not to split anew
;;;   Please see this haiku.

(define (rectangle n m)
    ;draws and fills a rectangle of height n and width m
  (begin (color '"brown")
  (pendown)
  (begin_fill)
  (forward n)
  (right 90)
  (forward m)
  (right 90)
  (forward n)
  (right 90)
  (forward m)
  (end_fill))
)
;(rectangle 60 20)

(define (leaf c r)
    (pendown)
    (color c)
    (begin_fill) 
    (circle r)
    (end_fill))

;(leaf '"red")

(define (try h c r)
    (if (< h 10)
    (leaf c r)
        (begin
        (color '"brown")
        (pendown)
    
        (rectangle h (/ h 20))
        
        (right 90)
        (forward h)
        (left 45)
        (try (/ h (/ 3 2)) '"dark green" 6)
        (color '"brown")
        (right 75)
        (try (/ h 2) '"green" 6)
        (color '"brown")
        (left 30)
        (try (/ h) '"palevioletred1" 5)
        (color '"brown")
        (backward h)
        )
    )

)

;(pixelsize 5)
;(speed 10)

;(penup)





(define (draw)
    (speed 10)
  (bgcolor '"light blue")
  (penup)
  (goto 200 -600)
  (try 500 '"" 10)
  
  (exitonclick))
  
; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
