drop database if exists municipios;
create database if not exists municipios CHARACTER SET utf8 COLLATE utf8_general_ci;
use municipios;
create table departamento(
iddepartamento int primary key auto_increment,
departamento varchar(15)
);
insert into departamento(departamento) values("Putumayo");
insert into departamento(departamento) values("Nariño");
insert into departamento(departamento) values("Antioquia");
create table municipio(
idmunicipio int primary key auto_increment,
municipio varchar(15),
iddepartamento int,
foreign key (iddepartamento) references departamento(iddepartamento)
);




