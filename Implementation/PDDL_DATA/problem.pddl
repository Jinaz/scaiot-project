(define (problem smrtroom) (:domain SMRTROOM)
;this was our template problem
(:objects
    r0 - room
    win1 - window
    outside - outside
    c1 - cooler
    h1 - heater
    d0 - door
    l0 - light 
    cu0 - curtain
)

(:init 
    (isSunny outside)
    
    ;(roomEmpty r0)
    ;(lectureTimeOver r0)
    (inLectureTime r0)
    
    (has_window r0 win1)
    (has_door r0 d0)
    (has_cooler c1 r0)
    (has_heater h1 r0)
    (has_light r0 l0)
    (has_curtain r0 cu0)
    
    (not (output-done r0))
    
    (presentingInRoom r0)
    
    (are_up cu0)
    (are_off l0)
    (are_closed win1)
    (is_unlocked d0)
    (is_off_heat h1)
    (is_off_cool c1)
    
    (= (temperature_wanted r0) 30)
    (= (actual_temp r0) 30)
    (= (outside_temp) 30)
    (= (outtemp) 0)
    
    (=(actual_lightlevel r0) 30)
    (=(wantedLightlevel r0) 30)
    (=(wantedLightlevelPPT r0) 40)

)

(:goal (and
        (output-done r0)
    )
)

)