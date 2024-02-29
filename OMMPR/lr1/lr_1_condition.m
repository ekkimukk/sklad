clc ;
close all ;
clear all ;

Aish =[3 4 3 8 9; 5 2 1 4 3; 4 9 4 6 7; 3 4 11 5 4; 8 9 8 7 1];
Bish =[61;43;79;87;58];
disp ('Введите номер варианта [1 . . . 30] ') ;
n = input ( ’n = ’) ;
if n <=0;
n =1;
elseif n >30;
n =30;
end
disp ( ’Исходные данные варианта’) ; disp ( n ) ;
A = Aish .+(2* n -1)
B = Bish .+(9* n -4)
% Векторные и матричные вычисления
disp ( ’Транспонированные матрицы A и В’) ;
Bt =B ’
At =A ’
disp ( ’Обратная матрица A с проверкой’) ;
Aobr = inv ( A )
provA = A * Aobr
disp ( ’Проверка матрицы A на ортогональность’) ;
Eort =At - Aobr
disp ( ’Матрица нормированных коэфф. СНорм=( Bt ) ’) ;
C =( Bt . - min ( Bt ) ) /( max ( Bt ) - min ( Bt ) )
disp ( ’Результат умнож. матриц FcbС=* B ’) ;
Fcb = C *B
disp ( ’Результат умнож. матриц Fbc = B * C ’) ;
Fbc = B *C
disp ( ’Определитель матрицы Fbc ’) ;
OFbc = det ( Fbc )
disp ( ’Находим минор М[1 ,2] матрицы Fbc ’) ;
MFbc12 =[ Fbc (2:5 ,1) , Fbc (2:5 ,3:5) ]
M12_Fbc = det ( MFbc12 )
disp ( ’Решаем СЛАУ Ax = B методом Гаусса’) ;
AGs = rref ([ A B ])
r = size ( AGs )
disp ( ’Вектор значений переменных [ X ] СЛАУ Ax = b ’) ;
XGs = AGs (: , r (2) )
disp ( ’Проверяем решение СЛАУ Ax - B =0 ’) ;
EpsGs = A * XGs - B
disp ( ’Решаем СЛАУ Ax = B методом обратной матрицы’) ;
Xom = inv ( A ) * B
disp ( ’Проверяем решение СЛАУ Ax - B =0 ’) ;
Epsom = A * Xom - B
% Запись результатов в файл
f_stud_N19 = fopen ( ’ Lab_rabota_1_stud_N19 . txt ’ , ’ wt ’) ;
fprintf ( f_stud_N19 , "Исходные данные варианта \ t % u \ n \ n " ,n ) ;
fprintf ( f_stud_N19 , ’Матрица А \ n ’) ;
dlmwrite ( f_stud_N19 ,A , ’\t ’) ; fprintf ( f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , ’Матрица B \ n ’) ;
dlmwrite ( f_stud_N19 ,B , ’\t ’) ; fprintf ( f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , ’Транспонированная матрица A \ n ’) ;
dlmwrite ( f_stud_N19 , At , ’\ t ’) ; fprintf ( f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , ’Транспонированная матрица B \ n ’) ;
dlmwrite ( f_stud_N19 , Bt , ’\ t ’) ; fprintf ( f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , ’Обратная матрица A \ n ’) ;
dlmwrite ( f_stud_N19 , Aobr , ’\ t ’ ," precision " ," %3.5 e " ) ; fprintf (
f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , ’Проверка обратной матрицы A \ n ’) ;
dlmwrite ( f_stud_N19 , provA , ’\ t ’ ," precision " ," %3.3 e " ) ; fprintf (
f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , ’Проверка матрицы A на ортогональность =[0] \ n ’)
;
dlmwrite ( f_stud_N19 , Eort , ’\ t \ t ’ ," precision " ," %3.3 f " ) ; fprintf
( f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , ’Матрица нормированных коэфф. СНорм=( Bt ) \ n ’) ;
dlmwrite ( f_stud_N19 ,C , ’\t ’ ," precision " ," %3.3 g " ) ; fprintf (
f_stud_N19 , ’\ n ’);
fprintf ( f_stud_N19 , "Результат умнож. матриц FcbС=* B = \ t % f \ n \ n " ,
Fcb ) ;
fprintf ( f_stud_N19 , ’Продолжаем вывод результатов модифицируя пример .
. . \ n ’) ;
fclose ( f_stud_N19 ) ;
% Построение графика
% Задаем область значений аргумента
AAx =[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
23 24 25];
% Вычисляем значение функции
muAAx =( AAx . -1) ./( AAx *( n +39) /( n +31) ) ;
AAx1 =[0 0.99]; % Добавляем недостающее нач. знач. арг.
muAAx1 =[0 0]; % Добавляем недостающее нач. знач. функ.
% рисуем и сохраняем в файл pdf
hf = figure () ;
hold on ;
plot ( AAx , muAAx , ’b ’ , ’ linewidth ’ ,4 , AAx1 , muAAx1 , ’b ’ , ’ linewidth ’
,4) ;
set ( gcf , ’ position ’ ,[100 100 600 300]) ; % Положение нижн. лев.
угла и разм окна в пикселях
set ( gca , ’ fontname ’ , ’ Liberation Serif ’) ; % Тип шрифта знач.
графика
set ( gca , ’ fontsize ’ ,20) ; % Размер шрифта знач. графика
set ( gca , ’ xtick ’ ,[0 5 10 15 20 25] , ’ xlim ’ ,[0 25] , ’ linewidth ’
,1.8) ; % позиции сетки на X
set ( gca , ’ ytick ’ ,[0 0.25 0.5 0.75 1] , ’ ylim ’ ,[0 1]) ; % позиции
сетки на Y
% вкл. сетку и подписываем оси
grid on ; xlabel ( " AA " , ’ fontsize ’ ,20) ; ylabel ( " \ mu ( AA ) " , ’
fontsize ’ ,20) ;
% Записываем график в файл
print ( hf , " Graf_LabRab_1 . pdf " , " - dpdf " ," - S600 ,300 " ) ; % сохр.
в PDF
print ( hf , " fig_LabRab_1 . jpg " , " - djpg " ," - S550 ,304 " ) ; % сохр.
в jpg
% Нахождение значения целевой функции графическим способом
k = round (((32 - n ) /(41 - n ) ) * n)
w = round (( n -k +6) /( n +1) )
t = -4* pi :0.1:3* pi ;
V1 =k * cos ( w* t ) +( n /( n +3) )* cos (3* w * t ) ;
V2 =k /2+ w *t -1;
hf = figure () ;
hold on ;
plot (t , V1 , ’b ’, ’ linewidth ’ ,4 ,t , V2 , ’g ’ , ’ linewidth ’ ,4) ;
set ( gcf , ’ position ’ ,[200 200 600 300]) ;
set ( gca , ’ fontsize ’ ,18) ;
grid on ;
print ( hf , " Resh_LabRab_1 . pdf " , " - dpdf " ," - S600 ,300 " ) ; % сохр.
в PDF
% Дописываем в файл значения k и w
f_stud_N19 = fopen ( ’ Lab_rabota_1_stud_N19 . txt ’ , ’ at ’) ;
fprintf ( f_stud_N19 , ’\ n ’) ;
fprintf ( f_stud_N19 , "k = \t % f \ n \ n " ,k ) ;
fprintf ( f_stud_N19 , "w = \t % f \ n \ n " ,w ) ;
fclose ( f_stud_N19 ) ;
