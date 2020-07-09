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
    (isSunny outside)
    
    (not(roomEmpty r0))
    
    (inLectureTime r0)
    
    (has_window r0 w0)
    (has_door r0 d0)
    (has_cooler c0 r0)
    (has_heater h0 r0)
    (has_light r0 l0)
    (has_curtain r0 c0)
    
    (not (output-done r0))
    
    (notpresentingInRoom r0)
    
    (are_up c0)
    (are_off l0)
    (are_closed w0)
    (is_unlocked d0)
    (is_off_heat h0)
    (is_off_cool c0)
    
    (= (temperature_wanted r0) 24)
    (= (actual_temp r0) -11.196819220738696)
    (= (outside_temp) 30)
    (= (outtemp) 0)
    
    (=(actual_lightlevel r0) 46.5)
    (=(wantedLightlevel r0) 45)
    (=(wantedLightlevelPPT r0) 35)

)

(:goal (and
        (output-done r0)
    )
)

)