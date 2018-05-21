clear;
% Uzkraunami duomenys
load scores.txt;
close all;
% Pavaizduojamas saules demiu grafikas nuo 1700-1950
figure(1);
plot(scores(:,1),scores(:,2),'r-*');
xlabel('Varzybu numeris');
ylabel('Tasku skaicius');
title('Komandos taskai');

% Sukuriamos duomenu ir siekiamu rezultatu matricos
L = length(scores); 	% duomenø kiekis
P = [scores(1:L-12,2)' ; 	% ávesties duomenø
     scores(2:L-11,2)' ;
     scores(3:L-10,2)' ;
     scores(4:L-9,2)' ;
     scores(5:L-8,2)' ;
     scores(6:L-7,2)' ;
     scores(7:L-6,2)' ; 	% ávesties duomenø
     scores(8:L-5,2)' ;
     scores(9:L-4,2)' ;
     scores(10:L-3,2)' ;]; 	% matrica
T = scores(11:L,2)'; 	% iðvesties duomenø vektorius

% sudaromos matricos apmokymui
Pu = P(:,1:50);
Tu = T(:,1:50);  

% tinklo sukurimas ir apmokymas tiesioginiu metodu
% net = newlind(Pu, Tu);
% tiesinio neurono sukurimas ir apmokymas
net = newlin(P, T, 0, maxlinlr(Pu, 0)/2);
net.trainParam.goal = 100; 
net.trainParam.epochs = 1000;
net = train(net, Pu, Tu); 

% generuojamas rezultatu vektorius
Tsu = sim(net,Pu);
figure(3);
hold on;

% pavaizduojamos spejamos ir tikros saules demiu reiksmes
plot(Tu(:,1:50),'b-*');
plot(Tsu(:,1:50),'r-*');
legend('Tikros','Spejamos');
title('Spejamos ir tikros varzybu tasku reiksmes');
xlabel('Varzybos');
ylabel('Spejami ir tikri taskai');

% gaunamas rezultatu vektorius ir jo vaizdavimas
Ts = sim(net,P);
figure(4);
hold off;

% santykis spejamu ir tikru reiksmiu
e = T(:,1:50)-Ts(:,1:50);
plot(abs(e),'b-*');
title('Ts ir T reiksmiu lyginamasis grafikas');
xlabel('Taskai buve');
ylabel('Taskai dabartiniai');

% prognozes klaidu histograma is apskaiciuoto santykio e
figure(5)
hist(e);
title('Prognozes klaidu histograma');
xlabel('Paklaidu dydziai');
ylabel('Paklaidu daznumas');

