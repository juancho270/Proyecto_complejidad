var 0..1: V1; var 0..1 : n_V1;
var 0..1: V2; var 0..1 : n_V2;
var 0..1: V3; var 0..1 : n_V3;
var 0..1: V4; var 0..1 : n_V4;
var 0..1: V5; var 0..1 : n_V5;
var 0..1: V6; var 0..1 : n_V6;

% Valores asociados a los literales
constraint V1 + n_V1 = 1;
constraint V2 + n_V2 = 1;
constraint V3 + n_V3 = 1;
constraint V4 + n_V4 = 1;
constraint V5 + n_V5 = 1;
constraint V6 + n_V6 = 1;
% Clausulas
constraint n_V2 + V3 >= 1;
constraint V4 + V5 >= 1;
constraint V6 >= 1;
