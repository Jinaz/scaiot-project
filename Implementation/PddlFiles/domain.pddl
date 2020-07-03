(define (domain SMR-ROOM)
    (:requirements [:strips] [:typing] [:equality] [:adl] [:conditional-effects])
    (:predicates 
        (room ?room)
        (window ?window)
        (climate ?climate)
        (light ?light))
    (:functions
        (room-hum ?room)
        (outside-Hum ?room)
        (room-Temp ?room)
        (windowState ?room))
    (:action openWindowsHum
        :parameters (
                    ?room
                    )
        :precondition (and 
                    (>(room-hum ?room) 60)
                    (<(outside-Hum ?room) 50)
                    (<(windowState ?room) 89))
        :effect (and
                (increase (windowState ?room) 5)
                (decrease (room-Hum ?room) 10)
                )
    )


)