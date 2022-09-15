create database DBZP;
use DBZP;
create table Personaje(id int, nombre varchar(50), sayayin boolean, humano boolean, androide boolean, namek boolean, otroalien boolean, Demonio boolean, pelo boolean, vistenaranja boolean, rosa boolean, verde boolean, realeza boolean);
alter table Personaje add (guerrero int,joven int,viejo int,mujer int,hombre int, bajito int,gordo int, morado int, fusionpotara int, fusionbaile int, esdelfuturo int, azul int, guiniu int );
alter table Personaje modify column id int auto_increment;

insert into personaje(nombre, sayayin, humano, androide, namek, otroalien, demonio, pelo, vistenaranja, rosa, verde,realeza)
values('GOKU', TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE,TRUE,FALSE,FALSE,FALSE);

use DBZP;
create table Propiedad(id int, propiedad varchar(50));
insert into Propiedad(id,propiedad)
values(1,'sayayin');
alter table Propiedad add primary key (id);
alter table Propiedad modify column id int auto_increment;


