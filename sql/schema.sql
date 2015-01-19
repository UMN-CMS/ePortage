create table Card
(
	sn int not null,
	Mac_address char(18),
	card_id int unsigned auto_increment,
	primary key (card_id)
);

create table Test_Type
(	
	test_type int unsigned auto_increment,
	primary key (test_type),
	name varchar(30),
	required tinyint(1) not null,
	desc_short varchar(50),
	desc_long varchar(250),
	relative_order int not null
);

create table Test
(
	test_id int unsigned auto_increment,
	primary key (test_id),
	test_type_id int not null,
	card_id int not null,
	person_id int not null,
	day timestamp not null, 
	successful tinyint(1) not null,
	comments varchar(320)
); 	

create table People
(
	person_id int unsigned auto_increment,
	primary key (person_id),
	person_name varchar (100)
);

create table Attachments
(
	attach_id int unsigned auto_increment,	
	primary key (attach_id),
	test_id int,
	attachdesc varchar (120),
	comments varchar (200),
	attachpath varchar (250)
); 
