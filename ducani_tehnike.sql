--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

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
-- Name: ducani_tehnike; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ducani_tehnike (
    ducan_id bigint NOT NULL,
    naziv character varying,
    adresa character varying,
    grad character varying,
    drzava character varying,
    telefonski_broj character varying,
    email character varying,
    geolokacija character varying,
    recenzija double precision,
    postanski_broj character varying
);


ALTER TABLE public.ducani_tehnike OWNER TO postgres;

--
-- Name: vlasnici; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vlasnici (
    id bigint NOT NULL,
    ime character varying,
    prezime character varying,
    ducan_id bigint
);


ALTER TABLE public.vlasnici OWNER TO postgres;

--
-- Data for Name: ducani_tehnike; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ducani_tehnike (ducan_id, naziv, adresa, grad, drzava, telefonski_broj, email, geolokacija, recenzija, postanski_broj) FROM stdin;
1	Links.hr	Dankovečka ulica 5	Zagreb	Hrvatska	013096944	 dubrava@links.hr	45.83, 16.06	4.4	10040 
2	Elipso	Ulica Rudolfa Kolaka 14	Zagreb	Hrvatska	015533094	podrska@links.hr	45.84, 16.05	4.1	10040 
3	Laptopi.hr	Dugoselska ulica 12	Zagreb	Hrvatska	016182261	prodaja@pc1.hr	45.80, 16.02	2.8	10000 
4	Sancta Domenica	Vukovarska ulica 207	Split	Hrvatska	072336955	podrska@sancta-domenica.hr	43.51, 16.50	4.4	21000
5	Instar	Ulica Josipa Jovića 93	Split	Hrvatska	021440214	split@instar-informatika.hr	43.61, 16.48	4.4	21000
6	HGSPOT	Užarska ulica 18	Rijeka	Hrvatska	051317475	rijeka@hgspot.hr	45.51, 14.42	4.6	51000
7	Svijet medija	Trg Drage Iblera 10	Zagreb	Hrvatska	014554882	importanne.galleria@svijet-medija.hr	45.85, 16.00	4.3	10000
9	Tehno Mag	Tehno Mag	Zagreb	Hrvatska	015790602	webshop@tehno-mag.hr	45.81, 16.10	4.3	10000
10	Saturn	Alexanderplatz 3	Berlin	Njemačka	4922122243333	shop@saturn.de	52.52, 13.41	4.2	10178
8	Emmezeta	Ulica Siniše Glavaševića 1	Zagreb	Hrvatska	072202022	info@emmezeta.hr	45.80, 16.05	4.3	10000
\.


--
-- Data for Name: vlasnici; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vlasnici (id, ime, prezime, ducan_id) FROM stdin;
1	Vedran	Puškarić	1
5	Robert 	Škeljo	4
3	Bernard	Šepetanc	2
2	Denis	Piljek	1
6	Marko	Cvetovski	5
8	Saša	Lončar	6
7	Vedrana	Lončar	6
12	Karsten	Wildberger	10
11	Zlatko	Marošević	9
9	Anđelko	Ćurić	7
10	Andrzej	Pawel Sitarz	8
13	Emil	Bogdan	3
\.


--
-- Name: ducani_tehnike ducani_tehnike_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ducani_tehnike
    ADD CONSTRAINT ducani_tehnike_pkey PRIMARY KEY (ducan_id);


--
-- Name: vlasnici vlasnici_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vlasnici
    ADD CONSTRAINT vlasnici_pkey PRIMARY KEY (id);


--
-- Name: fki_m; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_m ON public.vlasnici USING btree (ducan_id);


--
-- PostgreSQL database dump complete
--

