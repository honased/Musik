grammar musik;

// start var
prog: (decl | expr)+ EOF
    ;

decl: 'let' ID '=' (num | sound)       # DeclareT
    ;

// ANTLR resolves ambiguities in favor of the alternative given first.
expr: 'loop' '{' expr+ '}'              # LoopT
    | func                              # FuncT
    | sound                             # SoundT
    | num                               # NumberT
    | ID '=' (num | sound)              # AssignT
    | ID                                # IdT
    ;

num: num '*' num                        # MultT
    | num '/' num                       # DivT
    | num '%' num                       # ModT
    | num '+' num                       # AddT
    | num '-' num                       # MinusT
    | NUM                               # NumValT
    ;

sound: 'sin_wave' num                   # SinWaveT
    | 'square_wave' num                 # SquareWaveT
    | 'mix' sound sound                 # MixT
    | 'pitch_shift' sound num           # PitchShiftT
    ;

func: 'sleep' num                       # SleepT
    | 'play' sound                      # PlayT
    | 'print' expr                      # PrintT
    ;

/* Tokens */
ID: [a-z][a-zA-Z0-9_]*;
NUM: '0' | '-'?[1-9][0-9]*;
INT_TYPE: 'int';
SOUND_TYPE: 'sound';
COMMENT: '--'~[\r\n]* -> skip;
WS : [ \t\n]+ -> skip;
NEW_LINE: [\r\n] -> skip;