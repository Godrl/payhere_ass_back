create table household_ledger
(
    id         int auto_increment
        primary key,
    user_id    int                                not null,
    money      int                                not null,
    content    varchar(256)                       not null,
    is_deleted tinyint(1)                         not null,
    created_at datetime default CURRENT_TIMESTAMP not null,
    updated_at datetime default CURRENT_TIMESTAMP not null,
    constraint household_ledger_ibfk_1
        foreign key (user_id) references user (id)
);

create index user_id
    on household_ledger (user_id);
