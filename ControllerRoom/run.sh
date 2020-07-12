#!/bin/bash

# Read the user input
while true; do
  echo "Enter command, for help type \"help\" "
  read x
  if [ "$x" = "help" ]; then
    echo "valid commands:"
    echo "roomstatus"
    echo "heater_on"
    echo "heater_off"
    echo "ac_on"
    echo "ac_off"
    echo "lights_off"
    echo "lights_dim"
    echo "lights_on"
    echo "door_lock"
    echo "door_unlock"
    echo "window_open"
    echo "window_close"
    echo "curtain_open"
    echo "curtain_close"
    echo "exit"
  fi
  if [ "$x" = "roomstatus" ]; then
    python3 OutsideController roomstatus
  fi

  if [ "$x" = "heater_on" ]; then
    python3 OutsideController heater_on
  fi

  if [ "$x" = "heater_off" ]; then
    python3 OutsideController heater_off
  fi

  if [ "$x" = "ac_on" ]; then
    python3 OutsideController cooler_on
  fi
  if [ "$x" = "ac_off" ]; then
    python3 OutsideController cooler_off
  fi
  if [ "$x" = "lights_off" ]; then
    python3 OutsideController light_off
  fi
  if [ "$x" = "lights_dim" ]; then
    python3 OutsideController light_dom
  fi
  if [ "$x" = "lights_on" ]; then
    python3 OutsideController light_on
  fi
  if [ "$x" = "door_lock" ]; then
    python3 OutsideController lock_door
  fi
  if [ "$x" = "door_unlock" ]; then
    python3 OutsideController unlock_door
  fi
  if [ "$x" = "window_open" ]; then
    python3 OutsideController window_open
  fi
  if [ "$x" = "window_close" ]; then
    python3 OutsideController window_close
  fi
  if [ "$x" = "curtain_open" ]; then
    python3 OutsideController curtain_up
  fi
  if [ "$x" = "curtain_close" ]; then
    python3 OutsideController curtain_down
  fi

  if [ "$x" = "exit" ]; then
    break
  fi
done
