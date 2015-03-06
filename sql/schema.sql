create table Card
(
	sn int not null,
	card_id int unsigned auto_increment,
	primary key (card_id),
	UNIQUE(sn)
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
	comments varchar(320),
	INDEX (card_id),
	INDEX (person_id)
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
	attachmime varchar (30),
	attachdesc varchar (120),
	comments varchar (200),
	originalname varchar (200),
	INDEX (test_id)
);

create table Card_Info_Types
(
	info_type_id int unsigned auto_increment,
	primary key (info_type_id),
	Info_Name varchar (30),
	Info_Desc_Short varchar (100),
	Info_Desc_Long varchar (300)
);

create table Card_Info
(
	info_id int unsigned auto_increment,
	primary key (info_id),
	card_id int not null,
	info_type int not null,
	info varchar (300),
	INDEX(card_id),
	INDEX(info_type)
);

create table TestRevoke
(
	test_id int unsigned not null,
	primary key(test_id),
	comment varchar(120)
);
