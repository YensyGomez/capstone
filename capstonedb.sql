--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: helena
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying,
    age integer,
    gender character varying
);


ALTER TABLE public.actors OWNER TO helena;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: helena
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO helena;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: helena
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: helena
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO helena;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: helena
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying,
    release_date date
);


ALTER TABLE public.movies OWNER TO helena;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: helena
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO helena;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: helena
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: helena
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: helena
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: helena
--

COPY public.actors (id, name, age, gender) FROM stdin;
1	Manolo Cardona	47	HOMBRE
2	Sean Connery	80	HOMBRE
3	Maria Conchita Alonso	60	MUJER
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: helena
--

COPY public.alembic_version (version_num) FROM stdin;
900cee1246a6
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: helena
--

COPY public.movies (id, title, release_date) FROM stdin;
1	Quien mato a Sara	2020-12-17
2	Doctor No	1962-12-17
3	Depredador	0190-12-17
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: helena
--

SELECT pg_catalog.setval('public.actors_id_seq', 3, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: helena
--

SELECT pg_catalog.setval('public.movies_id_seq', 3, true);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: helena
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: helena
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: helena
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

