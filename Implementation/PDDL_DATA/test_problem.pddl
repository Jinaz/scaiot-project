(define (problem smrtroom) (:domain SMRTROOM)
;this was our template problem
(:objects
    r0 - room
    w0 - window
    outside - outside
    c0 - cooler
    h0 - heater
    d0 - door
    l0 - light 
    c0 - curtain
)

(:init 
    (isCloudy outside)
    
    (not(roomEmpty r0))
    
    (inLectureTime r0)
    
    (has_window r0 w0)
    (has_door r0 d0)
    (has_cooler c0 r0)
    (has_heater h0 r0)
    (has_light r0 l0)
    (has_curtain r0 c0)
    
    (not (output-done r0))
    
    (presentingInRoom r0)
    
    (are_down c0)
    (are_off l0)
    (are_closed w0)
    (is_unlocked d0)
    (is_off_heat h0)
    (is_off_cool c0)
    
    (= (temperature_wanted r0) 30)
    (= (actual_temp r0) 30)
    (= (outside_temp) 26)
    (= (outtemp) 0)
    
    (=(actual_lightlevel r0) 30)
    (=(wantedLightlevel r0) 30)
    (=(wantedLightlevelPPT r0) 20)

)

(:goal (and
        (output-done r0)
    )
)

)