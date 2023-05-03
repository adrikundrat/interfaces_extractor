create table if not exists public.interface
(
    id              serial
        primary key,
    connection      integer,
    name            varchar(255) not null,
    description     varchar(255),
    config          json,
    type            varchar(50),
    infra_type      varchar(50),
    port_channel_id integer
        references public.interface,
    max_frame_size  integer
);