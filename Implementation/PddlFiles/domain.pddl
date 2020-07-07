(define (domain SMRTROOM)

  (:requirements :strips :fluents :typing :negative-preconditions :disjunctive-preconditions )

  (:types
    room window outside cooler heater humidity light door curtain
  )

  (:predicates
        ;cooler is operational and ready
        (has_cooler ?c - cooler ?r - room)
        (is_on_cool ?c - cooler)
        (is_off_cool ?c - cooler)
        
        ;heater is operational and ready
        (has_heater ?h - heater ?r - room)
        (is_on_heat ?h - heater)
        (is_off_heat ?h - heater)
        
        ; window properties
        (has_window ?r - room ?win - window) ;room has windows
        (are_closed ?win - window)
        (are_open ?win - window)
        
        ;curtain properties
        (has_curtain ?r - room ?cu - curtain)
        (are_down ?cu - curtain)
        (are_up ?cu - curtain)
        
        ;door properties
        (has_door ?r - room ?d - door)
        (is_locked ?d - door)
        (is_unlocked ?d - door)
        
        ;Light properties
        (has_light ?r - room ?l - light)
        (are_dimmed ?l - light)
        (are_off ?l - light)
        (are_fully_on ?l - light)
        
        ;outside Properties 
        (isSunny ?o - outside)
        (isRainy ?o - outside)
        (isCloudy ?o - outside)
        (isSnowing ?o - outside)
        
        ;room Properties
        (peopleInRoom ?r - room)
        (roomEmpty ?r - room)
        ;lecture 
        (lectureTimeOver ?r - room)
        (firstlecture ?r - room)
        (inLectureTime ?r - room)
        (betweenLectures ?r - room)
        ;beamer
        (presentingInRoom ?r - room)
        (notpresentingInRoom ?r - room)
        ;termination of algorithm
        (output-done ?r - room)
        
  ) 
  
    (:functions 
    (temperature_wanted ?r - room)
    (humidity_wanted ?r - room)
    
    (outsideLightLevel)
    
    (actual_temp ?r - room)
    (actual_hum ?r - room)
    
    (outside_temp)
    (outside_hum)
    
    (actual_lightlevel ?r - room)
    (wantedLightlevel ?r - room)
    (wantedLightlevelPPT ?r - room)
    
    (timeneeded)
    
    (tempdiff ?r - room)
    (humdiff ?r - room)
    
    (outtemp)
    
    )
    
    
    ;temperature related
    (:action heater_On
        :parameters (?r - room ?o - outside ?h - heater)
        :precondition (and
                        (inLectureTime ?r)
                        (has_heater ?h ?r)
                        (is_off_heat ?h)
                        
                        (or (and
                            (> (temperature_wanted ?r) (actual_temp ?r))
                            (>= (actual_temp ?r) (outside_temp))
                            )
                            (and
                                (or
                                (isRainy ?o)
                                (isSnowing ?o)
                                )
                                (< (temperature_wanted ?r) (actual_temp ?r)) 
                            )
                        
                        )
                    
                    )
        :effect (and
            (is_on_heat ?h)
            (not (is_off_heat ?h))
            (assign (outtemp) (temperature_wanted ?r) )
            (output-done ?r)
            
        )
    )
    
    (:action heater_Off
        :parameters (?r - room ?o - outside ?h - heater)
        :precondition (or
                        (and
                        (inLectureTime ?r)
                        (has_heater ?h ?r)
                        (is_on_heat ?h)
                        (= (temperature_wanted ?r) (actual_temp ?r))
                        )
                        (and
                        (roomEmpty ?r)
                        (lectureTimeOver ?r)
                        (has_heater ?h ?r)
                        (is_on_heat ?h)
                        )
        )
        :effect (and
            (is_off_heat ?h)
            (not (is_on_heat ?h))
            (output-done ?r)
        )
    )
    (:action cooler_On
        :parameters (?r - room ?o - outside ?c - cooler)
        :precondition (and
                        (inLectureTime ?r)
                        (has_cooler ?c ?r)
                        (is_off_cool ?c)
                        
                        (or
                        (and
                        (< (temperature_wanted ?r) (actual_temp ?r))
                        (<= (actual_temp ?r) (outside_temp))
                        )
                        (and
                            (or
                                (isRainy ?o)
                                (isSnowing ?o)
                            )
                            (> (temperature_wanted ?r) (actual_temp ?r))
                        )
                        )
        
        )
        :effect (and
            (is_on_cool ?c)
            (not (is_off_cool ?c))
            (assign (outtemp) (temperature_wanted ?r)  )
            (output-done ?r)
            
        )
    )
    (:action cooler_Off
        :parameters (?r - room ?o - outside ?c - cooler)
        :precondition (or
                        (and
                        (inLectureTime ?r)
                        (has_cooler ?c ?r)
                        (is_on_cool ?c)
                        (= (temperature_wanted ?r) (actual_temp ?r))
                        )
                        (and
                        (roomEmpty ?r)
                        (lectureTimeOver ?r)
                        (has_cooler ?c ?r)
                        (is_on_cool ?c)
                        )
        )
        :effect (and
            (is_off_cool ?c)
            (not (is_on_cool ?c))
            (output-done ?r)
        )
    )
    
    (:action open_Windows
        :parameters (?r - room ?o - outside ?win - window)
        :precondition (and
                        (or
                            (isSunny ?o)
                            (isCloudy ?o)
                        )
                        (inLectureTime ?r)
                        (has_window ?r ?win)
                        (are_closed ?win)
                        
                        (or 
                            (and
                                (> (temperature_wanted ?r) (actual_temp ?r))
                                (< (actual_temp ?r) (outside_temp))
                            )
                            (and
                                (< (temperature_wanted ?r) (actual_temp ?r))
                                (> (actual_temp ?r) (outside_temp))
                            )
                        )
        )
        :effect (and
            (are_open ?win)
            (not (are_closed ?win))
            (assign (outtemp) (temperature_wanted ?r) )
            (output-done ?r)
            
        )
    )
    (:action close_Windows
        :parameters (?r - room ?o - outside ?win - window)
        :precondition  (or
                        (and
                        (inLectureTime ?r)
                        (has_window ?r ?win)
                        (are_open ?win)
                        (= (temperature_wanted ?r) (actual_temp ?r))
                        )
                        (and
                            (roomEmpty ?r)
                            (lectureTimeOver ?r)
                            (has_window ?r ?win)
                            (are_open ?win)
                        )
                        )
        :effect (and
            (are_closed ?win)
            (not (are_open ?win))
            (output-done ?r)
        )
    )
    (:action nothing
        :parameters (?r - room ?o - outside ?win - window ?l - light)
        :precondition (and
                        (inLectureTime ?r)
                        (has_window ?r ?win)
                        (are_closed ?win)
                        (= (temperature_wanted ?r) (actual_temp ?r))
                        (= (actual_temp ?r) (outside_temp))
                        (or
                            (and
                            
                            (= (wantedLightlevel ?r) (actual_lightlevel ?r))
                            (notpresentingInRoom ?r)
                            )
                            (and
                            (= (wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                            (presentingInRoom ?r)
                            )
                        )
        )
        :effect (and
            (output-done ?r)
        )
    )
    
    ;humidity related
    (:action refresh_air
        :parameters (?r - room ?o - outside ?win - window)
        :precondition (and
                        (betweenLectures ?r)
                        (has_window ?r ?win)
                        (are_closed ?win)
                        (or 
                            (and
                                (< (humidity_wanted ?r) (actual_hum ?r))
                                (> (actual_hum ?r) (outside_hum))
                            )
                            (and
                                (> (humidity_wanted ?r) (actual_hum ?r))
                                (< (actual_hum ?r) (outside_hum))
                            )
                        )
        )
        :effect (and
            (are_open ?win)
            (not (are_closed ?win))
            (output-done ?r)
        )
    )
    
    ;light related
    (:action dimLightsup
        :parameters (?r - room ?o - outside ?l - light ?cu - curtain)
        :precondition (and
                    (has_light ?r ?l)
                    (inLectureTime ?r)
                    (are_off ?l)
                    (has_curtain ?r ?cu)
                    (are_up ?cu)
                    (or
                        (and
                            (presentingInRoom ?r)
                            (>(wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        )
                        (and
                            (notpresentingInRoom ?r)
                            (>(wantedLightlevel ?r) (actual_lightlevel ?r))
                        )
                    )    
        )
        :effect (and
            (are_dimmed ?l)
            (not (are_off ?l))
            (output-done ?r)
        )
    
    )
    (:action dimLightsdown
        :parameters (?r - room ?o - outside ?l - light ?cu - curtain)
        :precondition (and
                    (has_light ?r ?l)
                    (inLectureTime ?r)
                    (are_fully_on ?l)
                    (has_curtain ?r ?cu)
                    (are_down ?cu)
                    (or
                        (and
                            (notpresentingInRoom ?r)
                            (< (wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        )
                        (and
                            (presentingInRoom ?r)
                            (< (wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        )
                    )
        )
        :effect (and
            (are_dimmed ?l)
            (not (are_fully_on ?l))
            (output-done ?r)
        )
    
    )
    (:action fullLights
        :parameters (?r - room ?o - outside ?l - light ?cu - curtain)
        :precondition (and
                    (has_light ?r ?l)
                    (inLectureTime ?r)
                    (are_dimmed ?l)
                    (has_curtain ?r ?cu)
                    (are_up ?cu)
                    (or
                        (and
                            (presentingInRoom ?r)
                            (>(wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        )
                        (and
                            (notpresentingInRoom ?r)
                            (>(wantedLightlevel ?r) (actual_lightlevel ?r))
                        )
                    )    
        )
        :effect (and
            (are_fully_on ?l)
            (not (are_dimmed ?l))
            (output-done ?r)
        )
    )
    (:action lightsOff
        :parameters (?r - room ?o - outside ?l - light ?cu - curtain)
        :precondition (or
                    (and
                    (has_light ?r ?l)
                    (inLectureTime ?r)
                    (are_dimmed ?l)
                    (has_curtain ?r ?cu)
                    (are_down ?cu)
                    (or
                        (and
                            (notpresentingInRoom ?r)
                            (< (wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        )
                        (and
                            (presentingInRoom ?r)
                            (< (wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        )
                    )
                    )
                    (and
                        (roomEmpty ?r)
                        (lectureTimeOver ?r)
                        (or
                            (are_dimmed ?l)
                            (are_fully_on ?l)
                        )
                    )
        )
        :effect (and
            (are_off ?l)
            (not (are_dimmed ?l))
            (output-done ?r)
        )
    )
    (:action curtain_up 
        :parameters (?r - room ?o - outside ?cu - curtain)
        :precondition  (and
                    (inLectureTime ?r)
                    (has_curtain ?r ?cu)
                    (are_down ?cu)
                    (or
                        (and
                        (> (wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        (presentingInRoom ?r)
                        )
                        (and
                        (> (wantedLightlevel ?r) (actual_lightlevel ?r))
                        (notpresentingInRoom ?r)
                        )
                        
                    )
                )
        :effect (and
            (not (are_down ?cu))
            (are_up ?cu)
            (output-done ?r)
        )
    )
    (:action curtain_down 
        :parameters (?r - room ?o - outside ?cu - curtain)
        :precondition (and
                    (inLectureTime ?r)
                    (has_curtain ?r ?cu)
                    (are_up ?cu)
                    (or
                        (and
                        (< (wantedLightlevelPPT ?r) (actual_lightlevel ?r))
                        (presentingInRoom ?r)
                        )
                        (and
                        (< (wantedLightlevel ?r) (actual_lightlevel ?r))
                        (notpresentingInRoom ?r)
                        )
                    )
                )
        :effect (and
            (not (are_up ?cu))
            (are_down ?cu)
            (output-done ?r)
        )
    )
    
    ;door related
    (:action unlockRoom
        :parameters (?r - room ?d - door ?l - light)
        :precondition (and
                        (firstlecture ?r)
                        (has_door ?r ?d)
                        (is_locked ?d)
                        (has_light ?r ?l)
                        (are_off ?l)
        )
        :effect (and 
            (not (is_locked ?d))
            (is_unlocked ?d)
            (are_fully_on ?l)
        )
    )
    
    (:action lockRoom 
        :parameters (?r - room ?d - door)
        :precondition (and
                    (roomEmpty ?r)
                    (lectureTimeOver ?r)
                    (has_door ?r ?d)
                    (is_unlocked ?d)
        )
        :effect (and
            (not (is_unlocked ?d))
            (is_locked ?d)
        )
    )
)