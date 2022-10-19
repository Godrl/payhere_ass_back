create table user
(
    id         int auto_increment
        primary key,
    email      varchar(256)                       not null,
    password   varchar(256)                       not null,
    created_at datetime default CURRENT_TIMESTAMP not null,
    updated_at datetime default CURRENT_TIMESTAMP not null
);
