;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond ((= x 0) 0) ((< x 0) -1) (else 1))
)

(define (square x) (* x x))

(define (pow b n)
  (cond ((= n 0) 1)
        ((= n 1) b)
        (else (* b (pow b (- n 1)))))
)

(define (unique s)
    (cond ((equal? s nil) s)
         (else (cons (car s) (filter (lambda (x) (not (equal? x (car s)))) (unique(cdr s))))))
)