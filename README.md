# Disklavier-Echo-Effect

Project as part of MUS 305 at the University of Illinois Champaign-Urbana, under the course direction of Dr. Heinrich Taube

- This project aims to simulate an "echo" effect on a Yamaha Disklavier piano, on up to 16 key simulatenously, with repetitions and diminishing of echo sound up to the performer.
- The program runs using the musx library and uses threading to run real-time outputs to a Yamaha Disklavier.

# Running the program

- Have a computer connected to a Yamaha Disklavier.
- In a terminal, do `python -m realtime (repeat) (sustain) (cutoff)`
  - `repeat` defines the number of repetitions that are played following the initial note
  - `sustain` defines the number of seconds each repetition is held for
  - `cutoff` defines a midi note number where lower notes maintain the echo functionality, and higher notes play like a normal piano. An option to invert this            feature is still in progress.
