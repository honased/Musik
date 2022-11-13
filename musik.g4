grammar musik;

// start var
prog: (decl | loop)+ EOF
    ;

decl: 'let' ID '=' val                  # DeclareT
    ;

loop: 'loop' '{' expr+ '}'              # LoopT
    ;

// ANTLR resolves ambiguities in favor of the alternative given first.
expr: 'if' num '{' expr+ '}'            # IfT
    | ID '=' val                        # AssignT
    | func                              # FuncT
    | val                               # ValT
    ;

val: num                                # NumT
    | sound                             # SoundT 
    ;

num: ID                                 # IdNumT 
    | num '*' num                       # MultT
    | num '/' num                       # DivT
    | num '%' num                       # ModT
    | num '+' num                       # AddT
    | num '-' num                       # MinusT
    | NUM                               # NumValT
    | 'not' num                         # NotT
    ;

sound: ID # IdSoundT
    | 'sin_wave' num                    # SinWaveT
    | 'square_wave' num                 # SquareWaveT
    | 'noise_wave' num                  # NoiseWaveT
    | 'saw_wave' num                    # SawWaveT
    | 'triangle_wave' num               # TriangleWaveT
    | 'mix' sound sound                 # MixT
    | 'pitch_shift' sound num           # PitchShiftT
    | 'pitch_shift_semi' sound num      # PitchShiftSemiT
    ;

func: 'sleep' num                       # SleepT
    | 'play' sound num                  # PlayT
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