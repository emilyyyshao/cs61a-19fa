
; Tail recursion

(define (replicate x n)
  (define (helper k sofar)
    (if (= k 0) sofar
        (helper (- k 1) (cons x sofar)))) 
  (helper n nil)
)

(define (accumulate combiner start n term)
  (if (= n 0) start
      (accumulate combiner (eval (cons 'combiner (list start (eval (term n))))) (- n 1) term))
)

(define (accumulate-tail combiner start n term)
  (define (helper k m)
    (if (= m 0) k
      (helper (eval (cons 'combiner (list k (term m)))) (- m 1))))
  (helper start n)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define (int-stream start) (cons-stream start (int-stream (+ start 1))))
(define multiples-of-three
  (map-stream (lambda (x) (* x 3)) (int-stream 1))
)


(define (nondecreastream s)
  (define (helper1 lst n)
    (cond ((null? lst) 0)
          ((null? (cdr-stream lst)) (+ 1 n))
          ((> (car lst) (car (cdr-stream lst))) (+ 1 n))
          (else (helper1 (cdr-stream lst) (+ 1 n)))))
  (define (helper2 lst n)
    (if (or (null? lst) (= n 0)) lst (helper2 (cdr-stream lst) (- n 1))))
  (define (helper3 lst n)
    (if (or (null? lst) (= n 0)) nil (append (list (car lst)) (helper3 (cdr-stream lst) (- n 1)))))
  (if (null? s) s
    (cons-stream (helper3 s (helper1 s 0)) (nondecreastream (helper2 s (helper1 s 0))))))

(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))