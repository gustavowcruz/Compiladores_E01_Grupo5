grammar RoboLang;


programa        : ROBO ID LBRACE listaComandos RBRACE EOF;

listaComandos   : comando* ;

comando         : mover
                | virar
                | velocidade
                | esperar
                | repetir
                ;

mover           : MOVER EIXO distancia ;

virar           : VIRAR angulo ;

velocidade      : VELOCIDADE NUMBER ;

esperar         : ESPERAR NUMBER MS? ; // O '?' torna o 'ms' opcional

repetir         : REPETIR NUMBER LBRACE listaComandos RBRACE ;

distancia       : NUMBER unidade ;

angulo          : NUMBER GRAUS ;

unidade         : CM | M ;


ROBO        : 'robo';
MOVER       : 'mover';
VIRAR       : 'virar';
VELOCIDADE  : 'velocidade';
ESPERAR     : 'esperar';
REPETIR     : 'repetir';
GRAUS       : 'graus';
CM          : 'cm';
M           : 'm';
MS          : 'ms';
EIXO        : 'x' | 'y' | 'z';
LBRACE      : '{';
RBRACE      : '}';
ID          : [a-zA-Z][a-zA-Z0-9]*;
NUMBER      : [0-9]+ ('.' [0-9]+)?;
WS          : [ \t\r\n]+ -> skip;
