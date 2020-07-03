(define (problem smr-temp)
    
    (:domain 
        SMR-ROOM
    )
    
    (:objects 
        room0 
        windows 
        beamer
        climate
        door
        calendar
        time
        lights
        )
    (:init
        (room room0)
    
        (= (room-Temp room0) 28)
        (= (room-hum room0) 80)
        (= (outside-Hum room0) 40)
        (= (windowState room0) 30)
        
        
        
    )
    (:goal
        (and
            (< (room-Hum room0) 60)
            (< (windowState room0) 90)
        )
    )
)