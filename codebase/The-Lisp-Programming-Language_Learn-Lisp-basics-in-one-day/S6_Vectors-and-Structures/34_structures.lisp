(defstruct home 
    levels
    people
    name
)

(setq myhome (make-home :levels 4 :people 20 :name "my home"))

(write myhome) ; #S(HOME :LEVELS 4 :PEOPLE 20 :NAME "my home")